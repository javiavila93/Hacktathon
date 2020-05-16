import pygame, random
import datetime

# Varibbles, tamaño  bola.top += speed_bola_x
    bola.left += speed_bola_y


# Colors
back_color = (200, 200, 200)
light_gray = pygame.Color('grey12')

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

rectangulo = pygame.Rect(10, 10, 50, 140)
speed = 0
bola =pygame.Rect(10, 10, 50, 0)
speed_bola_x = 3
speed_bola_y = 3

def start_bola():
    if bola.left + 50 > screen.width:
        bola.top = screen_heighthttps://github.com/GeeksHubsAcademy/2020-hackathon-zero-python-Fundamentos

def mover_rectangulo():
    global speed
    rectangulo.top += 1
    if rectangulo.top + 50 < screen_height:
        rectangulo.top += speed

def mover_bola():
    global speed_bola_y, speed_bola_x
    if bola.top + 50 > screen_height:
        speed_bola_x = - speed_bola_x
    if bola.left + 50 > screen_width:
https://github.com/GeeksHubsAcademy/2020-hackathon-zero-python-Fundamentos

  

while True:
    screen.fill(light_gray)https://github.com/GeeksHubsAcademy/2020-hackathon-zero-python-Fundamentos
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed = -3
            elif event.key == pygame.K_DOWN:
        if event.type == pygame.KEYUP:
            speed = 0

    pygame.draw.rect(screen, back_color, rectangulo)
    pygame.draw.ellipse(screen, back_color, bola)
    pygame.display.flip()
    clock.tick(60)
    mover_rectangulo()
    mover_bola()


''' rebote
    if bola.left < 10 and rectangulo.top < bola.top < rectagunlo.top + 140
        speed_bola_y = -speed_bola_yhttps://github.com/GeeksHubsAcademy/2020-hackathon-zero-python-Fundamentos
    
    
    
    '''