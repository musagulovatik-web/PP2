import functools
x=list(map(int, input().split()))
y=list(map(lambda z:z*z, x))
for u in y:
    print(u, end=" ")
t=list(filter(lambda z: z>21, y))
print(t)
g=zip(x,y)
d=dict(g)
for m,n in enumerate(d, start=1):
    print(f"The square of {m} is {n}")
sm=functools.reduce(lambda x,y: x+y, x) #sum of x
mx=functools.reduce(lambda x,y: x if x>y else y, y) #largest number in y
print(sm, mx)