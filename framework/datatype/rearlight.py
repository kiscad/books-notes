from dataclasses import dataclass, field
from trimesh import Geometry
from trimesh.primitives import Sphere
from .ipart import IPart


@dataclass
class RearLight(IPart):
  mesh: Geometry = field(default_factory=Sphere)

  def display(self):
    print("display: rear light")
