import logging

from PIL.Image import Image

from datatype import Car, CarAsm

from . import IMeshMatch


## An Implementation of IMeshMatch
class MatchStub(IMeshMatch):
    def match_mesh_with_image(self, car: Image) -> CarAsm:
        logging.info("Match Stub")
        return CarAsm()
