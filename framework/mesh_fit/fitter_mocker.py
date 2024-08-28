from . import IMeshFit
from datatype import IPart, Door


## An implementation of MeshFit
class MeshFitter(IMeshFit):
  def fit(self, srcMesh: IPart, tgtMesh: IPart) -> IPart:
    print("calling 'fit' from fitter")
    return Door()
