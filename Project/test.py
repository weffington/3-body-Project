import numpy as np
import re
from numpy import array

x=array([[2,3],[3,2]])
print(2*x)
arr=input("Enter position coordinates for each body (e.g. (2,2),(3,3),(4,4)):\n")
l = [p for p in re.split(r'[\(\),]', arr) if p.strip()]
m = list(map(float, l))
rvals = array([m[:2],m[2:4],m[4:6]])

arr=input("Enter velocity vectors in the same form (e.g. (1,0),(2,0),(0,0)):\n")
l = [p for p in re.split(r'[\(\),]', arr) if p.strip()]
m = list(map(float, l))
vvals = array([m[:2],m[2:4],m[4:6]])

print(rvals)