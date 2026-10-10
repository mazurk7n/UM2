import tkinter as tk
class Object:
    def __init__(self, x, y, width, height, color, canvas):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.canvas = canvas

    def draw(self):
            self.rect = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)