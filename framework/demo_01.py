# from mesh_gen.mesh_gen import MeshGen
from PIL.Image import Image

from mesh_asm.asm_stub import AsmStub
from mesh_fit.fit_stub import FitStub
from mesh_gen.gen_stub import GenStub
from mesh_match.match_stub import MatchStub
from mesh_split.split_stub import SplitStub

if __name__ == "__main__":
    # get the car image from user
    image = Image()

    # generate a car mesh from AI model
    gen_model = GenStub()
    car = gen_model.generate(image)

    # match the car in template-shape database
    tmpl_matcher = MatchStub()
    car_tmpl = tmpl_matcher.match_mesh_with_image(image)

    # split the generated car
    splitter = SplitStub()
    parts = splitter.split(car)

    # fit all parts
    fitter = FitStub()
    parts = [
        fitter.fit(src_part, tgt_part) for src_part, tgt_part in zip(parts, car_tmpl.list_parts())
    ]

    # assemble all parts into a car
    assembler = AsmStub()
    final_car = assembler.assemble(parts)
