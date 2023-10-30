import pygame
import os
pygame.init()

# Configurações da tela
display = pygame.display.set_mode((1280, 720))
fps = pygame.time.Clock()
fonte = pygame.font.SysFont('arial', 60,True,False)
# Variaveis
jogando = True

personagem1Y = 0
personagem2Y = 0

velociodadePersonagem = 5
velociodadePersonagem2 = 5

# Informações da bola
bolaX = 640
bolaY = 360
velocidadeBolaX = 7
velocidadeBolaY = 7
pontos1 = 0
pontos2 = 0
# Loop principal
while jogando:
    # Tela Incio

    def carregar():
        imagens = os.path.join(os.getcwd(),'imagens')

    exibe_pontos = f'{pontos1} - {pontos2}'
    pontos = fonte.render(exibe_pontos,False,(255,255,255))
    # Eventos do jogo
    for event in pygame.event.get():

        # Sair do jogo
        if event.type == pygame.QUIT:
            jogando = False

        # Movimentar personagem
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    velociodadePersonagem *= -1
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    velociodadePersonagem2 *= -1



    # Limitar FPS
    fps.tick(60)

    # Atualizar tela
    pygame.display.flip()

    # Limitar movimentação
    if personagem1Y >= 520:
        personagem1Y = 520
    elif personagem1Y <= 0:
        personagem1Y = 0

    if personagem2Y >= 520:
        personagem2Y = 520
    elif personagem2Y <= 0:
        personagem2Y = 0

    # Limitar movimentação da bola
    if bolaX >= 1280:
        velocidadeBolaX *= -1
        pontos1 +=1
        exibe_pontos = f'{pontos1} - {pontos2}'
        if pontos1 >= 5:
            jogando = False
            print('Player 2 Ganhou')
        print(exibe_pontos)
    elif bolaX <= 0:
        velocidadeBolaX *= -1
        pontos2 +=1
        exibe_pontos = f'{pontos1} - {pontos2}'
        if pontos2 >= 5:
            print('Player 2 Ganhou')
            jogando = False
        print(exibe_pontos)

    if bolaY >= 720:
        velocidadeBolaY *= -1
    elif bolaY <= 0:
        velocidadeBolaY *= -1

    personagem1Y += velociodadePersonagem
    personagem2Y += velociodadePersonagem2

    # Criar retangulos
    personagem1 = pygame.Rect(10,personagem1Y,20,200)
    personagem2 = pygame.Rect(1250,personagem2Y,20,200)

    # Movimentar bola
    bolaX += velocidadeBolaX
    bolaY += velocidadeBolaY

    # Colisão da bola com o personagem
    if personagem1.colliderect(bolaX, bolaY, 10, 10):
        velocidadeBolaX *= -1

    if personagem2.colliderect(bolaX, bolaY, 10, 10):
        velocidadeBolaX *= -1

    # Desenhar na tela
    display.fill((0, 0, 0))
    pygame.draw.rect(display, (194, 35, 35), personagem1)
    pygame.draw.rect(display, (26, 161, 214), personagem2)
    display.blit(pontos,(600, 100))
    # Bola
    pygame.draw.circle(display, (255, 255, 255), (bolaX, bolaY), 10)
    pygame.display.update()