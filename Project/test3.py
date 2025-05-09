import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(-1, 1))
line, = ax.plot([], [], lw=2)

x_data, y_data = [],[]

def animate(i):
    x_data.append(i)
    y_data.append(random.random())
    line.set_data(x_data, y_data)
    return line,

ani = animation.FuncAnimation(fig, animate, frames=50, interval=10)
plt.show()