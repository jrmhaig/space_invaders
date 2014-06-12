import pygame

# Colours
WHITE = (255,255,255)

# Size of the screen
WIDTH = 400
HEIGHT = 300

pygame.init()
clock = pygame.time.Clock()
game_speed = 85
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0)
pygame.key.set_repeat(1, 50)

run = True

while run:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Refresh the screen
    pygame.display.update()
    clock.tick(game_speed)
