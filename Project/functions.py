import numpy as np
from numpy import linalg

'''
obtained rkf45 algorithm 
from https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta%E2%80%93Fehlberg_method
'''

def equations(r, G=1 ,m_1=100, m_2=100, m_3=100):

    #position and velocity vectors
    r_1,r_2,r_3,v_1,v_2,v_3=r

    #velocity eqns
    fr_1=v_1
    fr_2=v_2
    fr_3=v_3

    #vector differences
    delta_1=r_2-r_1
    delta_2=r_3-r_1
    delta_3=r_3-r_2

    #softening term
    epsilon = 1e-2

    #compute norms with softening terms
    distance_1=(linalg.norm(delta_1)**2 + epsilon**2)**1.5
    distance_2=(linalg.norm(delta_2)**2 + epsilon**2)**1.5
    distance_3=(linalg.norm(delta_3)**2 + epsilon**2)**1.5

    #acceleration eqns
    fv_1=(G*m_2*((delta_1)/(distance_1)) +
    G*m_3*((delta_2)/(distance_2)))

    fv_2=(G*m_3*((delta_3)/(distance_3)) +
    G*m_1*((-delta_2)/(distance_2)))

    fv_3=(G*m_1*((-delta_2)/(distance_2)) +
    G*m_2*((-delta_3)/(distance_3)))
    
    return np.array([fr_1,fr_2,fr_3,fv_1,fv_2,fv_3])

def rkf45_step(r, dt, G=0.5 ,m_1=100, m_2=100, m_3=100, tol=1e-6, dt_max=1e-2, dt_min=1e-6):
    #runge-kutta-fehlberg
    while True:
        #calculate k values
        k1 = dt * equations(r,G,m_1,m_2,m_3)
        k2 = dt * equations(r + (1/4)*k1, G ,m_1, m_2, m_3)
        k3 = dt * equations(r + (3/32)*k1 + (9/32)*k2, G ,m_1, m_2, m_3)
        k4 = dt * equations(r + (1932/2197)*k1 + (-7200/2197)*k2 + (7296/2197)*k3, G ,m_1, m_2, m_3)
        k5 = dt * equations(r + (439/216)*k1 + (-8)*k2 + (3680/513)*k3 +
                        (-845/4104)*k4, G ,m_1, m_2, m_3)
        k6 = dt * equations(r + (-8/27)*k1 + 2*k2 + (-3544/2565)*k3 +
                      (1859/4104)*k4 + (-11/40)*k5, G ,m_1, m_2, m_3)
        
        #compute next r value
        r_next = (r + (16/135)*k1 + (6656/12825)*k3 + (6656/12825)*k4 - 
             (9/50)*k5 + (2/55)*k6)
        
        #error term
        TE = ((-1/360)*k1 + (128/4275)*k3 + (2197/75240)*k4 - 
          (1/50)*k5 - (2/55)*k6)
        r_error = linalg.norm(TE)

        #adaptive time step
        #use dt_max to avoid sudden time jumps
        #use dt_min to avoid very small time steps

        if r_error>=tol:
            dt = max(dt_min, 0.9 * dt * (tol/r_error)**0.2)
        
        else:
            dt = min(dt_max, 0.9 * dt * (tol/r_error)**0.25)
            if dt<dt_min:
                dt = dt_min
                break
            r = r_next
            break

    return r, dt