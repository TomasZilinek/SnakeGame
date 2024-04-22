from random import randint


class Point:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.height = 20

    def draw(self, canv):
        canv.create_rectangle(self.pos_x, self.pos_y, self.pos_x + self.height, self.pos_y + self.height, fill="yellow", width=0)

    def set_coordinates(self, max_w, max_h):
        x = randint(self.height * 2, max_w - self.height * 2)
        y = randint(self.height * 2, max_h - self.height * 2)
        self.pos_x = x + self.height - x % self.height
        self.pos_y = y + self.height - y % self.height

    def erase(self, canv):
        canv.create_rectangle(self.pos_x, self.pos_y, self.pos_x + self.height, self.pos_y + self.height, fill="white", width=0)
