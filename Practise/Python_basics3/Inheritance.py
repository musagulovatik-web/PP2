#1
class Object: #created a class
    def __init__(self, name):
        self.name=name #defined self.name
class Item(Object): #created a child class
    def __init__(self,name,do): #defined "name" and "do"
        super().__init__(name) #taken "name" information from parent class(Object)
        self.do=do
    def ms(self): #defined function 
        print(self.name+"is "+self.do)
human=Item("Human ","living") #give values into functions
human.ms() #call function