import pymunk
from pymunk.vec2d import Vec2d


collision_debug_mode = False

# Maximum post-collision force a component can withstand without being destroyed
_threshold_for_failure = 100000 # kg*m/s^2


# Collision Types
CT_COMPONENT = 2
CT_CELESTIAL_BODY = 1


# Collision Post-Solver: Component, Celestial Body
def post_solve_component_celestialbody(arbiter, space, data):
    """
    Determines what happens when two objects collide.

    :param arbiter: The :py:class:`pymunk.Body whose stats decide if a :py:class:`Component` will break.
    :type arbiter: :py:class:`pymunk.Body`
    """
    component = None
    for shape in arbiter.shapes:
        if shape.collision_type == CT_COMPONENT:
            component = shape
    if component is not None and arbiter.total_impulse.length/50 > _threshold_for_failure:
        component.body.destroyed = True
    return True
