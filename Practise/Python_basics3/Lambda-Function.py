#1
function= lambda x: x*2 #we create a mini function when we dont require something long
print(function(50))

#2
x=int(input())
y=int(input())
z=int(input())
j= lambda a, b, c: a*b+c #we write an name of function, then "lambda" and then needed variables + expression
print(j(x, y, z))

#3
def Force(n): #definition for our func to perform force from mass
    return lambda a: a*n #we created a lambda function inside regular function
mass=Force(9.8)
x=int(input())
print(mass(x)) #multiple our variable x to 9.8

#4
n = [1, 2, 3, 4] #we created a list
m = list(map(lambda x: x * 10, n)) # "map" function use lambda expression for every element in list "nums"
print(m)

#5
n = [1, 5, 8, 10, 3]
f = list(filter(lambda x: x > 5, n)) #filter is through our list by expression we wrote
print(f)
