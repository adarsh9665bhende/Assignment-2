
from matplotlib.pyplot import *
from numpy import *
#from sympy import *
x=linspace(-3,3,5000)
y=x**2
plot(x,y)
x=linspace(-4,4,100)
y=2-x
plot(x,y)
N = 2
x =-2,1
y = 4,1
#axhline(colour = 'black')
fill_between(y,x,where = [(x>-2)and(x<1) for x in x] ,colour='red',alpha=0.3)
scatter(x, y)
show()
xlabel("x axis")
ylabel("y axis")
print(x)
show()