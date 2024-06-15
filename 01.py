import pygame 
from sys import exit

pygame.init()
screen_width = 800
screen_height = 400
ground_y_pos = 300

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()

score_surface = test_font.render('My game', False, 'black')
score_rect = score_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (400, ground_y_pos))

player_sur = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_sur.get_rect(midbottom = (200, ground_y_pos))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print(str(event.pos) + "collide")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('jump')
        if event.type == pygame.KEYUP:
            print('key up')

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, ground_y_pos))

    # pygame.draw.rect(screen, 'Pink',score_rect)
    # pygame.draw.rect(screen, 'Pink',score_rect, 10)
    # pygame.draw.line(screen,'Pink',(0, screen_height),(screen_width, 0), 50)
    # pygame.draw.line(screen,'Pink',(0, 0),(screen_width, screen_height), 10)

    screen.blit(score_surface, score_rect)

    screen.blit(snail_surface, snail_rect)
    screen.blit(player_sur, player_rect)

    snail_rect.x -= 4
    if snail_rect.right < 0 : snail_rect.left = screen_width

    if player_rect.colliderect(snail_rect):
        pass

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump 2')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print("collide")

    pygame.display.update()

    clock.tick(60)
