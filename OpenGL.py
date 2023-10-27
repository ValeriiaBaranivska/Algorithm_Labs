"""
Виконала: Баранівська Валерія КМ-23

Завдання:
    1. Ознайомитись з описом API наприклад OpenGL
    2. Створити трьохвимірну форму (наприклад, тор, брусок, або напів сферу) Анімувати створену форму
 Наприклад: 
    по натисканню лівої кнопки миші міняє колір; 
    по натисканню правої кнопки миші включає або вимикає режим обертання; 
    по натисканню клавіш Вгору/ вниз збільшує/уповільнює обертання; 
    по натисканню клавіші ПРОБІЛ міняє осі обертання.
"""

import random
from math import*
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Глобальні змінні, які використовуються для контролю анімації
current_color = (0.8, 0.6, 1.0, 1.0)# Поточний колір тору
rotation_enabled = True # Чи ввімкнений режим обертання
current_rotation_axis = 'z' # Поточна вісь обертання


def create_torus(R, r, n, m):
    """
    Створення тору.
    """
    vertices = []
    colors = []  # Збереження кольорів для кожної вершини

    for i in range(n):
        for j in range(m):
            theta = 2 * j * pi / m
            psi = 2 * i * pi / n

            x = (R + r * cos(psi)) * cos(theta)
            y = (R + r * cos(psi)) * sin(theta)
            z = r * sin(psi)

            color = (0.8, 0.6, 1.0, 1.0)
            vertices.append((x, y, z))
            colors.append(colors)
    return vertices, colors 

def draw_torus(R, r, n, m, colors):
    torus, _ = create_torus(R, r, n, m)  # Ignore the second return value from create_torus
    glBegin(GL_TRIANGLES) #ствоерння трикутників
    for i in range(n - 1):
        for j in range(m):
            #вершини для трикутників
            vertex1 = torus[i * m + j]
            vertex2 = torus[i * m + (j + 1) % m]
            vertex3 = torus[(i + 1) * m + j]
            vertex4 = torus[(i + 1) * m + (j + 1) % m]

            # встановлення кольору для кожної вершини
            glColor4fv(colors[i * m + j])
            glVertex3fv(vertex1)
            glColor4fv(colors[i * m + (j + 1) % m])
            glVertex3fv(vertex2)
            glColor4fv(colors[(i + 1) * m + j])
            glVertex3fv(vertex3)

            glColor4fv(colors[(i + 1) * m + j])
            glVertex3fv(vertex3)
            glColor4fv(colors[i * m + (j + 1) % m])
            glVertex3fv(vertex2)
            glColor4fv(colors[(i + 1) * m + (j + 1) % m])
            glVertex3fv(vertex4)

    glEnd()

def change_color():
    """
    Зміна кольору тору на випадковий.
    """
    global current_color
    new_color = (random.random(), random.random(), random.random(), 1.0)# генераціяя рандомного кольору
    current_color = new_color
    
def toggle_rotation():
    """
    Ввімкнення/вимикання режиму обертання.
    """
    global rotation_enabled
    rotation_enabled = not rotation_enabled
    
def switch_rotation_axis():
     """
    Зміна осі обертання тору.
    """
    global current_rotation_axis
    if current_rotation_axis == 'x':
        current_rotation_axis = 'y'
    elif current_rotation_axis == 'y':
        current_rotation_axis = 'z'
    else:
        current_rotation_axis = 'x'
    
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)# Задаємо розмір вікна програми

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)# Встановлюємо перспективу для відображення 3D-сцени
    glTranslatef(0.0, 0.0, -15)
    glRotatef(0, 0, 0, 0)# Встановлюємо початковий поворот камери

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Ліва клавіша миші
                    change_color()
                elif event.button == 3:  # Права клавіша миші
                    toggle_rotation()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:  # натискання пробілу
                    switch_rotation_axis()

        if rotation_enabled:
            if current_rotation_axis == 'x':
                glRotatef(2, 1, 0, 0)
            elif current_rotation_axis == 'y':
                glRotatef(2, 0, 1, 0)
            else:
                glRotatef(2, 0, 0, 1)

        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)# Очищаємо буфери кольору та глибини
        torus, colors = create_torus(2, 1, 30, 30)
        draw_torus(2, 1, 30, 30, [current_color] * len(colors))# Створюємо список кольорів для вершин тору

        pygame.display.flip()# Перевертаємо буфер кадрів
        pygame.time.wait(10) 

if __name__ == '__main__':
    main()
