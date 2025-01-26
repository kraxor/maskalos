import pygame
import time

pygame.init()

screen_dimensions = (960, 540)
window = pygame.display.set_mode(screen_dimensions)

player = pygame.Rect(screen_dimensions[0] / 2, screen_dimensions[1] / 2, 10, 10)
player_color = pygame.Color(255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("QUIT event received, leaving game loop...")
            running = False

    pygame.draw.rect(window, player_color, player)
    pygame.display.flip()

print("Cleaning up...")
pygame.quit()
print("Done, bye!")
