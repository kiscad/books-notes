from PIL.Image import Image

from datatype import Car


## Interface of mesh generation function-module
class IMeshGen:
    def generate(self, image: Image) -> Car:
        raise NotImplementedError()
