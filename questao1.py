#importando Bibliotecas
import pygame
import math
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
#definindo formas geométricas

pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura), DOUBLEBUF | OPENGL)
glViewport(0, 0, largura, altura)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, largura, altura, 0, 1, -1)
glMatrixMode(GL_MODELVIEW)

def desenhar_quadrado():
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)  # Cor vermelha
    glVertex2f(100, 100)
    glVertex2f(100, 200)
    glVertex2f(200, 200)
    glVertex2f(200, 100)
    glEnd()

def desenhar_triangulo():
    glBegin(GL_TRIANGLES)
    glColor3f(0, 1, 0)  # Cor verde
    glVertex2f(300, 100)
    glVertex2f(250, 200)
    glVertex2f(350, 200)
    glEnd()

def desenhar_circulo():
    raio = 50
    num_segmentos = 100
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0, 0, 1)  # Cor azul
    glVertex2f(500, 150)
    for i in range(num_segmentos + 1):
        theta = 2.0 * 3.1415926 * float(i) / float(num_segmentos)
        x = raio * math.cos(theta)
        y = raio * math.sin(theta)
        glVertex2f(x + 500, y + 150)
    glEnd()

def desenhar_retangulo():
    glBegin(GL_QUADS)
    glColor3f(1, 1, 0)  # Cor amarela
    glVertex2f(600, 100)
    glVertex2f(600, 200)
    glVertex2f(700, 200)
    glVertex2f(700, 100)
    glEnd()

def desenhar_pentagono():
    glBegin(GL_POLYGON)
    glColor3f(1, 0, 1)  # Cor roxa
    glVertex2f(700, 300)
    glVertex2f(750, 400)
    glVertex2f(700, 500)
    glVertex2f(650, 500)
    glVertex2f(600, 400)
    glEnd()

def main():
    pygame.init()
   # display = (800,600)
    #pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    #glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #glRotatef(-1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        desenhar_quadrado()
        desenhar_pentagono()
        desenhar_circulo()
        desenhar_retangulo()
        desenhar_triangulo()
        
        pygame.display.flip()
        pygame.time.wait(10)

main()