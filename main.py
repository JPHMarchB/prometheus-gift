import pygame
import time
import random

WIDTH, HEIGHT = 500, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prometheus' Gift")

BG = pygame.transform.scale(pygame.image.load("./game_assets/bg_test.jpg"), (WIDTH,HEIGHT))

def draw():
    WIN.blit(BG, (0,0))

    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()