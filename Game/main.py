import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
cor_fundo = (0, 0, 0)
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)

# Dimensões da janela do jogo
largura = 800
altura = 800

# Tamanho da cobrinha e da comida
tamanho = 20

# Criação da janela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Cobrinha")

# Função para exibir a pontuação na tela
def mostrar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont(None, 25)
    texto = fonte.render("Pontuação: " + str(pontuacao), True, cor_cobra)
    tela.blit(texto, (10, 10))

# Função para desenhar a cobra na tela
def desenhar_cobra(lista_cobra):
    for x, y in lista_cobra:
        pygame.draw.rect(tela, cor_cobra, (x, y, tamanho, tamanho))

# Função principal do jogo
def jogo():
    # Posição inicial da cobra
    x_cobra = largura / 2
    y_cobra = altura / 2

    # Velocidade da cobra
    velocidade_x = 0
    velocidade_y = 0

    # Lista para armazenar as posições da cobra
    lista_cobra = []
    comprimento_inicial = 1

    # Posição inicial da comida
    x_comida = round(random.randrange(0, largura - tamanho) / 20) * 20
    y_comida = round(random.randrange(0, altura - tamanho) / 20) * 20

    # Variável para controlar o jogo
    fim_jogo = False

    # Variável para controlar a pontuação
    pontuacao = 0
    
    #Incrementar velocidade de jogo
    incrementador_frame = 0
    
    # Loop principal do jogo
    while not fim_jogo:
        # Eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_jogo = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    velocidade_x = -tamanho
                    velocidade_y = 0
                elif event.key == pygame.K_RIGHT:
                    velocidade_x = tamanho
                    velocidade_y = 0
                elif event.key == pygame.K_UP:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                elif event.key == pygame.K_DOWN:
                    velocidade_x = 0
                    velocidade_y = tamanho

        # Atualização da posição da cobra
        x_cobra += velocidade_x
        y_cobra += velocidade_y

        # Verificação de colisões com a parede
        if x_cobra >= largura or x_cobra < 0 or y_cobra >= altura or y_cobra < 0:
            fim_jogo = True

        # Preenchimento do fundo da tela
        tela.fill(cor_fundo)

        # Desenho da comida
        pygame.draw.rect(tela, cor_comida, (x_comida, y_comida, tamanho, tamanho))

        # Atualização da lista da cobra
        cabeca_cobra = []
        cabeca_cobra.append(x_cobra)
        cabeca_cobra.append(y_cobra)
        lista_cobra.append(cabeca_cobra)

        if len(lista_cobra) > comprimento_inicial:
            del lista_cobra[0]

        # Verificação de colisão com a própria cobra
        for segmento in lista_cobra[:-1]:
            if segmento == cabeca_cobra:
                fim_jogo = True

        # Desenho da cobra
        desenhar_cobra(lista_cobra)

        # Verificação de colisão com a comida
        if x_cobra == x_comida and y_cobra == y_comida:
            x_comida = round(random.randrange(0, largura - tamanho) / 20) * 20
            y_comida = round(random.randrange(0, altura - tamanho) / 20) * 20
            comprimento_inicial += 1
            pontuacao += 1
            incrementador_frame += 0.2

        # Exibição da pontuação
        mostrar_pontuacao(pontuacao)

        # Atualização da tela
        pygame.display.update()

        # Controle de FPS
        pygame.time.Clock().tick(15 + incrementador_frame)
        
    # Encerramento do Pygame
    pygame.quit()

# Execução do jogo
jogo()
