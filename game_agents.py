import pygame
from math import sin, cos, atan

class Tom:
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
        angle = atan(self.vy/self.vx) * 180 / 3.14
        print(angle)
        rotated_img = pygame.transform.rotate(self.img, angle)
        win.blit(rotated_img, (round(self.centerx - rotated_img.get_width()//2), round(self.centery - rotated_img.get_height()//2)))


class Cannon:
    def __init__(self, centerx, centery, head_img, canon_img, alpha):
        self.centerx = centerx
        self.centery = centery
        self.head_img = head_img
        self.canon_img = canon_img
        self.alpha = alpha


    def draw(self, win):
        # Base
        leftx = self.centerx - self.canon_img.get_width() // 2
        topy = self.centery - self.canon_img.get_height() // 2

        win.blit(self.canon_img, (leftx, topy))
        # Head
        rotated_img = pygame.transform.rotate(self.head_img, self.alpha*180/3.14)
        y_offset = 0
        topy2 = topy - rotated_img.get_height()
        leftx2 = leftx
        win.blit(rotated_img, (leftx2, topy2))


class Jerry:
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
