# Interface of Mesh datatype
class IMesh:
    def bounding_box(self):
        raise NotImplementedError()

    def num_vertices(self):
        raise NotImplementedError()

    def num_faces(self):
        raise NotImplementedError()

    def set_vertex(self, i, v):
        raise NotImplementedError()

    def set_face(self, i, f):
        raise NotImplementedError()

    def set_uv(self, i, uv):
        raise NotImplementedError()

    def set_color(self, i, c):
        raise NotImplementedError()

    def get_vertices_ndarray(self):
        raise NotImplementedError()

    def get_faces_ndarray(self):
        raise NotImplementedError()

    def get_normals_ndarray(self):
        raise NotImplementedError()

    def get_uvs_ndarray(self):
        raise NotImplementedError()

    def get_colors_ndarray(self):
        raise NotImplementedError()

    def get_materials_ndarray(self):
        raise NotImplementedError()

    def read_obj(self, filename):
        raise NotImplementedError()

    def write_obj(self, filename):
        raise NotImplementedError()
