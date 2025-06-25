import random, math
from consts import *

def random_moves(right_paddle, PADDLE_SPEED):
    right_paddle.y += random.choice([-1, 0, 1]) * PADDLE_SPEED

def sigmoid(x):
    return 1 / (1 + math.e ** -x)

weights = list()
for i in range(9):
    weights.append(random.uniform(-0.1, 0.1))

def dot(weights, inputs):
    assert len(weights) == len(inputs), "Weights and inputs must have the same length"
    return sum(w * i for w, i in zip(weights, inputs))

class Calculate:
    def __init__(self, right_paddle, right_paddle_vel, ball_pos, ball_vel, computer_paddle_pos):
        self.paddle = right_paddle
        self.paddle_vel = right_paddle_vel
        self.ball = ball_pos
        self.ball_vel = ball_vel
        self.comp_paddle_pos = computer_paddle_pos

        self.paddle_accel = 1.5
        self.max_speed = 10
        self.friction = 0.8

    def update(self, ball_pos, ball_vel, computer_paddle_pos):
        self.ball = ball_pos
        self.ball_vel = ball_vel
        self.comp_paddle_pos = computer_paddle_pos

    def inputs(self):
        return [
            self.paddle.x, 
            self.paddle.y, 
            self.paddle_vel, 
            self.ball.x, 
            self.ball.y, 
            self.ball_vel[0], 
            self.ball_vel[1],
            self.comp_paddle_pos.x, 
            self.comp_paddle_pos.y
        ]

    def expected_output(self):
        if self.ball_vel[1] > 0 and self.paddle.y <= self.ball.y: # Ball moving down
            return self.paddle_accel
        elif self.ball_vel[1] < 0 and self.paddle.y >= self.ball.y: # Ball moving up
            return -self.paddle_accel
        else:
            return 0
        '''
        if self.ball.y > self.paddle.y + self.paddle.height / 2:
            return self.paddle_accel
        elif self.ball.y < self.paddle.y + self.paddle.height / 2:
            return -self.paddle_accel
        else:
            return 0'''

    def random_moves(self):
        x = random.choice([-1, 0, 1])
        if x == 0: self.paddle_vel *= self.friction
        else: 
            prediction = (sigmoid(dot(weights, self.inputs())) - 0.5) * 2 * self.paddle_accel
            #self.paddle_vel += prediction
            self.paddle_vel += self.expected_output()

            print("Prediction:", prediction, "Expected", self.expected_output())

        if self.paddle_vel > self.max_speed:
            self.paddle_vel = self.max_speed
        if self.paddle_vel < -self.max_speed:
            self.paddle_vel = -self.max_speed

        self.paddle.y += int(self.paddle_vel)

        if self.paddle.top < 0:
            self.paddle.top = 0
            self.paddle_vel = 0
        if self.paddle.bottom > HEIGHT:
            self.paddle.bottom = HEIGHT
            self.paddle_vel = 0
