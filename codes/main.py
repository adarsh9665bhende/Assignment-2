import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import fsolve,root

f=lambda x:2-x
g = lambda x:x**2
h=lambda x: f(x)-g(x)
roots = root(h,(-2,1),method="hybr").x
x1 = roots[-2]
x2 = roots[1]
area = quad(h,x1,x2)
print(area)

