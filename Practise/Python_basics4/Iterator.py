#1
mylist={"5kg", "10kg", "15kg", "20kg"} #list
x=iter(mylist) #variable for iterator
print(next(x)) #print first element
print(next(x)) #iterate onto other one

#2
Mylist={"5kg", "10kg", "15kg", "20kg"} #other one list
for x in Mylist: #we iterate list with loop(while)
    print(x)

#3
y="You are welcome!" #string
u=len(y) #length of our string
for i in range(0, u): #iterating with "for" loop
    print(i)
    
#4
class iterator: #create class for iterator
    def __iter__(self): #iter func
        self.a=1
        return self 
    def __next__(self): #next func
        x=self.a
        self.a+=1 #iterating by 1
        return x #return value
myclass=iterator() #create iterable value
myiter=iter(myclass) #iterating
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#5
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)