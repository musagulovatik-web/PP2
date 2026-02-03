x=int(input())
y=int(input())
while y<x: #in this case "while" statement repeat code inside it until given condition is true
    y+=1 

while y>=x: #condition
    x=x+1
    if x==y: #combining "if" and "while"
        break #"break" statement that stop our loop
        #otherwise we have "continue" statement that stop iteration and pass to the next one
        
q=True
while q:
    print("YES")
else: #we can use "else" statement, that will work if "q" become false
    print("NO") 

