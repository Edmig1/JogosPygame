import pygame
import os
pygame.init()

# Configurações da tela
display = pygame.display.set_mode((1280, 720))
fps = pygame.time.Clock()
fonte = pygame.font.SysFont('arial', 60,True,False)

cena = 'menu'
ganhador = ''
# Variaveis
jogando = True

# Criar retangulos
personagem1 = pygame.image.load('../assets/player1.png')
boxP1 = personagem1.get_rect()
boxP1.center = (59.5, 360)
personagem2 = pygame.image.load('../assets/player2.png')
boxP2 = personagem2.get_rect()
boxP2.center = (59.5, 360)
boxP2.x = 1171

bolinha = pygame.image.load("../assets/ball.png")
bolinha_rect = bolinha.get_rect()
bolinha_rect.center = (630,360)

velociodadePersonagem = 5
# menu
menu = pygame.image.load('../assets/menu.png')
rect_menu = menu.get_rect()

# som da bola
som_bola = pygame.mixer.Sound('../assets/pong.wav')

# Carrega imagem de bg
bg = pygame.image.load("../assets/bg.png")

# Informações da bola
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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and cena != 'jogo':
                cena = 'jogo'

    # Limitar FPS
    pygame.display.update()
    fps.tick(60)

    #bg
    display.fill((0, 0, 0))

    if cena == 'menu':
        display.blit(menu,rect_menu)

    elif cena == 'jogo':
        # Pontos do jogador
        if bolinha_rect.centerx >= 1280:
            velocidadeBolaX *= -1
            pontos1 +=1
            bolinha_rect.centery = 360
            bolinha_rect.centerx = 640
            exibe_pontos = f'{pontos1} - {pontos2}'
            if pontos1 >= 5:
                jogando = False

        elif bolinha_rect.centerx  <= 0:
            velocidadeBolaX *= -1
            pontos2 +=1
            bolinha_rect.centery = 360
            bolinha_rect.centerx = 640
            exibe_pontos = f'{pontos1} - {pontos2}'

            if pontos2 >= 5:
                jogando = False

        if bolinha_rect.centery >= 720:
            som_bola.play()
            velocidadeBolaY *= -1
        elif bolinha_rect.centery <= 0:
            som_bola.play()
            velocidadeBolaY *= -1


        # Movimentar personagem
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            boxP1.centery -= velociodadePersonagem
            if boxP1.centery <86.5:
                boxP1.centery+=5
        if keys[pygame.K_s]:
            boxP1.centery += velociodadePersonagem
            if boxP1.centery > 633.5:
                boxP1.centery-=5

        if keys[pygame.K_UP]:
            boxP2.centery -= velociodadePersonagem
            if boxP2.centery <86.5:
                boxP2.centery+=5

        if keys[pygame.K_DOWN]:
            boxP2.centery += velociodadePersonagem
            if boxP2.centery > 633.5:
                boxP2.centery-=5

        # Movimentar bola
        bolinha_rect.centery +=velocidadeBolaY
        bolinha_rect.centerx +=velocidadeBolaX

        # Colisão da bola com o personagem
        if  boxP1.colliderect(bolinha_rect.centerx, bolinha_rect.centery, 10, 10):
            som_bola.play()
            velocidadeBolaX *= -1

        if boxP2.colliderect(bolinha_rect.centerx, bolinha_rect.centery, 10, 10):
            som_bola.play()
            velocidadeBolaX *= -1
        # Desenhar na tela
        display.blit(bg, (0, 0))

        # Desenhar os personagens
        display.blit(personagem1, boxP1)
        display.blit(personagem2, boxP2)
        display.blit(bolinha,bolinha_rect)
        display.blit(pontos,(600, 100))

