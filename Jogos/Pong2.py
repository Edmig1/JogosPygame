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
personagem1 = pygame.image.load('../assets2/senai.PNG')
personagem1 = pygame.transform.scale(personagem1,(60,179))
boxP1 = personagem1.get_rect()
boxP1.center = (59.5, 360)
personagem2 = pygame.image.load('../assets2/sesi.PNG')
personagem2 = pygame.transform.scale(personagem2,(60,179))
boxP2 = personagem2.get_rect()
boxP2.center = (59.5, 360)
boxP2.x = 1200
boxP1.x = 20

bolinha = pygame.image.load("../assets2/derso.png")
bolinha = pygame.transform.scale(bolinha,(60,60))
bolinha_rect = bolinha.get_rect()
bolinha_rect.center = (630,360)

velociodadePersonagem = 5
# menu
menu = pygame.image.load('../assets/DERSONG.png')
rect_menu = menu.get_rect()

# som da bola
som_bola = pygame.mixer.Sound('../assets2/faro.wav')

#musica
musica = pygame.mixer.Sound('../assets2/derso.wav')
musica.play(-1)
# Carrega imagem de bg
bg = pygame.image.load("../assets2/ceu.png")

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
    if pontos1 == 5:
        cena = 'fim'
        ganhador = 'Player 1 Ganhou'
    elif pontos2 == 5:
        cena = 'fim'
        ganhador = 'Player 2 Ganhou'

    if cena == 'menu':
        display.blit(menu,rect_menu)
    elif cena == 'fim':
        display.blit(fonte.render(ganhador,True,(255,255,255),),(580,200))
    elif cena == 'jogo':
        musica.stop()
        # Pontos do jogador
        if bolinha_rect.centerx >= 1280:
            velocidadeBolaX *= -1
            pontos1 +=1
            bolinha_rect.centery = 360
            bolinha_rect.centerx = 640
            exibe_pontos = f'{pontos1} - {pontos2}'

        elif bolinha_rect.centerx  <= 0:
            velocidadeBolaX *= -1
            pontos2 +=1
            bolinha_rect.centery = 360
            bolinha_rect.centerx = 640
            exibe_pontos = f'{pontos1} - {pontos2}'


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
        display.blit(pontos,(580, 100))

