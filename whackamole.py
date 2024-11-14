import pygame
import sys
import random

def initialize_board():
    return [["-" for i in range(640)] for j in range(512)]

pygame.init()
screen = pygame.display.set_mode((640, 512))
board = initialize_board()
screen.fill("pink")

def draw_grid():
    for i in range(1,16):
        pygame.draw.line(
            screen,
            (0,0,0),
            (0,i*32),
            (640,i*32),
            1
        )

    for i in range(1,20):
        pygame.draw.line(
            screen,
            (0, 0, 0),
            (i*32,0),
            (i*32,512),
            1
        )
draw_grid()
def main():
    try:
        pygame.init()
        x=4
        y=4
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                area = pygame.Rect(x,y,32,32)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if area.collidepoint(event.pos):
                        screen.fill("pink")
                        draw_grid()
                        row =random.randrange(1,640)
                        col =random.randrange(1,512)
                        x=(row//32)*32
                        y=(col//32)*32
                        screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))


            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
