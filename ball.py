from settings import *
import pygame
import random


class OriginBall:
    def __init__(self, radius, bounce_factor, ball_pos_x, ball_pos_y):
        
        self.radius = radius
        self.bounce_factor = bounce_factor

        self.ball_pos_y = ball_pos_y
        self.ball_pos_x = ball_pos_x

        self.ball_velocity_y = 0

        # Self limits
        self.ground_y = WINDOW_HEIGHT - radius

    def update(self, own_gravity, own_dt):

        # Personal Physics (Y)
        self.ball_velocity_y += own_gravity * own_dt
        self.ball_pos_y += self.ball_velocity_y

        # Personal Ground collision (Y)
        if self.ball_pos_y > self.ground_y:
            self.ball_pos_y = self.ground_y
            self.ball_velocity_y = -self.ball_velocity_y * self.bounce_factor

    def draw(self, surface, color=(255, 255, 255)):
        
        pygame.draw.circle(surface, color,
                           (int(self.ball_pos_x), int(self.ball_pos_y)), self.radius)


class SmallBall(OriginBall):
    def __init__(self, radius, bounce_factor, ball_pos_x, ball_pos_y, horizontal_force, vertical_force):
        super().__init__(radius, bounce_factor, ball_pos_x, ball_pos_y)

        self.horizontal_force = horizontal_force
        self.vertical_force = vertical_force

        self.ball_pos_x = ball_pos_x
        self.ball_velocity_x = 0

        # Self limits
        self.left_limit = radius
        self.right_limit = WINDOW_WIDTH - radius

        # Horizontal Boost
        self.boost_active = True
        self.direction = random.choice([-1, 1])

    def update(self, own_gravity, own_dt):

        # Personal Physics (Y) & Personal Ground collision (Y) from Ball
        super().update(own_gravity, own_dt)

        # Personal Physics (X)
        self.ball_pos_x += self.ball_velocity_x * own_dt
        self.ball_velocity_x *= HORIZONTAL_FRICTION

        # Horizontal and Vertical Boost
        if self.boost_active:
            self.ball_velocity_x += self.direction * self.horizontal_force
            self.ball_velocity_y += self.direction * self.vertical_force
            self.boost_active = False

        if self.ball_pos_x < self.left_limit:
            self.ball_pos_x = self.left_limit
            self.ball_velocity_x = -self.ball_velocity_x * self.bounce_factor
        if self.ball_pos_x > self.right_limit:
            self.ball_pos_x = self.right_limit
            self.ball_velocity_x = -self.ball_velocity_x * self.bounce_factor
