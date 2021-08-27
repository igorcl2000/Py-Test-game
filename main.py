from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

class Voxel (Button):
	def __init__(self, position = (0,0,0)):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			origin_y = .5,
			texture = 'white_cube',
			color = color.color(255,0, random.uniform(.9, 1.0)),
			highlight_color = color.lime,
		)

	def input(self, key):
		if self.hovered:
			if key == 'right mouse down':
				voxel = Voxel(position=self.position + mouse.normal)

			if key == 'left mouse down':
				destroy(self)

for z in range(16):
	for x in range(16):
		voxel = Voxel(position=(x,0,z))

player = FirstPersonController()
app.run()