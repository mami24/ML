from math import *
import matplotlib.pyplot as plt

f=0.27
pa=1.6e6
b=0.04
r2=0.110**2

deg = []
tor = []

for i in range(90,140):
    x = i / 180 * pi
    tetha1=pi/2-(x/2)-(5.71*pi/180)
    tetha2=pi/2+(x/2)-(5.71*pi/180)
#tethaA=90 (sin90=1)

    T = 2*f*pa*b*r2*(cos(tetha1)-cos(tetha2)) / (sin(pi/2))
    deg.append(i)
    tor.append(T)


plt.plot(deg,tor,"b--")
plt.title("Torque Capacity vs Brake Angle")
plt.xlabel("deg")
plt.ylabel("Torque Capacity (N*m)")
plt.grid(True)
plt.legend()
plt.show()
