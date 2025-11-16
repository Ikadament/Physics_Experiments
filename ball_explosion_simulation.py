from ball import *
import pygame
import time
import random

pygame.init()

# [Global Simulation Parameters]
ball_radius_max = 20

# [Window Parameters]
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ball Explosion Simulation")

# [Instantiation Parameters]
radius_min = 5
radius_max = 20

bounce_factor_min = 0.85
bounce_factor_max = 0.90

ball_pos_x_min = 250
ball_pos_x_max = 350
ball_pos_y_min = WINDOW_HEIGHT - 20
ball_pos_y_max = WINDOW_HEIGHT

horizontal_force_min = 200
horizontal_force_max = 500

vertical_force_min = 5
vertical_force_max = 10

small_ball_min = 5
small_ball_max = 25

small_balls = []
origin_ball = OriginBall(20, 0.85, 300, 50)


def reset_explosion_simulation():
    global small_balls, origin_ball
    small_balls = []
    origin_ball = OriginBall(20, 0.85, 300, 50)
    instantiate_small_ball(random.randint(small_ball_min,small_ball_max))


def instantiate_small_ball(nb_ball):
    for i in range(nb_ball):
        small_balls.append(
            SmallBall(random.randint(radius_min, radius_max), random.uniform(bounce_factor_min, bounce_factor_max),
                      random.randint(ball_pos_x_min, ball_pos_x_max), random.randint(ball_pos_y_min, ball_pos_y_max),
                      random.randint(horizontal_force_min, horizontal_force_max),
                      random.randint(vertical_force_min, vertical_force_max)))


def ball_explosion_simulation():

    global origin_ball
    program_running = True

    while program_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program_running = False

        # Reset
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            reset_explosion_simulation()

        # Origin Ball Physics (Y)
        if origin_ball is not None:
            if origin_ball.ball_pos_y < origin_ball.ground_y:
                origin_ball.update(GRAVITY, DELTA_TIME)
            else:
                origin_ball = None

        # Small Balls Physics
        if origin_ball is None:
            for ball in small_balls:
                ball.update(GRAVITY, DELTA_TIME)

        # Drawing
        window.fill((0, 0, 0))

        if origin_ball is not None:
            origin_ball.draw(window)

        if origin_ball is None:
            for ball in small_balls:
                ball.draw(window)

        pygame.display.update()
        time.sleep(DELTA_TIME)


if __name__ == "__main__":
    reset_explosion_simulation()
    ball_explosion_simulation()
