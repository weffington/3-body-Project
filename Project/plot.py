import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np
file="3body.txt"
data=np.loadtxt(file,skiprows=1)
t,r1x,r1y,r2x,r2y,r3x,r3y=data.T
fig,ax=plt.subplots(figsize=(6,6))
ax.set_ylim(-10,10)
ax.set_xlim(-10,10)
m1,= ax.plot([],[],'ro',markersize=5)
m2,= ax.plot([],[],'bo',markersize=7)
m3,= ax.plot([],[],'go',markersize=9)

line1, = ax.plot([], [], 'r-', lw=1)
line2, = ax.plot([], [], 'b-', lw=1)
line3, = ax.plot([], [], 'g-', lw=1)


def init():
    m1.set_data([], [])
    m2.set_data([], [])
    m3.set_data([], [])
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return m1, m2, m3, line1, line2, line3

def update(frame):
    # Update current positions
    m1.set_data([r1x[frame]], [r1y[frame]])
    m2.set_data([r2x[frame]], [r2y[frame]])
    m3.set_data([r3x[frame]], [r3y[frame]])

    # Update trajectory lines
    line1.set_data(r1x[:frame+1], r1y[:frame+1])
    line2.set_data(r2x[:frame+1], r2y[:frame+1])
    line3.set_data(r3x[:frame+1], r3y[:frame+1])

    return m1, m2, m3, line1, line2, line3

interval = 5
ani = ani.FuncAnimation(fig=fig, func=update, init_func=init,
                        frames=len(t), interval=interval, blit=True)
plt.show()

def animate(i):
    global r_n, dt, t_now, tvals, rvals
    r_n, dt = rkf45_step(r_n,dt)

    t_now += dt
    tvals=np.append(tvals,t_now)
    rvals = np.append(rvals, [r_n], axis=0)

    
    r1, r2, r3 = r_n[0], r_n[1], r_n[2]
    r1x, r1y = r1
    r2x, r2y = r2
    r3x, r3y = r3

    rvals_arr = array(rvals)

    m1.set_data([r1x], [r1y])
    m2.set_data([r2x], [r2y])
    m3.set_data([r3x], [r3y])

    rvals_arr = np.array(rvals)
    line1.set_data(rvals_arr[:,0,0], rvals_arr[:,0,1])
    line2.set_data(rvals_arr[:,1,0], rvals_arr[:,1,1])
    line3.set_data(rvals_arr[:,2,0], rvals_arr[:,2,1])

    return m1, m2, m3, line1, line2, line3

animation = ani.FuncAnimation(fig=fig, func=animate,
                          interval=5, blit=True)


plt.show()