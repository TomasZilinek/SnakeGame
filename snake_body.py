class Body:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.height = 20
        self.old_pos_x = 0
        self.old_pos_y = 0
        self.color = "blue"
        self.real_color = "blue"

    def draw(self, canv):
        canv.create_rectangle(self.pos_x, self.pos_y, self.pos_x + self.height, self.pos_y + self.height, fill=self.color)

    def erase(self, canv):
        canv.create_rectangle(self.pos_x, self.pos_y, self.pos_x + self.height, self.pos_y + self.height, fill="white")
