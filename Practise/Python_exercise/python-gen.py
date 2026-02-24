#1
def gen(n):
    for x in range(n+1):
        yield x * x

n = int(input())
m = gen(n)
for v in m:
    print(v, end=" ")

#2
def GEN(n):
    for x in range(n+1):
        if x%2==0:
            yield x
        else:
            continue
n=int(input())
m=GEN(n)
h=list()
for i in m:
    h.append(i)
print(h)

#3
def generator(n):
    for x in range(n):
        if x%3==0 and x%4==0:
            yield x
k=int(input())
u=generator(k)
for x in u:
    print(x, end=" ")

#4
def gen(n, m):
    for x in range(n, m):
        yield x * x
j = int(input())
p=int(input())
m = gen(j, p)
for v in m:
    print(v, end=" ")

#5
def gener(n):
    while n>0:
        yield n
        n=n-1
n=int(input())
hp=gener(n)
for i in hp:
    print(i, end=" ")