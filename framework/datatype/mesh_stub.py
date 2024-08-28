import numpy as np
import trimesh
from numpy import ndarray
from trimesh import Geometry

from .imesh import IMesh


class MeshStub(IMesh):
    def __init__(self, geometry: Geometry):
        self.geometry = geometry

    def make_sphere(radius=1):
        sphere = trimesh.primitives.Sphere(radius=radius)
        return MeshStub(sphere)

    def make_cube(size=1):
        cube = trimesh.primitives.Box(box_size=[size] * 3)
        return MeshStub(cube)

    def make_cylinder(radius=1, height=2):
        cylinder = trimesh.primitives.Cylinder(radius=radius, height=height)
        return MeshStub(cylinder)

    def make_cone(radius=1, height=2):
        cone = trimesh.primitives.Cylinder(radius=radius, height=height)
        return MeshStub(cone)

    def make_torus(radius=1, thickness=0.25):
        torus = trimesh.primitives.Torus(radius=radius, thickness=thickness)
        return MeshStub(torus)

    def make_plane(size=[1, 1]):
        plane = trimesh.primitives.Plane(size=size)
        return MeshStub(plane)

    def bounding_box(self):
        return np.asarray(self.geometry.bounding_box.vertices)

    def num_vertices(self):
        return self.geometry.vertices.shape[0]

    def num_faces(self):
        return self.geometry.faces.shape[0]

    def set_vertex(self, i, v):
        # i is the index of the vertex to be modified
        # v is a numpy array with shape (3,) containing the new coordinates
        self.geometry.vertices[i] = v

    def set_face(self, i, f):
        # i is the index of the face to be modified
        # f is a numpy array with shape (3,) containing the new indexes of the vertices
        self.geometry.faces[i] = f

    def get_vertices_ndarray(self):
        return np.asarray(self.geometry.vertices)

    def get_faces_ndarray(self):
        return np.asarray(self.geometry.faces)

    def get_normals_ndarray(self):
        return np.asarray(self.geometry.face_normals)

    def read_obj(self, filename):
        geometry = trimesh.load(filename)
        return MeshStub(geometry)

    def write_obj(self, filename):
        self.geometry.export(filename)
