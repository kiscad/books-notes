import logging
from typing import List

from datatype import Car, Door, HeadLight, IPart

from . import IMeshSplit


## An implementaion of MeshSplit
class SplitStub(IMeshSplit):
    def split(self, car: Car) -> List[IPart]:
        logging.info("Split Stub")
        return [Door(), HeadLight()]
