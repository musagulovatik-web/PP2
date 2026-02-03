x=int(input())
y=int(input())
if x>y: #first condition
    print("X is bigger")
elif x==y: #second condition
    print("They are equal")
else: #would happen in every condition except "if" and "elif"
    print("Y is bigger")
    
q=True
if q: #combine with booleans, this code would write "Yes" while "q=True"
    print("Yes")
    
#We have special statement "pass", it means null in any of condition