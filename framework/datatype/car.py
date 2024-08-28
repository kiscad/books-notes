from dataclasses import dataclass, field
from trimesh.primitives import Sphere
from trimesh import Geometry
from .ipart import IPart


@dataclass
class Car(IPart):
  mesh: Geometry = field(default_factory=Sphere)

  def display(self):
    print("display: Car")
