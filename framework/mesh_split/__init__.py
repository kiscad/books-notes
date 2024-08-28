from typing import List

from datatype import Car, IPart


## The interface for mesh split function-module
class IMeshSplit:
    # Split an integrated car model into a list of mesh models by parts
    def split(self, car: Car) -> List[IPart]:
        raise NotImplementedError()
