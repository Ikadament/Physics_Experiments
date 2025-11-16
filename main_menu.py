from settings import *
import pygame
import pygame_gui
from ball_bounce_simulation import reset_bounce_simulation, ball_bounce_simulation
from ball_explosion_simulation import reset_explosion_simulation, ball_explosion_simulation

pygame.init()

# [Window Parameters]
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT), 'main_theme.json')

# [Global Simulation Parameters]
clock = pygame.time.Clock()

# [UI Parameters]
button_bounce = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(200, 140, 200, 50),
                                             text="Bounce Simulation", manager=manager)
button_explosion = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(200, 210, 200, 50),
                                                text="Explosion Simulation", manager=manager)


def main_menu():

    program_running = True

    while program_running:
        delta_time = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_bounce:
                    reset_bounce_simulation()
                    ball_bounce_simulation()

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_explosion:
                    reset_explosion_simulation()
                    ball_explosion_simulation()

            manager.process_events(event)

        manager.update(delta_time)

        window.fill((0, 0, 0))
        manager.draw_ui(window)

        pygame.display.flip()


if __name__ == '__main__':
    main_menu()
