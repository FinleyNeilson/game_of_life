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

game_active = True

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()

score_surface = test_font.render('My game', False, 'black')
score_rect = score_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (500, ground_y_pos))

player_sur = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_sur.get_rect(midbottom = (200, ground_y_pos))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if game_active == False:
                game_active = True
                snail_rect.x -= 350
            elif event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                player_gravity = -20

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, ground_y_pos))
        screen.blit(score_surface, score_rect)

        screen.blit(snail_surface, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_sur, player_rect)

        snail_rect.x -= 7
        if snail_rect.right < 0 : snail_rect.left = screen_width
 
        if player_rect.colliderect(snail_rect):
            game_active = False
    else:
        screen.fill('Red')

    pygame.display.update()
    clock.tick(60)
