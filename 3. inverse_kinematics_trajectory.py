import numpy as np
import matplotlib.pyplot as plt

## INITIAL LOCALIZATION CONDITIONS
x,y,theta = 0,0,0
p = np.array([x,y,theta])
width = 285/1000
wheel_diameter = 65/1000

## INITIAl SIMULATION CONDITIONS
x0,y0,theta0 = 0,0,0
theta = 0
eta, eta_dot = np.array([0,0,0]), np.array([0,0,0])
eta0 = np.array([x0, y0, theta0])
eta = np.vstack((eta,eta0))

sampling_time = 0.1 #seconds
end_time = 10       #seconds
time_array = np.arange(0,end_time,sampling_time)

error = []
error_x = []
error_y = []

rho = 3.0
revolutions = 1
omega_circle = revolutions*2*np.pi/end_time

pos_desired = np.array([None,None,None])

## MATPLOTLIB PLOT SETTING
MR_TRAJ = plt.figure("MR_TRAJECTORY", figsize = (6,6))
Error = plt.figure("ERROR", figsize = (6,6))
##rps = plt.figure("RPS", figsize = (6,6))

## INITIALIZING FOR REAL TIME
plt.ion()
plt.show()

for i in range(0,len(time_array)):

    MR_TRAJ.clf()
    Error.clf()
##    rps.clf()
    
    jacobian = np.array([[np.cos(theta), -np.sin(theta), 0],
                         [ np.sin(theta),  np.cos(theta), 0],
                         [             0,              0, 1]])

    ## CALCULATING THE DESIRED POSITIONS AND DERIVATIVES OF SAME
    eta_desired = np.array([[rho*np.cos(omega_circle*time_array[i])],
                            [rho*np.sin(omega_circle*time_array[i])],
                            [np.pi/2 - omega_circle*time_array[i]]])

    eta_dot_desired = np.array([[-rho*np.sin(omega_circle*time_array[i])*omega_circle],
                                [ rho*np.cos(omega_circle*time_array[i])*omega_circle],
                                [omega_circle]])
    
#    print(eta_desired[0,0],eta_desired[1,0])
    
    pos_desired = np.vstack((pos_desired, eta_desired.T))
    zeta_desired = np.linalg.inv(jacobian).dot(eta_dot_desired)
    ## CALCULATING RPS FROM DESIRED VELOCITIES
    rps_l_desired = (2/wheel_diameter)*(zeta_desired[0] - (zeta_desired[2]*width/2))
    rps_r_desired = (2/wheel_diameter)*(zeta_desired[0] + (zeta_desired[2]*width/2))
    
    print(rps_l_desired, rps_r_desired)
    
    ## USE FORWARD K AND CALCULATE ERROR B/W THEM
    eta_dot = np.vstack((eta_dot, (jacobian.dot(eta_dot_desired)).T))
    eta = np.vstack((eta, eta[-1]+(sampling_time*eta_dot[-1])))
    error.append((eta_desired.T - eta[-1]))#.reshape(3))
    error_x.append(error[-1][0][0])
    error_y.append(error[-1][0][1])
##    print(error[-1][0][0])

    
    ## PLOTTING THE GRAPHS
    ax1 = MR_TRAJ.add_subplot(1,1,1)
    ax1.plot(pos_desired[:i,0], pos_desired[:i,1],'g:', label = 'traj')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_xlim(-rho-0.5,rho+0.5)
    ax1.set_ylim(-rho-0.5,rho+0.5)
    ax1.legend(loc = 'best')

    ax2 = Error.add_subplot(1,1,1)
    ax2.plot(error_x[:i], time_array[:i], label = "error_x")
    ax2.plot(error_y[:i], time_array[:i], label = "error_y")
    ax2.set_xlabel('time')
    ax2.set_ylabel('error')
    ax2.legend(loc = 'best')
    
    plt.pause(0.01)
