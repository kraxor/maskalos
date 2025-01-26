import pygame

pygame.init()

# game settings
speed = 2
player_color = pygame.Color(255, 0, 0)
npc_color = pygame.Color(0, 0, 255)
screen_dimensions = (960, 540)
frame_rate = 60 # FPS (frames per second)
character_width = 40
character_height = 40

# create screen
window = pygame.display.set_mode(screen_dimensions)

# create clock
clock = pygame.time.Clock()

# set player starting coordinates
player_x = screen_dimensions[0] / 2
player_y = screen_dimensions[1] / 2

# set NPC starting coordinates
npc_x = 200
npc_y = 200

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
        player_y = player_y - speed
    elif keys[pygame.K_s]:
        player_y = player_y + speed
    if keys[pygame.K_a]:
        player_x = player_x - speed
    elif keys[pygame.K_d]:
        player_x = player_x + speed

    # print("player location: %f,%f" % (player_x, player_y))

    # create rects for characters
    player_rect = pygame.Rect(player_x, player_y, character_width, character_height)
    npc_rect = pygame.Rect(npc_x, npc_y, character_width, character_height)

    # clear screen
    window.fill(pygame.Color(0, 0, 0))

    # draw character rects
    pygame.draw.rect(window, player_color, player_rect)
    pygame.draw.rect(window, npc_color, npc_rect)

    # flip display (apply changes)
    pygame.display.flip()

    # sleep until next frame
    clock.tick(frame_rate)

print("Cleaning up...")
pygame.quit()
print("Done, bye!")
