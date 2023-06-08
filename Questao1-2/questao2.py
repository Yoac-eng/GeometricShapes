import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Inicialização do Pygame
pygame.init()
largura = 800
altura = 600
pygame.display.set_mode((largura, altura), DOUBLEBUF | OPENGL)

# Configuração da câmera
glViewport(0, 0, largura, altura)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, largura, 0, altura, -1, 1)
glMatrixMode(GL_MODELVIEW)

# Definição das variáveis para as transformações
x = 200
y = 200
angulo = 0
escala = 1.0

# Definição do clock
clock = pygame.time.Clock()

# Loop principal
while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Limpar o buffer de cores e o buffer de profundidade
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Realizar as transformações
    glLoadIdentity()
    glTranslatef(x, y, 0)
    glRotatef(angulo, 0, 0, 1)
    glScalef(escala, escala, 1.0)

    # Desenhar o quadrado
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)  # Cor vermelha
    glVertex2f(-50, -50)
    glVertex2f(50, -50)
    glVertex2f(50, 50)
    glVertex2f(-50, 50)
    glEnd()

    # Atualizar a tela
    pygame.display.flip()

    # Aumentar o ângulo
    angulo += 1

    # Alterar a escala
    escala += 0.01
    if escala >= 2.0:
        escala = 1.0

    # Alterar a posição
    x += 1
    if x >= largura:
        x = 0

    y += 1
    if y >= altura:
        y = 0