import cv2
import numpy as np
import math

origin=(500,500)

def locationx(x0):
    global x
    x=x0

def locationy(y0):
    global y
    y=y0

def solution1(x,y,image):
    try:
        t1=2*math.atan2((2*200*y+(-(200**4)+2*(200**2)*(200**2)+2*(200**2)*x**2+2*(200**2)*y**2-(200**4)+2*(200**2)*(x**2)+2*(200**2)*(y**2)-(x**4)-2*(x**2)*(y**2)-y**4)**(1/2)),
                        (200**2+2*200*x-200**2+x**2+y**2))
        t2=-2*math.atan2(((-200**2+2*200*200-200**2+x**2+y**2)*(200**2+2*200*200+200**2-x**2-y**2))**(1/2),
                         (-200**2+2*200*200-200**2+x**2+y**2))
        x1,y1=((round(math.cos(t1)*200)+origin[0],round(math.sin(t1)*200)+origin[1]))
        x2,y2=((round(math.cos((t1+t2))*200)+round(math.cos(t1)*200)+origin[0],
                round(math.sin((t1+t2))*200)+round(math.sin(t1)*200)+origin[1]))
        cv2.line(image,(origin[0],origin[1]),(x1,y1),(255,0,0),20)
        cv2.line(image,(x1,y1),(x2,y2),(0,0,255),20)  
        image=cv2.flip(image,0)
        cv2.putText(image,f"theta1 = {round(t1*180/math.pi)} degrees   theta2 = {round(t2*180/math.pi)} degrees",(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        cv2.putText(image,"Solution 1",(0,950),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

    except:
        image=cv2.flip(image,0)
        cv2.putText(image,"Radius is bigger than 400 or less than 1",(0,300),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)
    
    return image


def solution2(x,y,image):
    try:
        t1=2*math.atan2((2*200*y-(-(200**4)+2*(200**2)*(200**2)+2*(200**2)*(x**2)+2*(200**2)*(y**2)-(200**4)+2*(200**2)*(x**2)+2*(200**2)*(y**2)-(x**4)-2*(x**2)*(y**2)-(y**4))**(1/2)),
                        (200**2+2*200*x-200**2+(x**2)+(y**2)))
        t2=2*math.atan2(((-(200**2)+2*200*200-200**2+x**2+y**2)*(200**2+2*200*200+200**2-x**2-y**2))**(1/2),
                        (-200**2 + 2*200*200 - 200**2 + x**2 + y**2))
        theta1=t1
        theta2=t2
        x1,y1=((round(math.cos(theta1)*200)+origin[0],round(math.sin(theta1)*200)+origin[1]))
        x2,y2=((round(math.cos((theta1+theta2))*200)+round(math.cos(theta1)*200)+origin[0],
                round(math.sin((theta1+theta2))*200)+round(math.sin(theta1)*200)+origin[1]))
        cv2.line(image,(origin[0],origin[1]),(x1,y1),(255,0,0),20)
        cv2.line(image,(x1,y1),
                 (x2,y2),(0,0,255),20)
        image=cv2.flip(image,0)
        cv2.putText(image,f"theta1 = {round(theta1*180/math.pi)} degrees   theta2 = {round(theta2*180/math.pi)} degrees",(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        cv2.putText(image,"Solution 2",(0,950),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

    except:
        image=cv2.flip(image,0)
        cv2.putText(image,"Radius is bigger than 400 or less than 1",(0,300),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2)

    return image


a=1

cv2.namedWindow('image',cv2.WINDOW_NORMAL)

cv2.createTrackbar('x','image',200,400,locationx)
cv2.createTrackbar('y','image',200,400,locationy)

cv2.resizeWindow("image", 500, 500)

while True:
    image=np.zeros((1000,1000),np.uint8)

    image=cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)

    if a==1:
        image=solution1(x,y,image)
    else:
        image=solution2(x,y,image)

    cv2.imshow("image",image)

    key=cv2.waitKey(1)
    if key==ord('q'):
        break
    elif key==ord('c'):
        a=-a
