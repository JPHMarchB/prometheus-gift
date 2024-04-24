import pygame
import time
import random


pygame.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Prometheus' Gift")

BG = pygame.transform.scale(pygame.image.load("./game_assets/bg_test.jpg"), (WIDTH, HEIGHT))
FONT = pygame.font.Font(None, 30)

# Text box variables
BOX_HEIGHT = 250

def draw(text_box, user_text):
    WIN.blit(BG, (0, 0))

    pygame.draw.rect(WIN, "white", text_box)

    text_surface = FONT.render(user_text, True, "red")
    WIN.blit(text_surface, (20, HEIGHT - 200))

    pygame.display.update()

def main():
    run = True
    text_box = pygame.Rect(0, HEIGHT - BOX_HEIGHT, WIDTH, BOX_HEIGHT)
    clock = pygame.time.Clock()
    user_text = ''
    lost = False

    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Check if the user pressed Enter to clear the text
                    user_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    # Check if the user pressed Backspace to delete the last character
                    user_text = user_text[:-1]
                else:
                    # Append the typed character to the user_text
                    user_text += event.unicode
                    

        if lost:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(text_box, user_text)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
