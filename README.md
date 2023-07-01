
# Simulations for Robot Kinematics on OpenCV

## Theory


### Forward kinematics:



Forward kinematics equations are based on angles by axis. Those equations give the location of robot's end by the angles of robot's movable joints. For every movable joint, robot's degree of freedom (DOF) can be found. For 2 movable joints its also called 2-DOF robot, for 3 mobable joints its also called 3-DOF robot. For every robot, there is a universal forward kinematics representation called D-H representation. Using the D-H representation for robots, we derive the equations.<br> 

To get the location of robot's end, we need the angles. Solving forward kinematics equations in terms of coordinates is called inverse kinematics.

### Inverse Kinematics:

Inverse kinematics equations are based on location of robot's end by the referance axes. Those equations give the joint angles by the location of robot's end. Solving forward kinematics in terms of coordinates will give the inverse kinematics equations. <br>

With inverse kinematics equations, we get values of joint angles for desired location of robot's end.

### Resources

#### https://www.mathworks.com/help/symbolic/derive-and-apply-inverse-kinematics-to-robot-arm.html
#### Introduction to Robotics: Analysis, Control, Applications (Saeed B. Niku)

