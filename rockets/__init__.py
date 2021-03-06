import os
_ASSETS_PATH = ""
if os.path.exists(os.path.abspath("assets")):
    _ASSETS_PATH = os.path.abspath("assets")
elif os.path.exists(os.path.abspath("../assets")):
    _ASSETS_PATH = os.path.abspath("../assets")

from .component import Component
from .sas import SAS, AdvancedSAS
from .tank import Tank, TestTank
from .thruster import *
from .commandmodule import CommandModule
from .rocket import Rocket
from . import testrocket

__all__ = ["_ASSETS_PATH", "Component", "SAS", "AdvancedSAS", "Tank", "TestTank", "CommandModule", "Thruster", "DeltaVee", "UpGoer2000", "SandSquid", "RCSThruster", "RightRCS", "LeftRCS", "Rocket", "testrocket"]


