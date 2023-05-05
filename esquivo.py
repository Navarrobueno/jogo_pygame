import pygame
import random

# Função para detectar colisão entre o jogador e a bola
def detect_collision(player_pos, ball_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    b_x = ball_pos[0]
    b_y = ball_pos[1]

    if (b_x >= p_x and b_x < (p_x + player_size)) or (p_x >= b_x and p_x < (b_x + ball_size)):
        if (b_y >= p_y and b_y < (p_y + player_size)) or (p_y >= b_y and p_y < (b_y + ball_size)):
            return True
    return False

# Função para mostrar a pontuação na tela
def show_score(score):
    font = pygame.font.Font(None, 30)
    score_text = font.render("Pontuação: " + str(score), True, WHITE)
    screen.blit(score_text, [0, 0])

# Inicializando o Pygame
pygame.init()

# Configurações da janela do jogo
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The First Game in Pygame")

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Configurações do jogador
player_size = 50
player_pos = [SCREEN_WIDTH/2, SCREEN_HEIGHT-2*player_size]

# Configurações da bola
ball_size = 50
ball_pos = [random.randint(0, SCREEN_WIDTH-ball_size), 0]
ball_list = [ball_pos]

# Velocidade da bola
ball_speed = 2

# Pontuação do jogador
score = 0

# Configurações do relógio
clock = pygame.time.Clock()

# Loop principal do jogo
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos[0] -= player_size
            elif event.key == pygame.K_RIGHT:
                player_pos[0] += player_size

    # Atualizando a posição da bola
    for idx, ball_pos in enumerate(ball_list):
        if ball_pos[1] >= 0 and ball_pos[1] < SCREEN_HEIGHT:
            ball_pos[1] += ball_speed
        else:
            ball_list.pop(idx)
            score += 1

    # Gerando novas bolas
    if len(ball_list) < 3:
        x_pos = random.randint(0, SCREEN_WIDTH-ball_size)
        y_pos = 0
        ball_list.append([x_pos, y_pos])

    # Desenhando na tela
    screen.fill(BLACK)
    for ball_pos in ball_list:
        pygame.draw.circle(screen, RED, (ball_pos[0]+ball_size//2, ball_pos[1]+ball_size//2), ball_size//2)
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], player_size, player_size))

    # Verificando colisão com o jogador
    for ball_pos in ball_list:
        if detect_collision(player_pos, ball_pos):
            game_over = True

    # Mostrando a pontuação
    show_score(score)

    # Atualizando a tela
    pygame.display.update()