import pygame

pygame.init()

# game settings
speed = 2
player_color = pygame.Color(255, 0, 0)
npc_color = pygame.Color(0, 0, 255)
text_color = pygame.Color(230, 230, 230)
screen_dimensions = (960, 540)
frame_rate = 60 # FPS (frames per second)
character_width = 40
character_height = 40
interact_distance = 70

# load fonts
font = pygame.font.Font("CollegeBlock.ttf", size=32)

# create screen
window_surface = pygame.display.set_mode(screen_dimensions)

# create clock
clock = pygame.time.Clock()

# set player starting coordinates
player_x = screen_dimensions[0] / 2
player_y = screen_dimensions[1] / 2

# set NPC starting coordinates
npc_x = 200
npc_y = 200

running = True
is_interacting = False
text_rect=None
flag=False
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("QUIT event received, leaving game loop...")
            running = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_e:
                distance_x = abs(player_x - npc_x)
                distance_y = abs(player_y - npc_y)
                if distance_x <= interact_distance and distance_y <= interact_distance:
                    if is_interacting:
                        is_interacting = False
                    else:
                        is_interacting = True
                else:
                    print("too far away, can not interact")
                    print("distance = (%f, %f)" % (distance_x, distance_y))

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

    # create rects for characters
    player_rect = pygame.Rect(player_x, player_y, character_width, character_height)
    npc_rect = pygame.Rect(npc_x, npc_y, character_width, character_height)

    ''' 
        Keep track of distance between the player and npc in real time will make it easy to find when the playe is near
        and when far away
    '''
    distance_x = abs(player_rect.x - npc_rect.x)
    distance_y = abs(player_rect.y - npc_rect.y)

    # clear screen
    window_surface.fill(pygame.Color(0, 0, 0))

    # draw character rects
    pygame.draw.rect(window_surface, player_color, player_rect)
    pygame.draw.rect(window_surface, npc_color, npc_rect)


    '''
        Instead of just checking for if interacting we can also use the real time distance we calculated to find whether 
        actor/player is within interaction range or not.
    '''
    if is_interacting and distance_x <= interact_distance and distance_x <= interact_distance:
        text_offset_x = npc_x - 50
        text_offset_y = npc_y - 100
        # draw text
        text_surface = font.render("Mountains are nice!", 0, text_color)
        window_surface.blit(text_surface, (text_offset_x, text_offset_y))

        # draw bubble around the text
        text_rect = text_surface.get_rect()
        horizontal_padding = 20
        text_rect.width += horizontal_padding
        text_rect.x = text_offset_x - int(horizontal_padding / 2)
        text_rect.y = text_offset_y

        pygame.draw.rect(window_surface, text_color, text_rect, 2, 20)

    
    else:
        '''
            If the actor/player is not in range we just set interacting to false which previously only happended
            when thr key 'e' was clicked and then we just replace the bubble with solid black
        '''
        
        if is_interacting and distance_x > interact_distance and distance_y > interact_distance:
            window_surface.blit(pygame.Color(0, 0, 0), text_rect)
        is_interacting=False

    # flip display (apply changes)
    pygame.display.flip()

    # sleep until next frame
    clock.tick(frame_rate)

print("Cleaning up...")
pygame.quit()
print("Done, bye!")
