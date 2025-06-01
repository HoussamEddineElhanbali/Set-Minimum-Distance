import bpy
import bmesh

selected_object = bpy.context.active_object
num = 10

def check_if_its_mesh():
    if selected_object.type != "MESH":
        print("please select a mesh object")
        return
    #reset transform
    bpy.ops.object.transform_apply(scale=True)

    get_vertices_and_scale_mesh(1.5) #change the minimum value that you want to be between the vertices

def get_vertices_and_scale_mesh(desired_minimum_distance):
    #create bmesh from the object
    mesh = selected_object.data
    editable_mesh = bmesh.new()
    editable_mesh.from_mesh(mesh)
    #create a list of vertices
    vertices = []
    for vertex in editable_mesh.verts:
        vertices.append(vertex.co.copy())
    #compare distances of the vertices
    minimum_distance = 0
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            distance = (vertices[i] - vertices[j]).length
            if minimum_distance == 0 or distance < minimum_distance:
                minimum_distance = distance
                print(minimum_distance)

    selected_object.scale *= desired_minimum_distance / minimum_distance

check_if_its_mesh()