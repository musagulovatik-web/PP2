#Arithmetic operator
x=int()
y=int()
print(x+y) #we use '+' operator to find a sum of our integers, otherwise we can add string to each other
'''+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y	'''

#Assignment operators
x=int(2)
x+=9 #give us x=x+9, and we could use it with any arithmetic function, just combine it like "x*=9" or "x/=9"

#Comparison
y=int(6)
if x==y: #if we will write "x=y" it would not valid
    print("Something") #otherwise we could use ">" "<" ">=" "<=" and "!="

#logical
x=int(input())
if(x<3 and x>1): # "And", "Not" and "Or" operators
    print("Good")
    
#Identity
x="Python"
y="C++"
print(x is y) #False

#Membership
y=["apple", "banana", "orange"]
x="apple"
print(x in y) #True

#Bitwise
print(6&3) #AND operation(we use bitwise to work with binary)
"""
& 	x & y	
|	x | y	
^	x ^ y	
~	~x	
<<	x << 2	
>>	x >> 2
"""

#Precedence
print(10+43*2) #in that case our multiple will calculates first
