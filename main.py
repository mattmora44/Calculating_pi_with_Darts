import matplotlib.pyplot as plt
import random as rand
import math

def generate_x(n): # this function returns a list of n random values
    xlist = []
    for i in range(0,n):
        tempneg1 = rand.randint(0,1)
        if (tempneg1 == 1):
            tempx = (rand.random()) * -1.0
        else:
            tempx = (rand.random())
        xlist.append(tempx)
    return xlist

def generate_y(n): # this function returns a list of n random values
    ylist = []
    for i in range(0,n):
        tempneg2 = rand.randint(0,1)
        if (tempneg2 == 1):
            tempy = (rand.random()) * -1.0
        else:
            tempy = (rand.random())
        ylist.append(tempy)
    return ylist

def is_inside_circle(xpt, ypt): # this function returns true if the point
    distance = math.sqrt(xpt**2 + ypt**2) # is inside a unit circle
    if (distance <= 1):
        return True
    else:
        return False

def x_inside_circle(xpts, ypts): # this function returns a list of x values
    insideList = [] #              inside the circle
    for i in range(0,len(xpts)):
        if (is_inside_circle(xpts[i], ypts[i])):
            insideList.append(xpts[i])
    return insideList

def y_inside_circle(xpts, ypts): # this function returns a list of y values
    insideList = [] #              inside the circle
    for i in range(0,len(xpts)):
        if (is_inside_circle(xpts[i], ypts[i])):
            insideList.append(ypts[i])
    return insideList

def x_outside_circle(xpts, ypts): # this function returns a list of x values
    outsideList = [] #               outside of the circle
    for i in range(0,len(xpts)):
        if ( not is_inside_circle(xpts[i], ypts[i])):
            outsideList.append(xpts[i])
    return outsideList

def y_outside_circle(xpts, ypts): # this function returns a list of y values
    outsideList = [] #               outside the cicle
    for i in range(0,len(xpts)):
        if ( not is_inside_circle(xpts[i], ypts[i])):
            outsideList.append(ypts[i])
    return outsideList

####### Start of main script

n = -1
while (n <= 0):
    n = int(input("How many darts would you like to throw?: "))

xpts = generate_x(n)
ypts = generate_y(n)

# Creating the circle for the plot
xcir = []
ycir = []
xcir1 = []
ycir1 = []
# y = sqrt(x^2 - 1)
for j in range(-1000,1000):
    tempxcir = j / 1000.0
    tempycir = (math.sqrt( (1000000.0-j**2))) / 1000.0
    xcir.append(tempxcir)
    ycir.append(tempycir)
for j in range(-1000,1000):
    tempxcir = j / 1000.0
    tempycir = (math.sqrt( (1000000.0-j**2) )) / -1000.0
    xcir1.append(tempxcir)
    ycir1.append(tempycir)
plt.plot(xcir,ycir)
plt.plot(xcir1,ycir1)
# Circle has been added to the plot

# find which points are in the circle
xinCircle = []
yinCircle = []
xoutCircle = []
youtCircle = []
xinCircle = x_inside_circle(xpts, ypts)
yinCircle = y_inside_circle(xpts, ypts)
xoutCircle = x_outside_circle(xpts, ypts)
youtCircle = y_outside_circle(xpts, ypts)
# plot outside points
plt.scatter(xoutCircle, youtCircle, marker='x',
            color = 'r',
            label = 'Points Inside Circle')
# plot inside points
plt.scatter(xinCircle, yinCircle, marker='x',
            color = 'g',
            label = 'Points Outside Circle')
# calculate ratio
pi = 4 *len(xinCircle) / len(xpts)
print("Calculated value of pi: " + str(pi))

# plot setup
plt.title("Calculated value of pi with "+ str(n) +" darts: " + str(pi))
plt.legend()
plt.show()
