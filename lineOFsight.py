import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import *

## SIMULATION PARAMETERS
samplingTime=0.1
endTime=10
timeArray=np.arange(0,endTime,samplingTime)
## CONDITIONS
eta=np.array([[0,0,0]])
etaDesired=[-4.5,-4.4,np.pi/2]
K_u = 0.5
K_r = -0.8
Kx,Ky,Kpsi = 2-0.5,2-0.5,20-5
## BOT GEOMETERY
wheelRadius = 0.00325
robotWidth  = 0.0284
robotLength = 0.028
roboCoord = 5*np.array([[-robotLength/2, robotLength/2, robotLength/2, -robotLength/2],
                        [-robotWidth/2 , -robotWidth/2, robotWidth/2 ,  robotWidth/2 ]])
casterCoord = np.array([[],
                        []])
## MATPLOTLIB PLOT
Simulation=plt.figure("Simulation", figsize = (6,6))
plt.ion()
plt.show()
for i in range(0,len(timeArray)):
    Simulation.clf()
    rho = np.sqrt((etaDesired[0]-eta[i,0])**2 + (etaDesired[1]-eta[i,1])**2)
    error = [etaDesired[0],etaDesired[1],np.arctan2(etaDesired[1]-eta[i,1],etaDesired[0]-eta[i,0])] - eta[i]
    
    if rho < 0.2:
        error = etaDesired-eta[i]
##        error = 0*error

    psi = eta[i,2]
    jacobian = np.array([[np.cos(psi),-np.sin(psi),0],
                         [np.sin(psi), np.cos(psi),0],
                         [       0,        0,1]])
    zetaDesired = np.linalg.inv(jacobian).dot(np.diag([Kx,Ky,Kpsi]).dot(error))
    zetaDesired[0],zetaDesired[1],zetaDesired[2]=K_u*zetaDesired[0],0,-1*K_r*zetaDesired[2]
    eta = np.vstack((eta, eta[i]+(1-np.exp(-timeArray[i]))*(samplingTime*jacobian.dot(zetaDesired))))                                                                             

    roboTransform = np.array([[np.cos(psi), -np.sin(psi)],
                               [np.sin(psi),  np.cos(psi)]])
    
    roboSimulCoord = roboTransform.dot(roboCoord)
    roboSimulCoord = roboSimulCoord + np.array([[eta[i-1,0]],[eta[i-1,1]]])
    bot = Polygon([[roboSimulCoord[0,0],roboSimulCoord[1,0]],
                   [roboSimulCoord[0,1],roboSimulCoord[1,1]],
                   [roboSimulCoord[0,2],roboSimulCoord[1,2]],
                   [roboSimulCoord[0,3],roboSimulCoord[1,3]]], closed = True, fc = 'lime',ec ='black', label = 'bot')
    desiredLocation=Circle((etaDesired[0],etaDesired[1]),0.2, ls="--",fill = 0,ec="blue",label="desired position")
    
    simulation=Simulation.add_subplot(1,1,1)
    simulation.add_patch(bot)
    simulation.add_patch(desiredLocation)
    simulation.plot(etaDesired[0],etaDesired[1],color="blue",label="desired position")
    simulation.plot(eta[:i,0],eta[:i,1],"r--",label="bot")
    simulation.set_xlabel("x")
    simulation.set_ylabel("y")
    simulation.legend()
    
    plt.pause(0.001)
    print(error, '\t', eta[-1])
    
