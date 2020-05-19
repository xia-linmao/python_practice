class ball:
    def __init__(self, x, y, vx, vy, r, t):
        self.directrion = (x, y)
        self.velocity_x = vx
        self.velocity_y = vy
        self.radio = r
        self.round_x = x + r
        self.round_y = y + r
        self.position_x = x
        self.position_y = y
        self.move_time = t

    def collision(self, other_ball):
        distance_x = self.position_x + self.radio + other_ball.radio
        distance_y = self.position_y + self.radio + other_ball.radio

        if distance_x >= other_ball.position_x and distance_y >= other_ball.position_y:
            return "Two balls collided"
        else:
            return "Two balls not collided"

    def move(self):
        x1 = self.position_x + self.velocity_x * self.move_time
        y1 = self.position_y + self.velocity_y * self.move_time
        final_position = (x1, y1)
        return final_position


qiu1 = ball(1, 1, 1, 1, 1, 2)
qiu2 = ball(4, 1, 1, 1, 1, 2)

print(qiu1.collision(qiu2))
print(qiu1.move())
