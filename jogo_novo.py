import pygame
import sys

pygame.init()

janela = pygame.display.set_mode([1024, 783])
pygame.display.set_caption("Jogo em Python")

fundo_voltar = pygame.image.load("floresta.jpeg")
fundo_jogo = pygame.image.load("fundo1.jpeg")
fundo_fase_um = pygame.image.load('fase1.jpeg')

BRANCO = (255, 255, 255)
VERDE = (70, 130, 186)
VERMELHO = (70, 130, 186)
AZUL = (0, 0, 255)
AZUL_CLARO = (173, 216, 230)
AMARELO = (255, 255, 0)


fonte = pygame.font.SysFont(None, 50)
raio_arredondamento = 10

estado = 'voltar'

def desenhar_botao(texto, x, y, largura, altura, cor, acao=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(janela, VERDE, (x - 2, y - 2, largura + 4, altura + 4), border_radius=raio_arredondamento + 2)

    pygame.draw.rect(janela, cor, (x, y, largura, altura), border_radius=raio_arredondamento)

    if x < mouse[0] < x + largura and y < mouse[1] < y + altura:
        if click[0] == 1 and acao:
            acao()

    texto_render = fonte.render(texto, True, VERDE)
    janela.blit(texto_render, (
        x + (largura // 2 - texto_render.get_width() // 2),
        y + (altura // 2 - texto_render.get_height() // 2)
    ))  

def iniciar_jogo():
      global estado
      estado = 'jogo'

def voltar_voltar():
    global estado
    estado = 'voltar'

def cena_um():
    global estado
    estado = 'avançar'

def sair():
    pygame.quit()
    sys.exit()

loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    if estado == 'voltar':
         janela.blit(fundo_voltar, (0, 0))
         fundo_voltar = pygame.image.load("floresta.jpeg")
         desenhar_botao("Iniciar", 412, 500, 200, 60, AZUL_CLARO, iniciar_jogo)
         desenhar_botao("Sair", 412, 580, 200, 60, AZUL_CLARO, sair)

    elif estado == 'jogo':
            janela.blit(fundo_jogo, (0, 0))
            fundo_jogo = pygame.image.load("fundo1.jpeg")
            desenhar_botao("Voltar", 10, 10, 150, 50, AZUL_CLARO, voltar_voltar)
            desenhar_botao("Avançar", 700, 10, 150, 50, AZUL_CLARO, cena_um)
        


  
    pygame.display.update()

pygame.quit()