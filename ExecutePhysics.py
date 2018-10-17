import pygame as pg
import pymunk as pm
import pymunk.pygame_util as pygame_util
from pymunk.vec2d import Vec2d
import sys
import Rockets.TestRocket as tr
import math
from Physics.Physics import Physics as phy
import Graphics.headsUpDisplay as hud

res_x, res_y = 1000, 1000
EARTH_MASS = 5.97*10**24
EARTH_RADIUS = 1000
EARTH_MOMENT = pm.moment_for_circle(EARTH_MASS, 0, EARTH_RADIUS)
GROUND_Y = res_y/20
G = 6.67408*10**-11


def keyDown(e, key):
    return e.type == pg.KEYDOWN and e.key == key


def keyUp(e, key):
    return e.type == pg.KEYUP and e.key == key


def updateGravity(space, rocket, objectShapes, objectBodies):
    space.gravity = phy.netGravity(objectBodies, objectShapes, rocket)
    space.gravity[0] = space.gravity[0]/rocket.mass
    space.gravity[1] = space.gravity[1]/rocket.mass


def updateCamera(screen, game, center, space, draw_options):
    x, y = screen.get_size()
    c_x, c_y = pygame_util.to_pygame(center, game)
    dest = max(c_x - x // 2, 0), max(c_y - y // 2, 0)
    print((x, y), (c_x, c_y), dest)
    screen.fill((0, 0, 0))
    game.blit(screen, dest)
    space.debug_draw(draw_options)
    screen.blit(game, (0, 0), pg.Rect(dest[0], dest[1], x, y))


def run():
    #pg.init()
    #screen = pg.display.set_mode((res_x, res_y), pg.RESIZABLE)
    celestialBodies = []
    celestialShapes = []
    screen = pg.display.get_surface()
    clock = pg.time.Clock()

    game = pg.Surface((10000, 10000))

    space = pm.Space()
    headsUp = hud.headsUpDisplay()

    #bodies exerting G force


    earthBody = pm.Body(body_type=pm.Body.STATIC)
    earthShape = pm.Circle(earthBody,EARTH_RADIUS)
    earthShape.mass = 10**13
    earthBody.position = 5000, 5000
    space.add(earthBody, earthShape)
    celestialBodies.append(earthBody)
    celestialShapes.append(earthShape)

    planetGageBody = pm.Body(body_type=pm.Body.STATIC)
    planetGageShape = pm.Circle(planetGageBody, 200)
    planetGageShape.mass = 10**13
    planetGageBody.position = 1000, 1000
    space.add(planetGageBody, planetGageShape)
    celestialBodies.append(planetGageBody)
    celestialShapes.append(planetGageShape)

    rocket = tr.genRocket(space)
    x, y = earthBody.position[0] + EARTH_RADIUS*math.sin(math.pi/4), earthBody.position[1] + EARTH_RADIUS*math.sin(math.pi/4)
    rocket.position = x, y
    draw_options = pygame_util.DrawOptions(game)
    space.gravity = 0, 0
    space.damping = 0.9

    fire_ticks = 480*50
    fire = False
    rotate = False
    auto = False
    sas_angle = 0
    print(rocket.position)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT or keyDown(event, pg.K_ESCAPE):
                pg.quit()
                sys.exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_a or event.key == pg.K_d:
                    rotKey = event.key
                    rotate = True
                elif event.key == pg.K_f:
                    fireKey = event.key
                    fire = True

            elif event.type == pg.KEYUP:
                if event.key == pg.K_a or event.key == pg.K_d:
                    rotate = False
                elif event.key == pg.K_f:
                    fire = False
                elif event.key == pg.K_v:
                    sas_angle = rocket.angle
                    auto = not auto

            elif event.type == pg.VIDEORESIZE:
                screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)

        if fire:
            fire_ticks -= 1
            rocket.thrust(fireKey)
        if rotate:
            rocket.turn_SAS(rotKey, 1)
        if auto:
            rocket.auto_SAS(sas_angle)

        print(rocket.position)
        updateGravity(space, rocket, celestialShapes, celestialBodies)
        space.step(1/50.0)
        updateCamera(screen, game, rocket.position, space, draw_options)
        headsUp.updateHUD(rocket.position[0], rocket.position[1], math.sqrt(rocket.velocity[0]**2 + rocket.velocity[1]**2),math.atan2(rocket.velocity[1], rocket.velocity[0])*180/math.pi,math.sqrt(space.gravity[0]**2+space.gravity[1]**2),math.atan2(space.gravity[1], space.gravity[0])*180/math.pi)
        pg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run()
