#1
def kmh_to_ms(x): #definition for our func
    print(float(x)/3.6) #our func need to change speed system from "km/h" to "m/s", so we divide it by 3.6
x=int(input())
kmh_to_ms(x)

#2
def calculator(a,b,c): #simple calculator by functions
    if b=="*":
        return a*c #we return values
    elif b=="/":
        return a/c
    elif b=="+":
        return a+c
    elif b=="-":
        return a-c
    elif b=="^":
        return a**c
    else:
        print("Error")
print("First variable:")
x=int(input())
print("Second variable:")
z=int(input())
print("Operation(only *, /, +, -, ^):")
y=input()
print(calculator(x, y, z))

#3
def Mail(a, b): #a,b are parameters
    print("Login: " + a +"@gmail.com")
    print("Password:"+ " " +b )
x=str(input())
y=str(input())
Mail(x,y) #x,y are arguments (we can write a=x, b=y)


#4
def Names(a):
    for name in a:
        print(name, end=" ") #that func would write names from given list one by one
x=list(["Alex", "Batyr", "Charles", "Moicano", "Izzy"]) 
Names(x)

#5
def marks(*args): #we use the "*" at the beginning of parameter when we dont know how many arguments will be 
    x=int(len(args)) #length of out tuple
    y=int(0)
    for i in range(x):
        y=y+args[i] #sum 
    print("Average mark: "+ str(y/x)) 
x=list(map(int, input().split())) #create an array with only integers
marks(*x)

#6
def List(**kwargs): #kwargs(**) help us to make a dict(), we have a name and key for that
    print(kwargs)
List(name="Alikhan") #it is a little hard to use a kwargs with an input() variable
List(name="Alan", age="21")
List(name="Justin", age="37")

#7
def Scope(): #we created a function that contains some numbers which are useable only inside this func
    x=int(300)
    y=int(60)
    return(x/y)
x=Scope()
print(x)

#or we could carry our x and y outside the functions that will make our variables global
""""The LEGB Rule
Python follows the LEGB rule when looking up variable names, and searches for them in this order:

Local - Inside the current function
Enclosing - Inside enclosing functions (from inner to outer)
Global - At the top level of the module
Built-in - In Python's built-in namespace"""

