import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Cria a janela
janela = pygame.display.set_mode([1024, 783])
pygame.display.set_caption("Jogo em Python")

# Carrega a imagem de fundo
fundo = pygame.image.load("floresta.jpeg")

# Define cores
BRANCO = (255, 255, 255)
VERDE = (70, 130, 186)
VERMELHO = (70, 130, 186)

# Fonte
fonte = pygame.font.SysFont(None, 50)
raio_arredondamento = 10  # Raio dos cantos arredondados

# Função para desenhar botões com borda branca
def desenhar_botao(texto, x, y, largura, altura, cor, acao=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Desenha a borda branca (um retângulo maior)
    pygame.draw.rect(janela, BRANCO, (x - 2, y - 2, largura + 4, altura + 4), border_radius=raio_arredondamento + 2)

    # Desenha o botão com cantos arredondados
    pygame.draw.rect(janela, cor, (x, y, largura, altura), border_radius=raio_arredondamento)

    # Verifica clique
    if x < mouse[0] < x + largura and y < mouse[1] < y + altura:
        if click[0] == 1 and acao:
            acao()

    # Renderiza o texto centralizado
    texto_render = fonte.render(texto, True, BRANCO)
    janela.blit(texto_render, (
        x + (largura // 2 - texto_render.get_width() // 2),
        y + (altura // 2 - texto_render.get_height() // 2)
    ))

# Ações dos botões
def iniciar_jogo():
    print("Jogo iniciado!")

def sair():
    pygame.quit()
    sys.exit()

# Loop principal
loop = True
while loop:
    janela.blit(fundo, (0, 0))

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False

    # Desenha os botões com borda branca
    desenhar_botao("Start", 412, 500, 200, 60, VERDE, iniciar_jogo)
    desenhar_botao("Exit", 412, 580, 200, 60, VERMELHO, sair) 

  
    pygame.display.update()

pygame.quit()