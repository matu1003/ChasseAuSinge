import pygame
from game_agents import Tom, Jerry, Cannon
from math import atan, cos, sin

pygame.init()
WIN_W = int(0.95*pygame.display.Info().current_w)
WIN_H = int(0.95*pygame.display.Info().current_h)

win = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("Canon")
win.fill((255, 255, 255))



canon_img = pygame.image.load("Images/canon.png")
canon_img = pygame.transform.scale(canon_img, (40, 20))

head_img = pygame.image.load("Images/head.png")
head_img = pygame.transform.scale(head_img, (40, 20))

tom_img = pygame.image.load("Images/Tom.png")
tom_img = pygame.transform.scale(tom_img, (80, 50))

jerry_img = pygame.image.load("Images/Jerry.png")
jerry_img = pygame.transform.scale(jerry_img, (30, 30))

# Parametres de la simulation:

L = 1000 # Distance entre 30 et largeur de l'ecran
H = 800 # Distance entre 30 et hauteur de l'ecran
v0 = 150
alpha = atan(H/L)
x0 = 20 # x de l'origine
y0 = WIN_H - 20 # y de l'origine
g = 9.81

cannon = Cannon(x0, y0, head_img, canon_img, alpha)
v0xtom = v0*cos(alpha)
v0ytom = v0*sin(alpha)
tom = Tom(x0, y0, tom_img, v0xtom, v0ytom, 0, -g)
jerry = Jerry(x0 + L, y0 - H, jerry_img, 0, 0, 0, -g)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

    if jerry.centerx - tom.centerx >= 0:
        #Movement:
        tom.move(0.04)
        jerry.move(0.04)

        # Dessin
        # win.fill((255, 255, 255))
    cannon.draw(win)
    tom.draw(win)
    jerry.draw(win)

    clock.tick(25)

    pygame.display.update()
