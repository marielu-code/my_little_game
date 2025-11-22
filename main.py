import pygame

WIDTH, HEIGHT = 800, 600
FPS = 60
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('my little game')
CLOCK = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    SCREEN.fill((50, 50, 50))
    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()