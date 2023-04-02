from PyQt5 import Qt3DCore, Qt3DExtras, Qt3DRender

# Create a Qt3D window
view = Qt3DExtras.Qt3DWindow()
scene = view.scene()

# Create an entity to hold the mesh
entity = Qt3DCore.QEntity(scene)

# Load the mesh data from an .obj file
mesh = Qt3DRender.QMesh()
mesh.setMeshName("MyMesh")
mesh.setSource(QUrl.fromLocalFile("/home/T7725VK/Downloads/uploads_files_1017599_Jeep_Renegade_2016_obj/Jeep_Renegade_2016_obj/Jeep_Renegade_2016.obj"))

# Add the mesh to the entity
entity.addComponent(mesh)

# Add the entity to the scene
scene.addEntity(entity)

# Show the window
view.show()
