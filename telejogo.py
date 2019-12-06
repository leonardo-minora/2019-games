import pygame

def processamento_de_entrada_e_contina_jogo(players, velocity, delta):
    # Captura os eventos (mouse, teclado, etc)
    event = pygame.event.poll()
    player_right = players[1]
    player_left = players[0]

    ## verfifica se o evento foi finalizar o app
    if event.type == pygame.QUIT:
        return False
    elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
        player_right.move_ip(0, -(velocity * delta))
    elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
        player_right.move_ip(0, velocity * delta)
    elif event.type == pygame.KEYUP and event.key == pygame.K_a:
        player_left.move_ip(0, -(velocity * delta))
    elif event.type == pygame.KEYUP and event.key == pygame.K_z:
        player_left.move_ip(0, velocity * delta)
    return True

def atualizacao_do_jogo(screen, ball, players, velocity, delta):
    # move a bola
    ## https://www.pygame.org/docs/ref/rect.html#pygame.Rect.move_ip
    ## move o retângulo incrementando as coordenadas x, y
    ## valores x, y podem ser negativos
    ball.move_ip(velocity * delta, 0)
    screen_rect = screen.get_rect()
    if ball.collidelist(players) >= 0:
        return -velocity
    if not screen_rect.contains(ball):
        if ball.right > screen_rect.right:
            ball.move_ip(-320,0)
            return -velocity
        if ball.left < screen_rect.left:
            ball.move_ip(320,0)
            return -velocity
    return velocity

def mostrar(screen, ball, players):
    # desenha o fundo
    screen.fill(BLACK)
    # desenha a bola
    pygame.draw.rect(screen, WHITE, bola)
    # desenha os jogadores
    for jogador in jogadores:
        pygame.draw.rect(screen, WHITE, jogador)
    # mostra o desenho na tela
    pygame.display.flip()

# Tamanhos
DIMENSAO_TELA = (640, 480)

# Cores
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

pygame.init()

screen = pygame.display.set_mode(DIMENSAO_TELA)
screen_rect = screen.get_rect()
clock = pygame.time.Clock()

pygame.display.set_caption('Telejogo')

# bola
## https://www.pygame.org/docs/ref/rect.html
## x, y, largura, altura
bola = pygame.Rect(300, 230, 20, 20)
velocidade_da_bola = 0.2

# jogadores
jogador_esquerda = pygame.Rect(20, 210, 20, 60)
jogador_direita = pygame.Rect(600, 210, 20, 60)
jogadores = [jogador_esquerda, jogador_direita]
velocidade_do_jogador = 0.3

while True:
    dt = clock.tick(30)

    if not processamento_de_entrada_e_contina_jogo(jogadores, velocidade_do_jogador, dt):
        break
    velocidade_da_bola = atualizacao_do_jogo(screen, bola, jogadores, velocidade_da_bola, dt)
    mostrar(screen, bola, jogadores)