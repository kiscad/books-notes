import logging

from datatype import Door, IPart

from . import IMeshFit


## An implementation of MeshFit
class FitStub(IMeshFit):
    def fit(self, srcMesh: IPart, tgtMesh: IPart) -> IPart:
        logging.info("FitStub")
        return Door()
