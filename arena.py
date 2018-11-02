from builder import Builder

class Arena:
    
    def __init__(self):
        self.builder = Builder()

    def draw_arena(self):
        self.builder.draw_arena_outline()