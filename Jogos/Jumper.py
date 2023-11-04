import pygame
import os
pygame.init()

# Configurações da tela
display = pygame.display.set_mode((1280, 720))
fps = pygame.time.Clock()
fonte = pygame.font.SysFont('arial', 60,True,False)
# Variaveis
jogando = True
BolaX = 1260
BolaY = 663
VelocidadeBola = 17
VelY= 17
BonecoY = 620
pulo = False
pontos = 0
while jogando:

    exibe_pontos = f'{pontos}'
    pontos1 = fonte.render(exibe_pontos, False, (255, 255, 255))
    Boneco = pygame.Rect(30,BonecoY,60,60)
    chao = pygame.Rect(0,680,1280,40)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            jogando = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pulo = True
    if pulo:
        BonecoY -= VelY
        VelY -= 1
        if BonecoY ==620:
            VelY = 17
            pulo = False
    if Boneco.colliderect(BolaX-25,BolaY-25,15, 15):
        jogando = False
    # Limitar FPS
    fps.tick(60)

    # Atualizar tela
    pygame.display.flip()
    if BolaX > 20:
        BolaX -= VelocidadeBola
    else:
        BolaX = BolaX + 1260
        VelocidadeBola += VelocidadeBola *0.005
        print(VelocidadeBola)
        pontos += 1


    display.fill((0, 0, 0))
    pygame.draw.circle(display, (255, 255, 255), (BolaX,BolaY), 15)
    pygame.draw.rect(display, (194, 35, 35), chao)
    pygame.draw.rect(display, (66, 135, 245), Boneco)
    display.blit(pontos1,(0, 0))
    pygame.display.update()