import pygame
from sys import exit

def main():
    pygame.init()
    set_fps = pygame.time.Clock()
    screen_name = pygame.display.set_caption('SP-ACE')
    screen = pygame.display.set_mode((600,600))

    text = pygame.font.Font(None, 50)
    text_surface = text.render("HELLO WORLD", False, (255,255,255))
    text_rect = text_surface.get_rect(center = (300,100))

    space_img = pygame.image.load('game assets/space_game.jpg').convert_alpha()
    player_img = pygame.image.load('game assets/player1.png').convert_alpha()
    player_img = pygame.transform.scale(player_img,(50,50))

    player_rect = player_img.get_rect(center = (300,300))

    enemy_img = pygame.image.load('game assets/enemy1.png').convert_alpha()
    enemy_img = pygame.transform.scale(enemy_img,(40,40))
    enemy_rect = enemy_img.get_rect(center = (150,150))

    ship_speed = 10
    rect_hits = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        set_fps.tick(60)
        screen.blit(space_img,(0,0))
        screen.blit(player_img, player_rect)
        screen.blit(enemy_img, enemy_rect)
        pygame.draw.rect(screen, 'Red', text_rect)
        pygame.draw.rect(screen, 'Red', text_rect, 10)
        pygame.draw.line(screen, 'Purple', (0,0),pygame.mouse.get_pos(), 10)
        screen.blit(text_surface, text_rect)

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_a]:
            player_rect.centerx -= ship_speed
        if pressed_key[pygame.K_d]:
            player_rect.centerx += ship_speed
        if pressed_key[pygame.K_w]:
            player_rect.centery -= ship_speed
        if pressed_key[pygame.K_s]:
            player_rect.centery += ship_speed

        if player_rect.right < 0:
            player_rect.left = 600
        elif player_rect.left > 600:
            player_rect.right = 0
        
        if player_rect.bottom < 0:
            player_rect.top = 600
        elif player_rect.top > 600:
            player_rect.bottom = 0

        player_collide = player_rect.colliderect(enemy_rect)
        if player_collide:
            rect_hits += 1
            print(f'PLAYER COLLIED WITH ENEMY {rect_hits} TIMES')

        pygame.display.update()

if __name__ == "__main__":
    main()
