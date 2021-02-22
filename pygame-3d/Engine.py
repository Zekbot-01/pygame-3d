from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def Minecraft_copy():
    from ursina.prefabs.first_person_controller import FirstPersonController
    from ursina import mouse
    import playsound

    stone = False
    plank = True
    grass = False
    nani = False

    class Xube(Button):
        def __init__(self, colour, textur=None, model="cube", pos=(0, 0, 0)):
            super().__init__(
                parent=scene,
                position=pos,
                model=model,
                color=colour,
                origin_y=0.5,
                texture=textur)

        def input(self, key):
            if self.hovered:
                global stone, plank, grass, nani

                if held_keys["0"]:
                    grass = True
                    stone = False
                    plank = False
                    nani = False

                if held_keys["1"]:
                    stone = False
                    grass = False
                    plank = True
                    nani = False

                if held_keys["2"]:
                    stone = True
                    grass = False
                    plank = False
                    nani = False

                if held_keys["9"]:
                    stone = False
                    grass = False
                    plank = False
                    nani = True

                if key == "left mouse down":
                    if plank == True:
                        new_cube = Xube(colour=color.white, pos=self.position + mouse.normal, textur="plank.png")

                    if stone == True:
                        new_cube = Xube(colour=color.white, pos=self.position + mouse.normal, textur="stone.jpg")

                    if grass == True:
                        new_cube = Xube(colour=color.white, pos=self.position + mouse.normal, textur="dirt.jpg")

                    if nani == True:
                        new_cube = Xube(colour=color.white, pos=self.position + mouse.normal, textur="meme.jpg")

                if key == "right mouse down":
                    destroy(self)

    game = Ursina()

    def update():
        if held_keys["shift"]:
            player.speed = 8

        elif not held_keys["shift"]:
            player.speed = 5

    for z in range(30):
        for x in range(30):
            cube = Xube(pos=(x, 0, z), colour=color.white, textur="dirt.jpg")

    class Sky(Entity):
        def __init__(self):
            super().__init__(
                parent=scene,
                texture="sky.jpg",
                model="sphere",
                double_sided=True,
                scale=150)

    sky = Sky()

    player = FirstPersonController()
    player.cursor.color = color.lime
    player.jump_duration = 0.3

    game.run()