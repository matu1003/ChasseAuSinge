import pygame
from game_agents import Tom, Jerry, Cannon # Importation des differents elements de la simulation
from math import atan, cos, sin # Importation des fonction trigos

pygame.init() # Initialisation pygame
WIN_W = int(0.95*pygame.display.Info().current_w) # Fenetre qui recouvre 95 % de la largeur ...
WIN_H = int(0.95*pygame.display.Info().current_h) # Et 95 % de la hauteur

win = pygame.display.set_mode((WIN_W, WIN_H)) # Creation de la fenetre
pygame.display.set_caption("Canon") # Titre fenetre
win.fill((255, 255, 255)) # Fond blanc


############ NOTES IMPORTANTES ################
#Dans Pygame, x = 0, y = 0 est le point en haut a gauche de l'ecran
#Il faut donc faire attention a appliquer -vy pour les déplacements
###############################################

# Importation des images
canon_img = pygame.image.load("Images/canon.png") 
canon_img = pygame.transform.scale(canon_img, (40, 20))

head_img = pygame.image.load("Images/head.png")
head_img = pygame.transform.scale(head_img, (40, 20))

tom_img = pygame.image.load("Images/Tom.png")
tom_img = pygame.transform.scale(tom_img, (80, 50))

jerry_img = pygame.image.load("Images/Jerry.png")
jerry_img = pygame.transform.scale(jerry_img, (30, 30))

# Parametres de la simulation:

L = 1000 # Distance en m entre 30 et largeur de l'ecran, distance de singe
H = 800 # Distance en m entre 30 et hauteur de l'ecran, hauteur du singe
v0 = 150 # Vitesse initiale en m.s-1, valeur positive
alpha = atan(H/L) # Calcul de l'angle de tir initial
x0 = 20 # x de l'origine
y0 = WIN_H - 20 # y de l'origine
g = 9.81 # Contante gravitationelle


cannon = Cannon(x0, y0, head_img, canon_img, alpha) # Creation du cannon a x0, y0 avec une inclinaison de alpha radians

v0xtom = v0*cos(alpha) # Decomposition des coordonnees de vitesse initiale projectile
v0ytom = v0*sin(alpha)
tom = Tom(x0, y0, tom_img, v0xtom, v0ytom, 0, -g) # Tom: le projectile qui demare a x0, y0 avec ax = 0 et ay = -g
jerry = Jerry(x0 + L, y0 - H, jerry_img, 0, 0, 0, -g) # Jerry = le singe demare a x0 + L, y0 - H (y = 0 est en haut) et avec ax = 0 et ay = -g 

clock = pygame.time.Clock() # Pendule pour controler le nombre d'iteration par seconde de la boucle de simulation

while True:
    #Boucle de simulation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Si on veux fermer la fenetre
            pygame.quit()
            break

    if jerry.centerx - tom.centerx >= 0:
        #Tant que Tom n'a pas depasse Jerry
        #Mouvement:
        # Comme on a 25 iteration par seconde, dt = 0.04
        tom.move(0.04)
        jerry.move(0.04)
    
    # Clear screen
    win.fill((255, 255, 255))
        
    # Draw elements
    cannon.draw(win)
    tom.draw(win)
    jerry.draw(win)
    
    # Fixe le nombre d'etapes par seconde a 25
    clock.tick(25)

    pygame.display.update() # Update screen
