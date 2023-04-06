##THIS IS A BASIC SCRIPT FOR PLOTTING A TRAJECTORY OF A MOBILE ROBOT WITH INDIVIDUAL X,Y,THETA

## Importing required libraries
import numpy as np
import matplotlib.pyplot as plt

## Simulation Params
sampling_time = 0.1 #seconds
end_time = 10       #seconds
time_array = np.arange(0,end_time,sampling_time)

## Initial conditions
x0 = 0
y0 = 0
theta0 = 0
theta = 0

u = 0.3
v = 0.1
r = 0.2

eta, eta_dot = np.array([0,0,0]), np.array([0,0,0])
eta0 = np.array([x0, y0, theta0])
eta = np.vstack( (eta,eta0) )

zeta = np.array([u, v, r])

## SETTING THE PLOT FOR MATPLOTLIB
fig1 = plt.figure("Individual params",figsize=(6,6))
fig2 = plt.figure("MR_Trajectory", figsize=(6,6))

plt.ion()
plt.show()

for i in range(1, len(time_array)):
    theta = eta[-1, 2]
    jacobian = np.array([[np.cos(theta), -1*np.sin(theta), 0],
                        [np.sin(theta) ,    np.cos(theta), 0],
                        [             0,                0, 1]])
    eta_dot = np.vstack( (eta_dot,(jacobian.dot(zeta))) )
    #print(eta_dot[-1])
    eta = np.vstack( (eta,(eta[i]+(sampling_time*eta_dot[i])) ))
    #print(eta[0:i,1])
    
    ## Plotting function
    fig1.clf()
    fig2.clf()

    ax1 = fig1.add_subplot(1,1,1)
    ax1.plot(time_array[0:i],eta[0:i,0],'k-', label = 'x')
    ax1.plot(time_array[0:i],eta[0:i,1],'g-', label = 'y')
    ax1.plot(time_array[0:i],eta[0:i,2],'m-', label = 'theta')
    ax1.set_ylabel('params')
    ax1.set_xlabel('time')
    ax1.legend(loc='best')

    ax2 = fig2.add_subplot(1,1,1)
    ax2.plot(eta[0:i,0],eta[0:i,1],label = 'traj')
    ax2.set_ylabel('y')
    ax2.set_xlabel('x')
    ax2.legend(loc='best')

    plt.pause(0.1)
