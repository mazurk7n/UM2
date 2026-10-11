import tkinter as tk
class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Game Window")
        self.root.configure(background="white")
        self.root.geometry("600x600+50+50")

        self.container = tk.Frame(self.root)
        self.container.pack(fill=tk.BOTH, expand=True)

        self.main_frame = tk.Frame(self.container, bg="white")
        self.menu_frame = tk.Frame(self.container, bg="yellow")
        self.game_frame = tk.Frame(self.container, bg="blue")

        for frame in (self.main_frame, self.menu_frame, self.game_frame):
            frame.grid(row=0, column=0, sticky="nsew")

        self.canvas = tk.Canvas(self.game_frame, width=600, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.main_frame_button = tk.Button(
            self.main_frame,
            text="Go to Game Frame",
            command=lambda: self.change_frame(2),
        )
        self.main_frame_button.pack(pady=0)

        self.main_frame.tkraise()

        self.frame_list = [self.main_frame, self.menu_frame, self.game_frame]



    def change_frame(self, frame_index):
        self.frame_list[frame_index].tkraise()

    def run(self):
        self.root.mainloop()
        self.root.focus_set() 

