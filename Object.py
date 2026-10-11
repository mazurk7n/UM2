import tkinter as tk
class Object:
    def __init__(self, x, y, width, height, color, canvas, image, image_scale):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.canvas = canvas
        self.image = tk.PhotoImage(file=image).subsample(image_scale, image_scale) if image else None
    def draw(self):
            if self.image:
                self.rect = self.canvas.create_image(self.x, self.y, anchor=tk.NW, image=self.image)
            else:
                self.rect = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)