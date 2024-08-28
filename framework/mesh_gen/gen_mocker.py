from . import IMeshGen
from datatype import Car
from PIL.Image import Image


## An implementation of MeshGen
class MeshGen(IMeshGen):
  def generate(self, image: Image) -> Car:
    print("calling 'generate' from gneerator")
    return Car()
