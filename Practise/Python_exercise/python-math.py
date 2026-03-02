#1
import math

d = float(input())
r = d * (math.pi / 180)
print(r)

#2
h = float(input())
a = float(input())
b = float(input())
res = ((a + b) / 2) * h
print(res)

#3
import math

n = int(input())
s = float(input())
res = (n * s**2) / (4 * math.tan(math.pi / n))
print(int(res))

#4
b = float(input())
h = float(input())
print(b * h)