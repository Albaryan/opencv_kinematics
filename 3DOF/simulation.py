import math
import cv2
import numpy as np

global L
L=200
origin=(500,500)

def calculate_angles(x,y,z):
    t1=math.atan2(z,x)
    t2=math.atan2(y,math.sqrt(x**2 + z**2)) + math.atan2(math.sqrt(4*(L**2)*(x**2 + y**2 + z**2) - (x**2 + y**2 + z**2)**2),
                                                             math.sqrt(x**2 + y**2 + z**2)**2) 
    t3=2*math.atan2(math.sqrt(4*(L**2)*(x**2 + y**2 + z**2) - (x**2 + y**2 + z**2)**2),
                                                             math.sqrt(x**2 + y**2 + z**2)**2)
    
    return t1,t2,-t3

def x_change(x0):
    global x
    x=x0

def y_change(y0):
    global y
    y=y0

def z_change(z0):
    global z
    z=z0

x=0
y=0
z=0

cv2.namedWindow("Simulation",cv2.WINDOW_NORMAL)

cv2.createTrackbar("X","Simulation",200,400,x_change)
cv2.createTrackbar("Y","Simulation",200,400,y_change)
cv2.createTrackbar("Z","Simulation",0,400,z_change)
cv2.setTrackbarMin("Z","Simulation",-400)

cv2.resizeWindow("Simulation", 750, 750)

while True:
    image1=np.zeros((1000,1000),np.uint8)
    image1=cv2.cvtColor(image1,cv2.COLOR_GRAY2BGR)
    image2=np.zeros((1000,1000),np.uint8)
    image2=cv2.cvtColor(image2,cv2.COLOR_GRAY2BGR)

    try:
        t1,t2,t3=calculate_angles(x,y,z)

        if z>0:    
            cv2.line(image1,(round(L*math.cos(t1)*math.cos(t2))+origin[0],round(L*math.sin(t2))+origin[1]),
                 (round(L*math.cos(t1)*math.cos(t2)+L*math.cos(t1)*math.cos(t2+t3))+origin[0],round(L*math.sin(t2)+L*math.sin(t2+t3))+origin[1]),(0,0,255),20)
            
            cv2.line(image1,(origin[0],origin[1]),(round(L*math.cos(t1)*math.cos(t2))+origin[0],round(L*math.sin(t2))+origin[1]),(255,0,0),20)
        else:
            cv2.line(image1,(origin[0],origin[1]),(round(L*math.cos(t1)*math.cos(t2))+origin[0],round(L*math.sin(t2))+origin[1]),(255,0,0),20)

            cv2.line(image1,(round(L*math.cos(t1)*math.cos(t2))+origin[0],round(L*math.sin(t2))+origin[1]),
                 (round(L*math.cos(t1)*math.cos(t2)+L*math.cos(t1)*math.cos(t2+t3))+origin[0],round(L*math.sin(t2)+L*math.sin(t2+t3))+origin[1]),(0,0,255),20)


        cv2.line(image2,(origin[0],origin[1]),(round(L*math.cos(t1)*math.cos(t2))+origin[0],round(L*math.sin(t1)*math.cos(t2))+origin[1]),(255,0,0),20)
        cv2.line(image2,(round(L*math.cos(t1)*math.cos(t2))+origin[0],round(L*math.sin(t1)*math.cos(t2))+origin[1]),
                 (round(L*math.cos(t1)*math.cos(t2)+L*math.cos(t1)*math.cos(t2+t3))+origin[0],
                  round(L*math.cos(t2)*math.sin(t1) + L*math.sin(t1)*math.cos(t2+t3))+origin[1]),(0,0,255),20)

        image1=cv2.flip(image1,0)
        image2=cv2.flip(image2,0)

        cv2.putText(image1,"X-Y AXES",(10,970),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        cv2.putText(image2,"X-Z AXES",(10,970),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

        cv2.putText(image1,f"T1 = {round(t1*180/math.pi)} degrees",(10,50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),2)
        cv2.putText(image1,f"T2 = {round(t2*180/math.pi)} degrees",(10,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),2)
        cv2.putText(image1,f"T3 = {round(t3*180/math.pi)} degrees",(10,150),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),2)

        image1[:,990:999]=(255,255,255)

        image = np.concatenate((image1, image2), axis=1)

    except:
        image=np.concatenate((image1,image2),axis=1)
        cv2.putText(image,"Radius is bigger than 400",(origin[0]-300,origin[1]),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),5)

    

    cv2.imshow("Simulation",image)

    if cv2.waitKey(1) == ord('q'):
        break
