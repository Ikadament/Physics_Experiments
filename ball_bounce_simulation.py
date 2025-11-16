from settings import *
import pygame
import time

pygame.init()

# [Window Parameters]
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ball Simulation")
font = pygame.font.SysFont(None, 24)

# [Physics Parameters]
bounce_force = 0.85  # Absolutely needs to be < 1 in order to reduce bounce over time
horizontal_speed = 200.0
horizontal_friction = 0.9

# [Ball State]
ball_pos_x = WINDOW_WIDTH // 2
ball_pos_y = 50
ball_velocity_x = 0
ball_velocity_y = 0

ball_radius = 20

# [Limits]
ground_y = WINDOW_HEIGHT - ball_radius
left_limit = ball_radius
right_limit = WINDOW_WIDTH - ball_radius


def reset_bounce_simulation():
    global ball_pos_x, ball_pos_y, ball_velocity_x, ball_velocity_y
    ball_pos_x = WINDOW_WIDTH // 2
    ball_pos_y = 50
    ball_velocity_x = 0
    ball_velocity_y = 0


def render_text(label, value):
    return font.render(f"{label}: {value:.2f}", True, (255, 255, 255))


def ball_bounce_simulation():

    global ball_velocity_x, ball_velocity_y, ball_pos_y, ball_pos_x
    program_running = True

    while program_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program_running = False

        # Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ball_velocity_x -= horizontal_speed * DELTA_TIME
        if keys[pygame.K_RIGHT]:
            ball_velocity_x += horizontal_speed * DELTA_TIME
        if keys[pygame.K_r]:
            reset_bounce_simulation()

        # Physics (Y)
        ball_velocity_y += GRAVITY * DELTA_TIME
        ball_pos_y += ball_velocity_y

        # Ground collision (Y)
        if ball_pos_y > ground_y:
            ball_pos_y = ground_y
            ball_velocity_y = -ball_velocity_y * bounce_force

        # Physics (X)
        ball_pos_x += ball_velocity_x
        ball_velocity_x *= horizontal_friction

        # Wall collision (X)
        if ball_pos_x < left_limit:
            ball_pos_x = left_limit
            ball_velocity_x = -ball_velocity_x * bounce_force
        if ball_pos_x > right_limit:
            ball_pos_x = right_limit
            ball_velocity_x = -ball_velocity_x * bounce_force

        # Drawing
        window.fill((0, 0, 0))
        pygame.draw.circle(window, (255, 255, 255), (int(ball_pos_x), int(ball_pos_y)), ball_radius)

        debug_text_velocity_y = render_text("Velocity Y", ball_velocity_y)
        debug_text_velocity_x = render_text("Velocity X", ball_velocity_x)
        debug_text_pos_y = render_text("Pos Y", ball_pos_y)
        debug_text_pos_x = render_text("Pos X", ball_pos_x)

        window.blit(debug_text_velocity_y, (10, 10))
        window.blit(debug_text_pos_y, (10, 30))
        window.blit(debug_text_velocity_x, (10, 60))
        window.blit(debug_text_pos_x, (10, 80))

        pygame.display.update()
        time.sleep(DELTA_TIME)


if __name__ == '__main__':
    ball_bounce_simulation()
