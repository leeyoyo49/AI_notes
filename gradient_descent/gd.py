import numpy
import math
import matplotlib.pyplot as plt

#target func 
#eg. x^2 + 3x^4 = [0,0,2,0,4]
func_para = [0,0,2,-1]

#return y
def func(x):
    y =0
    for i in range(len(func_para)):
        y+=func_para[i]*math.pow(x,i)
    return y

#return derrerative of f(x)
def dfunc(x):
    dx = 0
    for i in range(1,len(func_para)):
        dx += func_para[i]*i*math.pow(x,i-1)
    return dx

"""
x_start = initial num
df = derrerative of f(x)
epoches = how many times
lr = learing rate
"""
def GD(x_start, df, epoches, lr):
    passed_points = numpy.zeros(epoches+1)
    x = x_start
    passed_points[0] = x
    for i in range(epoches):
        dx = df(x)
        print(dx)
        delta = -dx*lr
        x += delta
        passed_points[i+1] = x

    return passed_points

x_start = -5
epoches = 20
lr = 0.005
x = GD(x_start, dfunc, epoches, lr)
print(x)

from numpy import arange 
t = arange(-10,10,0.01)

plt.plot(t, [func(i) for i in t], c='b')
plt.plot(x, [func(i) for i in x], c='r', label=f"lr={lr}")
plt.scatter(x, [func(i) for i in x], c ='r',)
plt.legend()
plt.show()