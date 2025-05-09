# Introduction
This repository simulates the movement of 3 massive gravitational bodies in 2D space.

# Description
Using Newton's law of universal gravitation, we can model the movement of three gravitational bodies using the following three second-order differential equations for the acceleration of the three bodies:

$$\ddot{\mathbf{r_1}} = Gm_2\frac{\mathbf{r_2} - \mathbf{r_1}}{{\lvert \mathbf{r_2} - \mathbf{r_1} \rvert}^3} + Gm_3\frac{\mathbf{r_3} - \mathbf{r_1}}{{\lvert \mathbf{r_3} - \mathbf{r_1} \rvert}^3}$$

$$\ddot{\mathbf{r_2}} = Gm_3\frac{\mathbf{r_3} - \mathbf{r_2}}{{\lvert \mathbf{r_3} - \mathbf{r_2} \rvert}^3} + Gm_1\frac{\mathbf{r_1} - \mathbf{r_2}}{{\lvert \mathbf{r_1} - \mathbf{r_2} \rvert}^3}$$

$$\ddot{\mathbf{r_3}} = Gm_1\frac{\mathbf{r_1} - \mathbf{r_3}}{{\lvert \mathbf{r_1} - \mathbf{r_3} \rvert}^3} + Gm_2\frac{\mathbf{r_2} - \mathbf{r_3}}{{\lvert \mathbf{r_2} - \mathbf{r_3} \rvert}^3}$$

This simulation seeks to numerically integrate and animate the result using `matplotlib`.

## Installation
This section will describe how to download and run this simulation in Linux. This simulation requires the packages `numpy` and `matplotlib`. First, run the following command in the command terminal to ensure Python is installed: 
`python3 --version`.
Next, run the following commands to install `numpy` and `matplotlib`:
```
python3 -m pip install numpy
python3 -m pip install matplotlib
```


## Methods
This section will outline the mathematical methods used to simulate the 3-body problem.

$$\ddot{\mathbf{r_1}} = Gm_2\frac{\mathbf{r_2} - \mathbf{r_1}}{{\lvert \mathbf{r_2} - \mathbf{r_1} \rvert}^3} + Gm_3\frac{\mathbf{r_3} - \mathbf{r_1}}{{\lvert \mathbf{r_3} - \mathbf{r_1} \rvert}^3}$$

$$\ddot{\mathbf{r_2}} = Gm_3\frac{\mathbf{r_3} - \mathbf{r_2}}{{\lvert \mathbf{r_3} - \mathbf{r_2} \rvert}^3} + Gm_1\frac{\mathbf{r_1} - \mathbf{r_2}}{{\lvert \mathbf{r_1} - \mathbf{r_2} \rvert}^3}$$

$$\ddot{\mathbf{r_3}} = Gm_1\frac{\mathbf{r_1} - \mathbf{r_3}}{{\lvert \mathbf{r_1} - \mathbf{r_3} \rvert}^3} + Gm_2\frac{\mathbf{r_2} - \mathbf{r_3}}{{\lvert \mathbf{r_2} - \mathbf{r_3} \rvert}^3}$$

 Each $\ddot{\mathbf{r_n}}$ represents the position vectors for each of the three bodies. However, notice that each of these equations will blow up in proportion with $\frac{1}{r^3}$. This will cause problems when numerically integrating these equations as we will obtain very high acceleration values when this happens, causing numerical errors and animating problems. We therefore will insert a softening term $\epsilon$ and rewrite the equations as the following:

$$\ddot{\mathbf{r_1}} = Gm_2\frac{\mathbf{r_2} - \mathbf{r_1}}{({\lvert \mathbf{r_2} - \mathbf{r_1} \rvert^2 + \epsilon^2})^{1.5}} + Gm_3\frac{\mathbf{r_3} - \mathbf{r_1}}{({\lvert \mathbf{r_3} - \mathbf{r_1} \rvert^2 + \epsilon^2})^{1.5}}$$

$$\ddot{\mathbf{r_2}} = Gm_3\frac{\mathbf{r_3} - \mathbf{r_2}}{({\lvert \mathbf{r_3} - \mathbf{r_2} \rvert^2 + \epsilon^2})^{1.5}} + Gm_1\frac{\mathbf{r_1} - \mathbf{r_2}}{({\lvert \mathbf{r_1} - \mathbf{r_2} \rvert}^2 + \epsilon^2)^{1.5}}$$

$$\ddot{\mathbf{r_3}} = Gm_1\frac{\mathbf{r_1} - \mathbf{r_3}}{({\lvert \mathbf{r_1} - \mathbf{r_3} \rvert}^2 + \epsilon^2)^{1.5}} + Gm_2\frac{\mathbf{r_2} - \mathbf{r_3}}{({\lvert \mathbf{r_2} - \mathbf{r_3} \rvert}^2 + \epsilon^2)^{1.5}}$$


In the case of this particular simulation, $\epsilon = 0.01$. We want to use numerical methods to solve these three differential equations. We therefore can use a simple change of variables to write the above equations in the following form:
$$\mathbf{v_1} = \mathbf{\dot{\mathbf{r_1}}}$$

$$\mathbf{v_2} = \mathbf{\dot{\mathbf{r_2}}}$$

$$\mathbf{v_3} = \mathbf{\dot{\mathbf{r_3}}}$$

$$\mathbf{\dot{v_1}} = \mathbf{\ddot{\mathbf{r_1}}}$$

$$\mathbf{\dot{v_2}} = \mathbf{\ddot{\mathbf{r_2}}}$$

$$\mathbf{\dot{v_3}} = \mathbf{\ddot{\mathbf{r_3}}}$$

Each $\mathbf{v_n}$ in this equation represents the velocity of each object. We are now ready for numerical approximations.

This simulation numerically integrates these equations using the Runge-Kutta-Fehlberg method. The Runge-Kutta-Fehlberg method is different from other Runge-Kutte methods in that it has an adaptive step size built into its algorithm. An adaptive step size is important for this problem, as it will let our simulation run much faster than a fixed step size, as well as better approximations when each body moves closer together. The coefficients for the Runge-Kutta-Fehlberg method is given by the following equations:

$${\displaystyle {\begin{aligned}k_{1}&=h\cdot f(x+A(1)\cdot h,y)\\k_{2}&=h\cdot f(x+A(2)\cdot h,y+B(2,1)\cdot k_{1})\\k_{3}&=h\cdot f(x+A(3)\cdot h,y+B(3,1)\cdot k_{1}+B(3,2)\cdot k_{2})\\k_{4}&=h\cdot f(x+A(4)\cdot h,y+B(4,1)\cdot k_{1}+B(4,2)\cdot k_{2}+B(4,3)\cdot k_{3})\\k_{5}&=h\cdot f(x+A(5)\cdot h,y+B(5,1)\cdot k_{1}+B(5,2)\cdot k_{2}+B(5,3)\cdot k_{3}+B(5,4)\cdot k_{4})\\k_{6}&=h\cdot f(x+A(6)\cdot h,y+B(6,1)\cdot k_{1}+B(6,2)\cdot k_{2}+B(6,3)\cdot k_{3}+B(6,4)\cdot k_{4}+B(6,5)\cdot k_{5})\end{aligned}}}$$

where each $A(n)$ and $B(l,m)$ values represent certain coefficients. Likewise,

$${\displaystyle y(x+h)=y(x)+CH(1)\cdot k_{1}+CH(2)\cdot k_{2}+CH(3)\cdot k_{3}+CH(4)\cdot k_{4}+CH(5)\cdot k_{5}+CH(6)\cdot k_{6}}$$

We can then calculate our new step size $dt_{new}$ with the following two eqautions:

$${\displaystyle \mathrm {TE} =\left|\mathrm {CT} (1)\cdot k_{1}+\mathrm {CT} (2)\cdot k_{2}+\mathrm {CT} (3)\cdot k_{3}+\mathrm {CT} (4)\cdot k_{4}+\mathrm {CT} (5)\cdot k_{5}+\mathrm {CT} (6)\cdot k_{6}\right|}$$


$${\displaystyle h_{\text{new}}=0.9\cdot h\cdot \left({\frac {\varepsilon }{TE}}\right)^{1/5}}$$

Again, we have each $CH(i)$ and $CT(j)$ representing more RKF45 coefficients and $\epsilon$ representing an arbitrary tolerance value. Each of these equations were taken directly from the Wikipedia page about [Runge-Kutta-Fehlberg](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta%E2%80%93Fehlberg_method). The coefficients used in this simulation also come from Wikipedia, specifically from the second coefficient table in the article. 


