import pygame
import os
_ASSETS_PATH = ""
if os.path.exists(os.path.abspath("assets")):
    _ASSETS_PATH = os.path.abspath("assets")
elif os.path.exists(os.path.abspath("../assets")):
    _ASSETS_PATH = os.path.abspath("../assets")
from .video import Video
Video.init()
from .graphics import Graphics
from .zoom import Zoom
from .drawer import Drawer
from .hud import HUD
from .menu import Menu
from .trajectory import Trajectory
from .explosion import Explosion

__all__ = ["_ASSETS_PATH", "Graphics", "Zoom", "Drawer", "HUD", "Menu", "Trajectory", "Explosion"]
