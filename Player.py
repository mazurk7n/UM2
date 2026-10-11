import Object

# Unsure if player movement is good enough but its like fine

class Player(Object.Object):
    def __init__(self, x, y, width, height, canvas):
        super().__init__(x, y, width, height, "red", canvas)

        # checks ALL key inputs, only acts on registered ones
        self.canvas.bind_all("<KeyPress>", self.key_press)
        self.canvas.bind_all("<KeyRelease>", self.key_release) 

        self.movement_loop_active = False # maybe shouldnt be here

    # Speed variables, might move to config file/readjust the implementation
    BASE_MS = 10
    movement_speed = BASE_MS
    diagonal_ms = BASE_MS * 0.7071  # Adjust speed for diagonal movement
    def focus_mode(self, event=None): # Simple Touhou-style focus mode, pondering if I can add a visual indicator or hitbox toggle for aura purposes
        self.movement_speed = self.BASE_MS * 0.35 

    def focus_mode_stop(self, event=None):
        self.movement_speed = self.BASE_MS


    # Key press registry, mostly movement for now
    registered_keys = {"Left", "Right", "Up", "Down", "Shift_L"}
    horizontal_keys = {"Left", "Right"}
    vertical_keys = {"Up", "Down"}

    keys_pressed = set() # List of currently pressed keys

    # Movement loop/key press reading solution seems to handle multiple key presses

    def key_press(self, event):
        if event.keysym not in self.registered_keys:
            return  # Ignore unregistered keys
        self.keys_pressed.add(event.keysym) 
        
        if not self.movement_loop_active: # Checking whether the movement loop is already active to avoid multiple loops running simultaneously
            self.movement_loop()
        

    def key_release(self, event):
        self.keys_pressed.discard(event.keysym)
        if event.keysym == "Shift_L": # This part of the focus mode implementation might be improvable 
            self.focus_mode_stop()

    def movement_loop(self):
        self.movement_loop_active = True
        # Adjusting movement speed for diagonal movement by checking if there's an input from both horizontal and vertical keys
        if any(key in self.keys_pressed for key in self.horizontal_keys) and any(key in self.keys_pressed for key in self.vertical_keys):
            self.movement_speed = self.diagonal_ms  
        else:
            self.movement_speed = self.BASE_MS  

        if "Shift_L" in self.keys_pressed: # jak wyzej
            self.focus_mode()

        if "Left" in self.keys_pressed:
            self.move_left()
        if "Right" in self.keys_pressed:
            self.move_right()
        if "Up" in self.keys_pressed:
            self.move_up()
        if "Down" in self.keys_pressed:
            self.move_down()


        if self.keys_pressed==set(): # If no keys are pressed, stop the movement loop
            self.movement_loop_active = False
            return
        self.canvas.after(10, self.movement_loop) # Delaying the next iteration, essentially the tick rate 

    # Movement commands
    def move_left(self, event=None):
        self.canvas.move(self.rect, -self.movement_speed, 0)

    def move_right(self, event=None):
        self.canvas.move(self.rect, self.movement_speed, 0)

    def move_up(self, event=None):
        self.canvas.move(self.rect, 0, -self.movement_speed)

    def move_down(self, event=None):
        self.canvas.move(self.rect, 0, self.movement_speed)

    
