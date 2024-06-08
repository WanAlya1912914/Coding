# MATH Libraries
from math import exp, sqrt
# from math import*         # this is to import all function in math lib
a = exp(0)
print(a)

b = sqrt(9)
print(b)

# MATPLOTLIB Libraries
from matplotlib import pyplot as plt

x = [0,1,2,3,4,5,6,7,8,9,10]
y = [0,1,4,9,16,25,36,49,64,81,100]
plt.plot(x,y)
plt.show()

i = [0,-1,-2,-3,-4,-5,-6]
j = [0,-1,-8,-27,-64,-125,-216]
plt.plot(i,j)
plt.show()