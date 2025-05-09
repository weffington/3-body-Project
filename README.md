# Simulation of the 3-body Problem
## Introduction
The 3-body problem is perhaps one of the most famous problems in physics. This repository simulates this problem using numerical methods in Python.

## Description
Using Newton's law of universal gravitation, we can model the movement of three gravitational bodies using the following three second-order differential equations for the acceleration of the three bodies:

$$\ddot{\mathbf{r_1}} = Gm_2\frac{\mathbf{r_2} - \mathbf{r_1}}{{\lvert \mathbf{r_2} - \mathbf{r_1} \rvert}^3} + Gm_3\frac{\mathbf{r_3} - \mathbf{r_1}}{{\lvert \mathbf{r_3} - \mathbf{r_1} \rvert}^3}$$

$$\ddot{\mathbf{r_2}} = Gm_3\frac{\mathbf{r_3} - \mathbf{r_2}}{{\lvert \mathbf{r_3} - \mathbf{r_2} \rvert}^3} + Gm_1\frac{\mathbf{r_1} - \mathbf{r_2}}{{\lvert \mathbf{r_1} - \mathbf{r_2} \rvert}^3}$$

$$\ddot{\mathbf{r_3}} = Gm_1\frac{\mathbf{r_1} - \mathbf{r_3}}{{\lvert \mathbf{r_1} - \mathbf{r_3} \rvert}^3} + Gm_2\frac{\mathbf{r_2} - \mathbf{r_3}}{{\lvert \mathbf{r_2} - \mathbf{r_3} \rvert}^3}$$

In this particular simulation, each body has the same mass and $G=0.5$.
This simulation numerically integrates and animates these equations using `matplotlib` and `numpy`.

## Installation
This section will describe how to download and run this simulation in Linux. This simulation requires the packages `numpy` and `matplotlib`. First, run the following command in the command terminal to ensure Python is installed: 
`python3 --version`.
Next, run the following commands to install `numpy` and `matplotlib`:
```
python3 -m pip install numpy
python3 -m pip install matplotlib
```
Next, navigate to a desired directory and clone the repository using the following git command:

```
git clone https://github.com/weffington/3-body-Project
```

Finally, navigate to the Simulation directory.

## Usage
This project uses a test simulation with predefined initial positions and velocities. To run the test simulation, enter 
```
chmod +x runtest.sh
./runtest.sh
```

into the command line. This test file is used to ensure the simulation works properly. Run this test before running the simulation. What you should see is described below.

To run the actual simulation, enter the following commands:
```
chmod +x runsim.sh
./runsim.sh
```
What you should see is described below.
You will get the following prompt in the command terminal:
```
Enter position coordinates for each body (e.g. (2,2),(3,3),(4,4)):
```
This prompt is asking you for the initial xy positions for each of the three bodies. Enter the xy positions in the exact form listed in the example in the prompt. For example:
```
Enter position coordinates for each body (e.g. (2,2),(3,3),(4,4)):
(1,2),(2,3),(4,1)
``` 
After entering the xy positions, you will get another prompt:
```
Enter velocity vectors in the same form (e.g. (1,0),(2,0),(0,0)):
```
This prompt is asking for the initial 2d velocity vectors in the same format as the initial positions. Enter them. For example:
```
Enter velocity vectors in the same form (e.g. (1,0),(2,0),(0,0)):
(2,2),(1,0),(1,1)
```
You will then see a window pop up on your screen showing an animation of the 3-body simulation. This is a live animation of the paths of the three bodies. The x and y axes scale as the bodies move to keep each of the three objects in view. A video demonstrating this process is available in the repository

It is worth noting that the animation will slow down as each object gets closer to one another. This is due to using a numerical algorithm that has an adaptive step size. When each object gets closer together, the time step will decrease to increase precision, slowing the animation down in the process. This adaptive step size process is described below in the following section.

To stop the animation, simply close the popup window.

## Methods
This section will outline the mathematical and coding methods used to simulate the 3-body problem. As stated above, the three body problem can be modeled with the following equations:

$$\ddot{\mathbf{r_1}} = Gm_2\frac{\mathbf{r_2} - \mathbf{r_1}}{{\lvert \mathbf{r_2} - \mathbf{r_1} \rvert}^3} + Gm_3\frac{\mathbf{r_3} - \mathbf{r_1}}{{\lvert \mathbf{r_3} - \mathbf{r_1} \rvert}^3}$$

$$\ddot{\mathbf{r_2}} = Gm_3\frac{\mathbf{r_3} - \mathbf{r_2}}{{\lvert \mathbf{r_3} - \mathbf{r_2} \rvert}^3} + Gm_1\frac{\mathbf{r_1} - \mathbf{r_2}}{{\lvert \mathbf{r_1} - \mathbf{r_2} \rvert}^3}$$

$$\ddot{\mathbf{r_3}} = Gm_1\frac{\mathbf{r_1} - \mathbf{r_3}}{{\lvert \mathbf{r_1} - \mathbf{r_3} \rvert}^3} + Gm_2\frac{\mathbf{r_2} - \mathbf{r_3}}{{\lvert \mathbf{r_2} - \mathbf{r_3} \rvert}^3}$$

The denominators in each of these three equations will be problematic when coding the simulation, as each equation will blow up as the three bodies get closer together. To get around this, we insert a softening term $\epsilon$ into the denominators:

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

This simulation numerically integrates these equations using the Runge-Kutta-Fehlberg (RKF45) method. The Runge-Kutta-Fehlberg method is different from other Runge-Kutte methods in that it has an adaptive step size built into its algorithm. An adaptive step size is important for this problem, as it will let our simulation run much faster than a fixed step size, as well as better approximations when each body moves closer together. The equation for an RK45 step is given by the following:

$${\displaystyle y(x+h)=y(x)+CH(1)\cdot k_{1}+CH(2)\cdot k_{2}+CH(3)\cdot k_{3}+CH(4)\cdot k_{4}+CH(5)\cdot k_{5}+CH(6)\cdot k_{6}}$$

Each $k_n$ term in the equation represents specific calculated coefficients for RKF45. We can then calculate our new step size $h_{new}$ with the following two equations:

$${\displaystyle \mathrm {TE} =\left|\mathrm {CT} (1)\cdot k_{1}+\mathrm {CT} (2)\cdot k_{2}+\mathrm {CT} (3)\cdot k_{3}+\mathrm {CT} (4)\cdot k_{4}+\mathrm {CT} (5)\cdot k_{5}+\mathrm {CT} (6)\cdot k_{6}\right|}$$


$${\displaystyle h_{\text{new}}=0.9\cdot h\cdot \left({\frac {\varepsilon }{TE}}\right)^{1/5}}$$

Again, we have each $CH(i)$ and $CT(j)$ representing more RKF45 coefficients and $\epsilon$ representing an arbitrary tolerance value. Each of these equations were taken directly from the Wikipedia page about [Runge-Kutta-Fehlberg](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta%E2%80%93Fehlberg_method). The coefficients used in this simulation also come from Wikipedia, specifically from the second coefficient table listed in the article. This article also shows the equations for each $k$ term. Using these methods, we can simulate the 3-body problem by repeatedly applying RK45 steps.

## Licensing
This project is licensed under MIT.

## Acknowledgements
Special thanks to the [Runge-Kutta-Fehlberg](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta%E2%80%93Fehlberg_method) Wikipedia article for help with my Runge-Kutta-Fehlberg algorithm.


