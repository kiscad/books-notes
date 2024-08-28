from typing import List

from datatype import CarAsm, IPart


## Interface of mesh assembly module
class IMeshAsm:
    def assemble(self, parts: List[IPart]) -> CarAsm:
        raise NotImplementedError()
