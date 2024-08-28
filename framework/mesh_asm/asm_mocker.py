from . import IMeshAsm
from datatype import SedanAsm, IPart
from typing import List


## An implementation of MeshAsm
class MeshAsm(IMeshAsm):
  def assemble(self, parts: List[IPart]) -> SedanAsm:
    print("calling 'assemble' from assembler")
    return SedanAsm()
