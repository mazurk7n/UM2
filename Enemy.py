import Object
class Enemy(Object.Object):
    def __init__(self, x, y, width, height, canvas):
        super().__init__(x, y, width, height, "green", canvas)