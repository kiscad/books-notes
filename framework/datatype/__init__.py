import logging

from .car import Car
from .car_asm import CarAsm
from .door import Door
from .headlight import HeadLight
from .imesh import IMesh
from .ipart import IPart
from .mesh_stub import MeshStub
from .rearlight import RearLight
from .sideview_mirror import SideviewMirror
from .wheel import Wheel
from .windshield import WindShield

# Configure logging to write to a file, including the time, level, and message
logging.basicConfig(
    filename="app.log",
    filemode="w",
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s] %(message)s",
)
