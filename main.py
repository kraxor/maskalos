import pygame
import time

pygame.init()

screen_dimensions = (960, 540)
window = pygame.display.set_mode(screen_dimensions)

player_x = screen_dimensions[0] / 2
player_y = screen_dimensions[1] / 2

player_color = pygame.Color(255, 0, 0)

running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("QUIT event received, leaving game loop...")
            running = False

    # handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= 0.1

    # create player rect
    player_rect = pygame.Rect(player_x, player_y, 10, 10)

    # clear screen
    window.fill(pygame.Color(0, 0, 0))

    # draw player rect
    pygame.draw.rect(window, player_color, player_rect)

    # flip display (apply changes)
    pygame.display.flip()

print("Cleaning up...")
pygame.quit()
print("Done, bye!")
