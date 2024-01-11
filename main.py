from math import pi
import math
from matplotlib import pyplot as plt

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

time_histories = []
avelocity_histories = []
theta_histories = []
velocity_histories = []
slope_histories = []

while theta <= math.acos(2 / 3):
    av = calc_av(theta)
    ad = (dt * av)
    theta += ad # Apply Angular change over this very small interval (dt)
    t += dt
    iters += 1

    time_histories.append(t)
    avelocity_histories.append(av)
    theta_histories.append(theta)
    velocity_histories.append(calc_v(theta))
    m = -1 * math.tan(theta)
    slope_histories.append(m) 

    if iters % 500 == 0:
        pass

print(theta)
print(t)
print("Last slope: ", slope_histories[-1])
print("Last a: ", ((velocity_histories[-1] - velocity_histories[-2]) / dt) )

plt.plot(time_histories, avelocity_histories, label="avelocity_histories")
plt.plot(time_histories, theta_histories, label="theta_histories")
plt.plot(time_histories, velocity_histories, label="velocity_histories")
plt.plot(time_histories, slope_histories, label="slope_histories")
plt.legend(loc="upper left")
plt.show()
# plt.draw()
# plt.pause(0.0000001)
# plt.clf()


# print("adding: ", ad)
# print("av: ", av)
# print("Theta: ", theta)
# print("T: ", t)

