from math import pi
import math
import cv2
import numpy as np


r = 1
g = 9.806

def calc_v(theta : float):
    return math.sqrt(2 * g * r * (1 - math.cos(theta)))
def calc_av(theta :float):
    return calc_v(theta)/ (2 *pi * r)

dt = 0.00001

t=0
theta = dt / 2

iters = 0


#draw vars
cx = 250
cy = 250
cr = 150

def draw_circle(frame, r, x, y):
    center_coordinates = (round(x), round(y)) 
    
    # Blue color in BGR 
    color = (0, 255, 255) 
    
    # Line thickness of 2 px 
    thickness = 2
    
    # Using cv2.circle() method 
    # Draw a circle with blue line borders of thickness of 2 px 
    frame = cv2.circle(frame, center_coordinates, r, color, thickness) 

def draw_time(frame, t):
    # font 
    font = cv2.FONT_HERSHEY_SIMPLEX 
    
    # org 
    org = (50, 50) 
    
    # fontScale 
    fontScale = 1
    
    # Blue color in BGR 
    color = (0, 0, 255) 
    
    # Line thickness of 2 px 
    thickness = 2
    
    # Using cv2.putText() method 
    frame = cv2.putText(frame, str(t) , org, font,  
                    fontScale, color, thickness, cv2.LINE_AA) 

def draw_axes(img,cx, cy):
    cv2.line(img, (0, cy), (cx * 2, cy), (255, 0, 0), 1) 
    cv2.line(img, (cx, 0), (cx, cy * 2), (255, 0, 0), 1) 

def draw(img, theta):
    draw_circle(img,cr,cx,cy)
    draw_time(img, t)

    x = cr*math.sin(theta) +cx
    y = -cr*math.cos(theta)+cy
    
    draw_circle(img,5, x, y)
    draw_axes(img, cx, cy)
    cv2.line(img, (cx, cy), (round(x), round(y)), (0, 255, 0), 1) 


    cv2.imshow("Frame:", img)
    

while theta <= math.acos(2 / 3):
    img = np.zeros((500, 500, 3), dtype = "uint8")
    av = calc_av(theta)
    ad = (dt * av)
    theta += ad # Apply Angular change over this very small interval (dt)
    t += dt
    iters += 1



    if iters%1000 == 0:
        draw(img, theta)
        key = cv2.waitKey(1)

        if key == ord("q"):
            break
        
draw(img, theta)


cv2.destroyAllWindows()