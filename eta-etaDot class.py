import numpy as np
import math

class eta:

    def circular(self, radius, omega, time):
        self.circular = np.array([ [radius*np.cos(omega*time)],
                                   [radius*np.sin(omega*time)],
                                   [(omega*time) + (np.pi/2) ] ])
        return self.circular

    def linear(self, velocity, x, time):
        self.linear   = np.array([ [(velocity*x[0]/math.sqrt(x[0]*2+x[1]**2))*time],
                                   [(velocity*x[1]/math.sqrt(x[0]*2+x[1]**2))*time],
                                   [0] ])
        return self.linear
    
    def sine(self, omega, time): 
        sine     = np.array([ [omega*time],
                                   [np.sin(omega*time)],
                                   [math.atan(np.cos(omega*time))] ])
        return sine

    def infinty(self,):
        self.infinity = np.array([ [],
                                   [],
                                   [] ])
        return self.infinty

class etaDot:

    def circular(self, radius, omega, time):
        self.circular = np.array([ [ radius*omega*np.cos(omega*time)],
                                   [-radius*omega*np.sin(omega*time)],
                                   [ omega                          ] ])
        return self.circular

    def linear(self, velocity, x):
        self.linear   = np.array([ [(velocity*x[0]/math.sqrt(x[0]*2+x[1]**2))],
                                   [(velocity*x[1]/math.sqrt(x[0]*2+x[1]**2))],
                                   [0] ])
        return self.linear
    
    def sine(self, omega, time): 
        sine     = np.array([ [omega],
                                   [omega*np.cos(omega*time)],
                                   [-(omega*np.sin(omega*time))/(1+pow(np.cos(omega*time),2))] ])
        return sine

    def infinty(self,):
        self.infinity = np.array([ [],
                                   [],
                                   [] ])
        return self.infinty


if __name__ == "__main__":
    etaDesired = eta()
    etaDotDesired = etaDot()
    for i in range(0,5):
        x = etaDesired.sine(0.3,i)
        y = etaDotDesired.sine(0.3,i)
        print(x,y)
