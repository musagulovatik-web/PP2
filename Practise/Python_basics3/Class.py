#1
class Person: #simply class, same as func
    x=5
p1=Person()
print(p1.x)
del p1 #deleting unit

#2
class Warrior: #created class
    def __init__(self, n, p=100): #initialized characteristic of our class, gave default(minimal) size of power
        self.name=n
        self.power=p
w1=Warrior("Khan", 100) #give needed characteristic, switch size of power
print(w1.power, w1.name) #printed it

#3
class Support: #create class
    def __init__(self, name, hp, mana): #initialize characteristics
        self.name = name
        self.hp = hp
        self.mana = mana
        
    def info(self): #create "self" function
        print("My name is", self.name, ", I have", self.hp, "hp and", self.mana, "mana") #introducing

w1 = Support("Azamat", 100, 200)
w2 = Support("Tima", 150, 120)
w3 = Support("Ali", 120, 180)

w1.info()
w2.info()
w3.info()

#4
class J: #created a class
    def __init__(self, g):
        self.m=g #defined self characteristic
    def greet(self):
        return "Hello, "+self.m #value that our func need to return
    def meet(self): #created other self function that include first self function
        h=self.greet()
        print(h + " ,Im glad to see you")
j1=J("Atik") #give value to our function J
j1.meet() #run self.meet function

#5
class G:
    def __init__(self, age):
        self.age=age
    def a(self):
        return "I am "+self.age
    def you(self):
        h=self.a()
        print(h+ " Wow im too")
g1=G("18")
g1.you()
