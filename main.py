from ursina import *

app = Ursina()

player_speed = 5
block_pick = 1

def update():
    player_movement = (held_keys['d'] - held_keys['a'], held_keys['e'] - held_keys['q'], held_keys['w'] - held_keys['s'])
    player.y += player_movement[1] * player_speed * time.dt
    player.x += player_movement[0] * player_speed * time.dt
    player.z += player_movement[2] * player_speed * time.dt

    if player.y < 0.5:
        player.y = 0.5

    if held_keys['shift']:
        player.y -= 0.5

class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture='white_cube', color=color.white):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=0.5,
            texture=texture,
            color=color,
            highlight_color=color.lime,
            scale=1.0
        )

    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position=self.position + mouse.normal, texture=block_pick)
            elif key == 'left mouse down':
                destroy(self)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x, 0, z), texture='grass_block')

player = FirstPersonController()

app.run()
