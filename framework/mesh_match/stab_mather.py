from . import ITmplMatch
from datatype import SedanAsm, Car


## An Implementation of BaseGen
class TemplMatcher(ITmplMatch):
  def match_template(self, car: Car) -> SedanAsm:
    print("calling 'generate_base' from base generator")
    return SedanAsm()
