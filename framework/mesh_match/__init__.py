from PIL.Image import Image
from datatype import CarAsm


## Interface for base shape generation
class ITmplMatch:
  def match_template(self, car: Image) -> CarAsm:
    raise NotImplementedError
