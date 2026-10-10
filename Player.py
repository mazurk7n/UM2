import tkinter as tk
import Object
class Player(Object.Object):
    def __init__(self, x, y, width, height, canvas):
        super().__init__(x, y, width, height, "red", canvas)
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)
       # self.canvas.bind_all('<KeyRelease-Left>', self.move_left_stop)
        
    movement_speed = 5

    def move_left(self, event=None):
        self.canvas.move(self.rect, -self.movement_speed, 0)

    def move_right(self, event=None):
        self.canvas.move(self.rect, self.movement_speed, 0)

    def move_up(self, event=None):
        self.canvas.move(self.rect, 0, -self.movement_speed)

    def move_down(self, event=None):
        self.canvas.move(self.rect, 0, self.movement_speed)

    

