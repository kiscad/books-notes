import logging

from PIL.Image import Image

from datatype import Car

from . import IMeshGen


## An implementation of MeshGen
class GenStub(IMeshGen):
    def generate(self, image: Image) -> Car:
        logging.info("GenStub")
        return Car()
