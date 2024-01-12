from math import pi
import math
import cv2
import numpy as np


r = 1
g = 9.806
dt = 0.00001
t=0
theta = dt / 2

iters = 0

#draw vars
CENTER_CIRCLE_X = 250
CENTER_CIRCLE_Y = 250
CENTER_CIRCLE_R = 150


class IceCube:
    def __init__(self):
        self.x = CENTER_CIRCLE_X+CENTER_CIRCLE_R
        self.y = CENTER_CIRCLE_Y
        self.av = 0;
        self.r = 5
        self.theta = 0
    def display(self,img):
        draw_circle(img,self.r,self.x,self.y)
    def update(self,theta):
        self.x = CENTER_CIRCLE_R*math.sin(theta) +CENTER_CIRCLE_X
        self.y = -CENTER_CIRCLE_R*math.cos(theta)+CENTER_CIRCLE_Y
    

cube = IceCube()


def calc_v(theta : float):
    return math.sqrt(2 * g * r * (1 - math.cos(theta)))
def calc_av(theta :float):
    return calc_v(theta)/ (2 *pi * r)
def draw_circle(frame, r, x, y):
    center_coordinates = (round(x), round(y)) 
    color = (0, 255, 255) 
    thickness = 2
    frame = cv2.circle(frame, center_coordinates, r, color, thickness) 
def draw_time(frame, t):
    font = cv2.FONT_HERSHEY_SIMPLEX 
    org = (50, 50)
    fontScale = 1
    color = (0, 0, 255) 
    thickness = 2
    frame = cv2.putText(frame, str(t) , org, font,  
                    fontScale, color, thickness, cv2.LINE_AA) 

def draw_axes(img,CENTER_CIRCLE_X, CENTER_CIRCLE_Y):
    cv2.line(img, (0, CENTER_CIRCLE_Y), (CENTER_CIRCLE_X * 2, CENTER_CIRCLE_Y), (255, 0, 0), 1) 
    cv2.line(img, (CENTER_CIRCLE_X, 0), (CENTER_CIRCLE_X, CENTER_CIRCLE_Y * 2), (255, 0, 0), 1) 

def draw(img, theta):
    draw_circle(img,CENTER_CIRCLE_R,CENTER_CIRCLE_X,CENTER_CIRCLE_Y)
    draw_time(img, t)
    draw_axes(img, CENTER_CIRCLE_X, CENTER_CIRCLE_Y)
    cv2.line(img, (CENTER_CIRCLE_X, CENTER_CIRCLE_Y), (round(cube.x), round(cube.y)), (0, 255, 0), 1) 
    cube.display(img)

    cv2.imshow("Frame:", img)
    

while theta <= math.acos(2 / 3):
    img = np.zeros((500, 500, 3), dtype = "uint8")
    av = calc_av(theta)
    ad = (dt * av)
    theta += ad # Apply Angular change over this very small interval (dt)
    t += dt
    iters += 1
    cube.update(theta)


    if iters%1000 == 0:
        draw(img, theta)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        
draw(img, theta)
key = cv2.waitKey(0)

cv2.destroyAllWindows()
