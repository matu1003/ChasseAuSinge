import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import atan, cos, sin
import numpy as np

t = 0 # Date de debut en secondes
d = 1600 # Distance L au singe
h = 200 # Hauteur du singe
v0 = 450 # Vitesse initiale
g = 9.81 # Constante gravitationnelle
alpha = atan(h/d) # Calcul de l'angle de tir
duree = d/(v0*cos(alpha)) # Durée du modèle: lorsque xsinge < xballe

# Generation des courbes selon les equations avec 100 positions par seconde
xballe = [v0*cos(alpha)*i for i in np.linspace(0, duree, int(duree*100))]
yballe = [v0*sin(alpha)*i-g*i**2 for i in np.linspace(0, duree, int(duree*100))]
xsinge = [d for i in np.linspace(0, duree, int(duree*100))]
ysinge = [h-g*i**2 for i in np.linspace(0, duree, int(duree*100))]
j = 0

def animate(i):
  # A chaque etape, on prend un element de plus de la liste pour l'afficher sur la courbe
  global j
  plt.plot(xballe[:j], yballe[:j], c='b')
  plt.plot(xsinge[:j], ysinge[:j], c='r')  
  j+=1

ani = animation.FuncAnimation(plt.gcf(), animate, interval=10)

plt.show()
