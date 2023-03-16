import pygame

pygame.init()  # Iniciando o pygame

# Janela
window = pygame.display.set_mode([1280, 720])  # Definindo tamanho da tela
title = pygame.display.set_caption('Pong')  # Titulo da Janela

score1 = 0
score1_img = pygame.image.load("assets/score/0.png")
score2 = 0
score2_img = pygame.image.load("assets/score/0.png")

win = pygame.image.load("assets/win.png")


# Carragamento da imagem do campo
field = pygame.image.load("assets/field.png")
# Player 1
player1 = pygame.image.load("assets/player1.png")  # Carragamento sprite player
player1_y = 310  # Definição da posição do jogador no eixo Y
player1_moveup = False  # Definição de loop player_moveup
player1_movedown = False  # Definição de loop player_movedown

# Player 2
player2 = pygame.image.load("assets/player2.png")
player2_y = 310  # Definição da posição do player2 no eixo y
player2_moveup = False
player2_movedown = False

# Ball
ball = pygame.image.load('assets/ball.png')  # Carregamento da bola
ball_x = 617  # Definição da bola no eixo x
ball_y = 337  # Definição da bola no eixo y
ball_dir = -3  # Definição da direção da bola
ball_dir_y = 1  # Definição da direção da bola no eixo y


def move_player():  # Função move_player
    global player1_y  # Chamada da variavel

    if player1_moveup:  # Se o player1_moveup
        player1_y -= 5  # Então o eixo Y recebera - 5 ou seja irá subir

    else:  # Caso contrário
        player1_y += 0  # O eixo Y não recebera nada

    if player1_movedown:  # Se o player1_movedown
        player1_y += 5  # Então o eixo Y recebera +5 ou seja irá descer

    else:  # Caso contrário
        player1_y -= 0  # O eixo Y não recebera nada

    if player1_y <= 0:  # Se a posição do player1_y for menor ou igual a zero
        player1_y = 0  # Ela passará a ser zero, ou seja irá ter um limite de subida na tela

    elif player1_y > 575:  # Se a posição do player1_y for maior ou igual a 575
        player1_y = 575  # Ela passará a ser 575, ou seja irá ter um limite de descida na tela

    # print(player1_y) -- Mostra a posição do player 1


def move_player2():  # Função move_player 2
    global player2_y  # Chamada da variavel player2_y

    if player2_moveup:
        player2_y -= 5

    else:
        player2_y += 0
    
    if player2_movedown:
        player2_y += 5
    
    else:
        player2_y -= 0
    
    if player2_y <= 0:
        player2_y = 0
    
    elif player2_y > 575:
        player2_y = 575



def move_ball():  # Função para movimentar bola
    global ball_x  # Global == Chamada da variável dentro da função para alteração
    global ball_y  # Global == Chama da variável dentro da função para alteração
    global ball_dir  # Global == Chamada da variável dentro da função para alteração
    global ball_dir_y  # Global == Chamada da variavel dentro da função para alteração
    global score1  # Global == Chamada da variavel dentro da função para alteração
    global score2  # Global == Chamada da variavel dentro da função para alteração
    global score2_img  # Global == Chamada da variavel dentro da função para alteração
    global score1_img  # Global == Chamada da variavel dentro da função para alteração

    ball_x += ball_dir  # Variável recebe 1
    ball_y += ball_dir_y  # Variável ball_y recebe a variavel ball_dir_y

    if ball_x < 120:  # Se a bola no eixo y for menor que 120 --- Player 1
        if player1_y < ball_y + 23:  # E se a posição do player1_y menor que bola_y mais a metade da bola
            if player1_y + 146 > ball_y:  # E se player 1 mais o seu tamanho original for maior que a bola no eixo y
                ball_dir *= -1  # A direção da bola irá se inverter

    if ball_x > 1100:  # Se a bola no eixo x for menor que 1150 --- Player 2
        if player2_y < ball_y + 23:  # E se a posição do player1_y menor que bola_y mais a metade da bola
            if player2_y + 146 > ball_y:  # E se player 1 mais o seu tamanho original for maior que a bola no eixo y
                ball_dir *= -1  # A direção da bola irá se inverter

    if ball_y > 685:  # Se a bola no eixo y for maior que 685
        ball_dir_y *= -1  # Ball_dir_y recebe multiplicando -1 ou seja inverte a bola
    elif ball_y <= 0:  # Se a bola no eixo y for menor ou igual a 0
        ball_dir_y *= -1  # Ball_dir_y recebe multipllicando -1 ou seja inverte a bola

    if ball_x < -50:  # Condicional Player 2, se ball_x for menor que - 50
        ball_x = 617  # A bola retorna a posição 617 no eixo x
        ball_y = 337  # A bola retorna a posição 337 no eixo y
        ball_dir_y *= -1  # A bola retorna volta a se movimentar
        ball_dir *= -1  # Velocidade da direção da bola
        score2 += 1  # Placar do player  2 Ganho aumenta + 1
        # A imagem do placar do player 2 aumenta mais um ponto
        score2_img = pygame.image.load("assets/score/" + str(score2) + '.png')

    elif ball_x > 1320:  # Condicional player 2, se a ball_x for maior que 1320
        ball_x = 617  # A bola retorna a posição 617 no eixo x
        ball_y = 337  # A bola retorna a posição 337 no eixo y
        ball_dir_y *= -1  # A Bola retorna e volta a se movimentar
        ball_dir *= -1  # Velocidade da direção da bola
        score1 += 1  # Placar do Player 1 Ganho aumenta + 1
        # A imagem do placar do player 1 aumenta mais um ponto
        score2_img = pygame.image.load("assets/score/" + str(score1) + '.png')


def draw():  # Função para desenhar os itens na tela
    if score1 or score2 < 9:
        # Desenhar imagem na tela e respectivamente define sua posição
        window.blit(field, (0, 0))
        # Desenha o sprite e define sua posição
        window.blit(player1, (50, player1_y))
        # Desenha o sprite e define a posição
        window.blit(player2, (1150, player2_y))
        window.blit(ball, (ball_x, ball_y))  # Desenha a bola e define sua posição
        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))
        move_ball()  # Chamada da função move_ball
        move_player()  # Chamada da função move_player
        move_player2()  # Chamada da função move_player2
    
    else:
        window.blit(win, (300,330))


loop = True  # Variável controle de loop
while loop:  # Loop da tela

    for events in pygame.event.get():  # Para cada evento que a bibiloteca usar o for irá usar
        if events.type == pygame.QUIT:  # Se o tipo de evento for fechar
            loop = False  # Definição de fim de loop

        if events.type == pygame.KEYDOWN:  # Se o tipo de evento for de pressionar o teclado
            if events.key == pygame.K_w:  # E se esse evento for a tecla W
                player1_moveup = True  # A variavel passará a ser verdadeira
            if events.key == pygame.K_s:  # E se esse evento for a tecla S
                player1_movedown = True  # A variavel passará a ser verdadeira

        if events.type == pygame.KEYUP:  # Se o tipo de evento for de soltar o teclado
            if events.key == pygame.K_w:  # E se esse evento for a tecla W
                player1_moveup = False  # A variavel passará a ser Falsa

            if events.key == pygame.K_s:  # E se esse evento for a tecla S
                player1_movedown = False  # A variavel passará a ser Falsa
        
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_i:
                player2_moveup = True
            if events.key == pygame.K_k:
                player2_movedown = True
        
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_i:
                player2_moveup = False
            if events.key == pygame.K_k:
                player2_movedown = False

    draw()  # Chamada da função draw
    pygame.display.update()  # Atualização de tela, manter tela
