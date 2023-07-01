
# A Simulation for 2-DOF Robot Kinematics on OpenCV

## Demo

![untitled](https://github.com/Albaryan/opencv_kinematics/assets/104989834/7a6a0f93-d2b2-4e76-beca-e36d5d483c59)

## How to Use

Use x and y trackbars to change the location of robot's end.\
Press c to change between solution 1 and solution 2.

## Theory

![forwardgraph](https://github.com/Albaryan/opencv_kinematics/assets/104989834/e1b0b9e9-11c1-4016-b410-d87c598e76de)

### Forward kinematics:

![forward](https://github.com/Albaryan/opencv_kinematics/assets/104989834/f2fb96e5-8225-4e98-a93b-54fb6218136e)

### Inverse Kinematics:

![inverse](https://github.com/Albaryan/opencv_kinematics/assets/104989834/68322e7f-1f20-4781-bb8e-221e95d0c3ca)

### Solutions:

Two different solutions can simply reffered as inner solution and outer solution. For inner solution, the joint angle theta 2 is lower than zero. For outer solution, the joint angle theta 2 is bigger than zero. So, column 1 of inverse kinematics equation is inner solution and column 2 is outer solution.

![Screenshot from 2023-06-25 16-20-24](https://github.com/Albaryan/opencv_kinematics/assets/104989834/cbe4af48-3119-4abd-b151-572c88347e08)

![Screenshot from 2023-06-25 16-20-32](https://github.com/Albaryan/opencv_kinematics/assets/104989834/f44d3499-5d92-436a-969c-ac786090bf06)


