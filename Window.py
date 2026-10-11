import tkinter as tk
class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Game Window")
        self.root.configure(background="white")
        self.root.geometry("600x600+50+50")
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()

    def run(self):
        self.root.mainloop()
        self.root.focus_set() 
