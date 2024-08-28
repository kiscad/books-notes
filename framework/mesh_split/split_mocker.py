from . import IMeshSplit
from datatype import IPart, Car, Door, HeadLight
from typing import List


## An implementaion of MeshSplit
class MeshSplitter(IMeshSplit):
  def split(self, car: Car) -> List[IPart]:
    print("calling 'split' from splitter")
    return [Door(), HeadLight()]
