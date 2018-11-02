class Keyboard:
    
    def __init__(self, canvas):
        # A dictionary to keep track of which keys are pressed
        self.keyboard = {
            "left": False,
            "right": False
        }
        self.canvas = canvas
    
    def register_key(self, short_key, key):
        self.canvas.bind("<KeyPress-%s>" % short_key, lambda event: self.set_key(key, True))
        self.canvas.bind("<KeyRelease-%s>" % short_key, lambda event: self.set_key(key, False))
    
    def set_key(self, key, status):
        self.keyboard[key] = status
        
    def is_pressed(self, key):
        return self.keyboard.get(key)