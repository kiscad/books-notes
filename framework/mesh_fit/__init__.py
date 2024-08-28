from datatype import IPart


## Interface of mesh fitting function-module
class IMeshFit:
  def fit(self, srcMesh: IPart, tgtMesh: IPart) -> IPart:
    raise NotImplementedError
