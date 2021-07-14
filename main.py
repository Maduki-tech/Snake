# Created By David
#
# Snake In Python
#
# 13. Jul. 2021

import pygame
import HeadClass

pygame.init()  # Init Pygame
WIDTH, HEIGHT = 600, 600  # Canvas Size
FPS = 5
key_pressed = None


def refresh_screen(window):
    window.fill((0, 0, 0))


def main(key):
    game_over = False
    clock = pygame.time.Clock()
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    head = HeadClass.Head(WIN, (255, 0, 0), WIDTH / 2, HEIGHT / 2, 15, 15)

    while not game_over:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    return
                key = event.key

                # Getting the Key for the Movement of the Snake

        refresh_screen(WIN)
        head.movement(key)
        head.draw()
        pygame.display.update()


if __name__ == '__main__':
    main(key_pressed)
