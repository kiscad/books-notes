from dataclasses import dataclass, field

from .imesh import IMesh
from .ipart import IPart
from .mesh_stub import MeshStub


@dataclass
class Wheel(IPart):
    mesh: IMesh = field(default_factory=MeshStub.make_sphere)

    def get_name(self):
        return "Part: Wheel"
