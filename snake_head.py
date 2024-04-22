class Head:
    def __init__(self):
        self.pos_x = 100
        self.pos_y = 100
        self.height = 20
        self.old_pos_x = 0
        self.old_pos_y = 0
        self.course = "right"
        self.real_course = "right"
        self.color = "red"

    def draw(self, canv):
        canv.create_rectangle(self.pos_x, self.pos_y, self.pos_x + self.height, self.pos_y + self.height, fill=self.color)

    def erase(self, canv):
        canv.create_rectangle(self.pos_x, self.pos_y, self.pos_x + self.height, self.pos_y + self.height, fill="white")

    def move(self, crs, real_crs):
        if crs == "up" and real_crs != "down":
            self.pos_y -= self.height
            self.real_course = "up"
        elif crs == "down" and real_crs != "up":
            self.pos_y += self.height
            self.real_course = "down"
        elif crs == "right" and real_crs != "left":
            self.pos_x += self.height
            self.real_course = "right"
        elif crs == "left" and real_crs != "right":
            self.pos_x -= self.height
            self.real_course = "left"
