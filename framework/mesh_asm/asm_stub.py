import logging
from typing import List

from datatype import CarAsm, IPart

from . import IMeshAsm


## An implementation of MeshAsm
class AsmStub(IMeshAsm):
    def assemble(self, parts: List[IPart]) -> CarAsm:
        logging.info("AsmStub")
        return CarAsm()
