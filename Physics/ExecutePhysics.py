import pygame as pg
import pymunk as pm
import pymunk.pygame_util as pygame_util
from pymunk.vec2d import Vec2d
import sys
import TestRocket as tr

res_x, res_y = 1000, 1000
EARTH_MASS = 5.97*10**24
EARTH_RADIUS = 6371000
EARTH_MOMENT = pm.moment_for_circle(EARTH_MASS, 0, EARTH_RADIUS)
GROUND_Y = res_y/10
G = 6.67408*10**-11


def keyDown(e, key):
    return e.type == pg.KEYDOWN and e.key == key


def keyUp(e, key):
    return e.type == pg.KEYUP and e.key == key


def updateGravity(space, rocket, ground):
    r_sqrd = rocket.position[1]
    space.gravity = (0, -G*ground.mass*rocket.mass/r_sqrd)


def run():
    pg.init()
    screen = pg.display.set_mode((res_x, res_y))
    clock = pg.time.Clock()

    space = pm.Space()
    # earthBody = pm.Body(EARTH_MASS, EARTH_MOMENT, pm.Body.STATIC)
    groundLine = pm.Segment(
        space.static_body, (0, GROUND_Y), (1000, GROUND_Y), 3
    )
    space.add(groundLine)
    rocket = tr.genRocket(space, GROUND_Y)
    draw_options = pygame_util.DrawOptions(screen)

    rocket_fire_thrust = 5255000
    fire_ticks = 480*50
    fire = False
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT or keyDown(event, pg.K_ESCAPE):
                sys.exit(0)
            elif keyDown(event, pg.K_f):
                fire = True
            elif keyUp(event, pg.K_f):
                fire = False

        if fire:
            fire_ticks -= 1
            rocket.apply_force_at_local_point(
                tr.getRocketThrust(rocket, rocket_fire_thrust), Vec2d((0, 0))
            )
        updateGravity(space, rocket, groundLine)
        space.step(1/50.0)
        screen.fill((255, 255, 255))
        space.debug_draw(draw_options)
        pg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    run()
