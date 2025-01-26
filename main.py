import pygame
import time

pygame.init()

window = pygame.display.set_mode((960, 540))

running = True
while running:
    print("tick start")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("QUIT event received, leaving game loop...")
            running = False

    print("tick end")
    time.sleep(1)

print("Cleaning up...")
pygame.quit()
print("Done, bye!")
