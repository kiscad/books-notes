from PIL.Image import Image

from datatype import CarAsm


## Interface for base shape generation
class IMeshMatch:
    def match_mesh_with_image(self, car: Image) -> CarAsm:
        raise NotImplementedError()
