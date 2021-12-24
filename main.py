import pygame
import sys

WINDOW_SIZE = WIDTH, HEIGHT = 800, 400

BALL_SPEED = 10
player_pos_x, player_pos_y = 0, 100
computer_pos_x, computer_pos_y = WIDTH - 15, 100
ball_pos_x, ball_pos_y = 0, (HEIGHT / 2)

class Character:

    def __init__(self, image_path,  pos_x, pos_y, width, height):
        self.image_or = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image_or, (width, height))
        self.rect = self.image.get_rect(topleft = (pos_x, pos_y))


class Player(Character):
    
    def __init__(self, image_path = '',  pos_x = 0, pos_y = 0, width = 0, height = 0):
        super().__init__(image_path, pos_x, pos_y, width, height)

class Ball(Character):

     def __init__(self, image_path = '',  pos_x = 0, pos_y = 0, width = 0, height = 0):
        super().__init__(image_path, pos_x, pos_y, width, height)

def main():

    global player_pos_x, player_pos_y , computer_pos_x, computer_pos_y, ball_pos_x, ball_pos_y
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong Pong")
    clock = pygame.time.Clock()

    player = Player(image_path = "sprites/paddle.png", pos_x = player_pos_x, pos_y = player_pos_y, width = 15, height = 60)
    computer = Player(image_path = "sprites/computer.png", pos_x = computer_pos_x, pos_y = computer_pos_y, width = 15, height = 60)
    ball = Ball(image_path = "sprites/ball.png", pos_x = computer_pos_x, pos_y = computer_pos_y, width = 20, height = 20)

    ball_speed_x, ball_speed_y = 5, 7
    player_score = 0
    computer_score = 0
    
    is_playing = True

    while is_playing:
        
        screen.fill((255, 255, 255))
        pygame.draw.line(screen, (0,0,0), (WIDTH / 2, 0), (WIDTH /2, HEIGHT))
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            if player_pos_y > 0:
                player_pos_y -= 10

        if keys[pygame.K_DOWN]:
            if player_pos_y < (HEIGHT - player.image.get_height()):
                player_pos_y += 10
        
        ball_pos_x += ball_speed_x
        ball_pos_y += ball_speed_y

        if ball_pos_x <= 0 or ball_pos_x >= WIDTH:
            ball_speed_x *= -1
        if ball_pos_y <= 0 or ball_pos_y >= HEIGHT:
            ball_speed_y *= -1
        if ball_pos_x <= 0:
            computer_score += 1
        score_font = pygame.font.Font(None, 40)
        score_text = score_font.render(f'Player: {player_score}    Computer: {computer_score}', True, (0,0,0), (255,255,255))
        score_rect = score_text.get_rect()
        score_rect.center = ((WIDTH // 2) + 20, 20)
        screen.blit(score_text, score_rect)

        if ball_pos_x >= WIDTH:
            player_score += 1
        player.rect.top = player_pos_y
        computer.rect.top = (computer_pos_y + computer.image.get_height() + ball.image.get_height())

        ball.rect.left = ball_pos_x
        ball.rect.top = ball_pos_y
        computer_pos_y += ball_speed_y

        if ball.rect.colliderect(player.rect):
            ball_speed_x *= -1

        if ball.rect.colliderect(computer.rect):
            ball_speed_x *= -1
        
        screen.blit(player.image, (player_pos_x, player_pos_y))
        ball.rect.left = player_pos_x
        ball.rect.top = player_pos_y
        
        screen.blit(computer.image, (computer_pos_x, (computer_pos_y+computer.image.get_height()+ball.image.get_height())))
        screen.blit(ball.image, (ball_pos_x, ball_pos_y))
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
