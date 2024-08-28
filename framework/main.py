from PIL.Image import Image
from mesh_gen.mesh_gen import MeshGen
from base_match.base_matcher import BaseMatcher
from mesh_split.mesh_splitter import MeshSplitter
from mesh_fit.mesh_fitter import MeshFitter
from mesh_asm.mesh_asm import MeshAsm

if __name__ == "__main__":
  # get the car image from user
  image = Image()

  # generate a car mesh from AI model
  gen_model = MeshGen()
  car = gen_model.generate(image)

  # match the car in base-shape database
  base_matcher = BaseMatcher()
  car_base = base_matcher.match_base(car)

  # split the generated car
  splitter = MeshSplitter()
  parts = splitter.split(car)

  # fit all parts
  fitter = MeshFitter()
  parts = [
    fitter.fit(src_part, tgt_part) for src_part, tgt_part in zip(parts, car_base.list_parts())
  ]

  # assemble all parts into a car
  assembler = MeshAsm()
  final_car = assembler.assemble(parts)
