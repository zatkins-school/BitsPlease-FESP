import pymunk as pm


class CelestialBody():
    """Wrapper class for celestial bodies, contains Body and Shape

    Args:
        name_ (String): Name of planet
        space_ (space): Space to embed planet in
        mass_ (Float): Mass of body
        radius_ (Float): Radius of circle
        position_x (Float): Center position x
        position_y (Float): Center position y
        elasticity_ (Float): Elasticity of shape
        atmosphere_ (Float): Damping coefficient for atmoshphere
        bodytype_ (Int): Type of body

    Attributes:
        mass (type): Mass of body
        name (type): Name of planet
        radius (type): Radius of circle
        posx (type): Center position x
        posy (type): Center position y
        elasticity (type): Elasticity of shape
        atmosphere (Float): Damping coefficient for atmoshphere
        bodytype (Int): Type of body
        body (Body): Body object of planet
        shape (Shape): Shape object of planet

    """
    def __init__(self, name_, space_, mass_, radius_, position_x, position_y,
                 elasticity_, atmosphere_, bodytype_):
        self.mass = mass_
        self.name = name_
        self.radius = radius_
        self.posx = position_x
        self.posy = position_y
        self.elasticity = elasticity_
        self.atmosphere = atmosphere_
        self.bodytype = bodytype_
        if self.bodytype == 0:
            self.body = pm.Body(body_type=pm.Body.STATIC)
        else:
            self.body = pm.Body(body_type=pm.Body.KINEMATIC)
        self.shape = pm.Circle(self.body, self.radius)
        self.shape.mass = self.mass
        self.shape.elasticity = self.elasticity
        self.body.position = self.posx, self.posy
        space_.add(self.body, self.shape)