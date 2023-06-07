import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def draw_cube():
    vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    )

    faces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )

    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_cylinder():
    slices = 50
    height = 2.0
    radius = 1.0

    glBegin(GL_TRIANGLE_STRIP)
    for i in range(slices + 1):
        angle = 2.0 * 3.14159 * i / slices
        x = radius * math.cos(angle)
        y = height
        z = radius * math.sin(angle)
        glVertex3f(x, y, z)
        glVertex3f(x, -y, z)
    glEnd()

def draw_cone():
    slices = 50
    height = 2.0
    radius = 1.0

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, height, 0.0)
    for i in range(slices + 1):
        angle = 2.0 * 3.14159 * i / slices
        x = radius * math.cos(angle)
        z = radius * math.sin(angle)
        glVertex3f(x, -height, z)
    glEnd()

    glBegin(GL_TRIANGLES)
    for i in range(slices + 1):
        angle1 = 2.0 * 3.14159 * i / slices
        angle2 = 2.0 * 3.14159 * (i + 1) / slices
        x1 = radius * math.cos(angle1)
        z1 = radius * math.sin(angle1)
        x2 = radius * math.cos(angle2)
        z2 = radius * math.sin(angle2)
        glVertex3f(0.0, height, 0.0)
        glVertex3f(x1, -height, z1)
        glVertex3f(x2, -height, z2)
    glEnd()

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glColor3f(1.0, 0.0, 0.0)  # Red color for the cube
        draw_cube()
        glTranslatef(3.0, 0.0, 0.0)
        
        glColor3f(0.0, 1.0, 0.0)  # Green color for the cylinder
        draw_cylinder()
        glTranslatef(-6.0, 0.0, 0.0)
        
        glColor3f(0.0, 0.0, 1.0)  # Blue color for the cone
        draw_cone()
        glTranslatef(3.0, 0.0, 0.0)
        
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
