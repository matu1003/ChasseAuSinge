import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import atan, cos, sin
import numpy as np

t = 0
d = 1600
h = 200
v0 = 450
g = 9.81
alpha = atan(h/d)
duree = d/(v0*cos(alpha))


xballe = [v0*cos(alpha)*i for i in np.linspace(0, duree, int(duree*100))]
yballe = [v0*sin(alpha)*i-g*i**2 for i in np.linspace(0, duree, int(duree*100))]
xsinge = [d for i in np.linspace(0, duree, int(duree*100))]
ysinge = [h-g*i**2 for i in np.linspace(0, duree, int(duree*100))]
j = 0

def animate(i):
  global j
  plt.plot(xballe[:j], yballe[:j], c='b')
  plt.plot(xsinge[:j], ysinge[:j], c='r')  
  j+=1

ani = animation.FuncAnimation(plt.gcf(), animate, interval=10)

plt.show()