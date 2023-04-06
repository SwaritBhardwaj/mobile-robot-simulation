# Mobile-Robot-Simulation
In this repository you will see files implementing forward and inverse kinnematics for monile robots, more particularly differential drive.

## Dependencies

 - pip install numpy
 - pip install matplotlib
 
## Exploring files
 - 1.basic_simulation(forward_kinematics).py : *will simulate a trajectory of a presumed mobile robot with initial velocity states of [u, v, r].*  
 - 2.bot+traj_sim(forward_kinematics).py :  *will simulate a trajectory of an actual mobile robot with initial velocity states of [u, v, r].* 
 - 3.inverse_kinematics_trajectory.py : *will simulate a trajectory of a mobile robot by computing velocity states of [u, v, r] given the desired states.*
 - 4.lineOFsight(inverse_kinematics).py: *simulates path planning of a mobile robot by computing velocity states of [u, v, r] given the desired position and heading*
 - eta-etaDot_class.py: *contains code for various trajectory models that can be tinkered with.* 

