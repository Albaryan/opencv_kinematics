
# A Simulation for 2-DOF Robot Kinematics on OpenCV

## Demo

![untitled](https://github.com/Albaryan/opencv_kinematics/assets/104989834/7a6a0f93-d2b2-4e76-beca-e36d5d483c59)

## How to Use

Use x and y trackbars to change the location of robot's end.\
Press c to change between solution 1 and solution 2.

## Theory

### Forward kinematics:

![forwardgraph](https://github.com/Albaryan/opencv_kinematics/assets/104989834/e1b0b9e9-11c1-4016-b410-d87c598e76de)

Forward kinematics equations are based on angle of L1 by x axis (theta 1) and angle of L2 by the normal of L1 (theta 2). Those equations give the location of robot's end by the angles of robot's movable joints. For every movable joint, robot's degree of freedom (DOF) can be found. Since this robot has 2 movable joints, its also called 2-DOF robot. For every robot, there is a universal forward kinematics representation called D-H representation. Using the D-H representation for 2-DOF robot, we derive the formula below.

![forward](https://github.com/Albaryan/opencv_kinematics/assets/104989834/f2fb96e5-8225-4e98-a93b-54fb6218136e)

To get the location of robot's hand, we need the theta 1 and theta 2 angles. Solving forward kinematics equations in terms of x and y coordinates is called inverse kinematics.

### Inverse Kinematics:

Inverse kinematics equations are based on location of robot's end by the referance axes. Those equations give the joint angles by the location of robot's end. Solving forward kinematics in terms of x and y coordinates will give the inverse kinematics equations. As a result, we derive the formula below. 


![inverse](https://github.com/Albaryan/opencv_kinematics/assets/104989834/68322e7f-1f20-4781-bb8e-221e95d0c3ca)

With inverse kinematics equations, we get values of joint angles for desired location of robot's end. As you can see there is two possible solutions for inverse kinematics equations.

### Solutions:

Two different solutions can simply reffered as inner solution and outer solution. For inner solution, the joint angle theta 2 is lower than zero. For outer solution, the joint angle theta 2 is bigger than zero. So, column 1 of inverse kinematics equation is inner solution and column 2 is outer solution.

![Screenshot from 2023-06-25 16-20-24](https://github.com/Albaryan/opencv_kinematics/assets/104989834/cbe4af48-3119-4abd-b151-572c88347e08)

![Screenshot from 2023-06-25 16-20-32](https://github.com/Albaryan/opencv_kinematics/assets/104989834/f44d3499-5d92-436a-969c-ac786090bf06)

## Resources

https://www.mathworks.com/help/symbolic/derive-and-apply-inverse-kinematics-to-robot-arm.html
Introduction to Robotics: Analysis, Control, Applications (Saeed B. Niku)



