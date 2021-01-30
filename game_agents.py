import pygame
from math import sin, cos, atan

class Tom:
    # Une representation de Tom
    def __init__(self, centerx, centery, img, vx, vy, ax, ay):
        # Initialisation des parametres
        self.centerx = centerx # Coordonnées du centre de masse de Tom
        self.centery = centery # ...
        self.vx = vx # Vitesse selon les axes
        self.vy = vy
        self.ax = ax # Acceleration selon les axes
        self.ay = ay
        self.img = img # Image de Tom


    def move(self, dt):
        # Modifie la vitesse et la position a partir du temps ecoulé depuis le dernier calcul
        self.centerx += self.vx * dt # variationx = vitesse * variation de temps
        self.centery -= self.vy * dt # ...
        self.vx += self.ax * dt # variation de vitesse = variation de temps * acceleration
        self.vy += self.ay * dt # ...



    def draw(self, win):
        # Les coordonnées d'une image sont celles du coin superieur gauche. Son centre est donc ximage = xcentre - largeurimage / 2, on utilise round car les coor
        # donnees doivent etre entieres
        # Affichage de l'image de Tom aux coordonnees, avec l'angle
        angle = atan(self.vy/self.vx) * 180 / 3.14 # Calcul de l'angle en degres par rapport au sol a partir de la derivée de la position: la vitesse
        rotated_img = pygame.transform.rotate(self.img, angle) # Rotation de l'image
        win.blit(rotated_img, (round(self.centerx - rotated_img.get_width()//2), round(self.centery - rotated_img.get_height()//2))) # Affichage de l'image


class Cannon:
    # Une representation du cannon
    def __init__(self, centerx, centery, head_img, canon_img, alpha):
        # Meme demarche que pour Tom
        self.centerx = centerx
        self.centery = centery
        self.head_img = head_img
        self.canon_img = canon_img
        self.alpha = alpha


    def draw(self, win):
        # Contrairement a Tom, le cannon est composé d'une base immobile et d'une partie superieur qui s'incline pour viser
        
        # Base
        leftx = self.centerx - self.canon_img.get_width() // 2
        topy = self.centery - self.canon_img.get_height() // 2

        win.blit(self.canon_img, (leftx, topy))
        # Head
        rotated_img = pygame.transform.rotate(self.head_img, self.alpha*180/3.14)
        topy2 = topy - rotated_img.get_height() # Comme la rotation se fait autour du sommet gauche, il faut ajuster l'altitude.
        leftx2 = leftx
        win.blit(rotated_img, (leftx2, topy2))


class Jerry:
    # Classe representant Jerry == le singe
    def __init__(self, centerx, centery, img, vx, vy, ax, ay):
        self.centerx = centerx
        self.centery = centery
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.img = img


    def move(self, dt):
        self.centerx += self.vx * dt
        self.centery -= self.vy * dt
        self.vx += self.ax * dt
        self.vy += self.ay * dt


    def draw(self, win):
        win.blit(self.img, (round(self.centerx - self.img.get_width()//2), round(self.centery - self.img.get_height()//2)))
