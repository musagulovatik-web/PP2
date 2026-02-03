y=["Any", "Word","That","you", "want"]
for x in y: #we created a new variable that will iterate every element is given list
    print(x) #print every element

for x in "Any": #Or use it with a string
    print(x) 
    
z=["32","12","0","11"]
for x in z:
    x*=2
    print(x)
    if x== "12": #we combined "for" and "if"
        break #we used "break" statement, that stop the iteration
    
g=int(input())
for i in range(g):#Values from 0 to g-1 (we could change start point if we write range(-1, g))
    print(i)
for i in range(-2, g, 2): #We start from -2 until g-1, and size of step is 2
    pass #pass statement

for i in range(g):
    print(i)
else: #else statement in "for" loops
    print(x) 
    
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) #we can write loop inside loop

