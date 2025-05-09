import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from numpy import array
from functions import rkf45_step

#initial dt
dt=1e-2

#initial pos. and vel. vectors
rvals = array([[-1,0],[1,0],[0,np.sqrt(3)]])
vvals = array([[0,0],[0,0],[0,0]])

#current r matrix
r_n = np.append(rvals,vvals,axis=0)

#initial t
t_now = 0

#store r matrices
rvals=array([r_n])

#set up plot
fig, ax = plt.subplots(figsize=(10,6))
ax.grid()
ax.set_xticks([])
ax.set_yticks([])

#plot mass shapes and trajectory lines
m1,= ax.plot([],[],'ro',markersize=7)
m2,= ax.plot([],[],'bo',markersize=7)
m3,= ax.plot([],[],'go',markersize=7)

line1, = ax.plot([], [], 'r-', lw=1)
line2, = ax.plot([], [], 'b-', lw=1)
line3, = ax.plot([], [], 'g-', lw=1)

#create animation
def animate(i):
    global r_n, dt, t_now, rvals

    #perform Runge-Kutta-Fehlberg steps
    r_n, dt = rkf45_step(r_n,dt)

    t_now += dt
    rvals = np.append(rvals, [r_n], axis=0)

    #get x and y positions for each mass
    r1, r2, r3 = r_n[0], r_n[1], r_n[2]
    r1x, r1y = r1
    r2x, r2y = r2
    r3x, r3y = r3

    #keep masses in view
    ax.set_xlim(min(r1x-5,r2x-5,r3x-5),max(r1x+5,r2x+5,r3x+5))
    ax.set_ylim(min(r1y-5,r2y-5,r3y-5),max(r1y+5,r2y+5,r3y+5))

    rvals_arr = array(rvals)

    #set mass and trajectory data
    m1.set_data([r1x], [r1y])
    m2.set_data([r2x], [r2y])
    m3.set_data([r3x], [r3y])

    rvals_arr = np.array(rvals)
    line1.set_data(rvals_arr[:,0,0], rvals_arr[:,0,1])
    line2.set_data(rvals_arr[:,1,0], rvals_arr[:,1,1])
    line3.set_data(rvals_arr[:,2,0], rvals_arr[:,2,1])

    
    return m1, m2, m3, line1, line2, line3

animation = ani.FuncAnimation(fig=fig, func=animate,
                          interval=5, blit=True, cache_frame_data=False)

plt.show()
plt.close()

