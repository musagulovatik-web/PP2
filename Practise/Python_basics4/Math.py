#1
l=(5, 10, 21, 97) #list
x=min(l) #minimal element(by value)
y=max(l) #maximal element(by value)
print(x, y)

#2
x=abs(-912+54) # even if our value is less than 0, "abs" function would write it absolute value

#3
y=pow(5,3) #5**3

#4
import math #import "math" module
z=math.sqrt(121) #find root of 121(square root)

#5
a=math.ceil(1.9) #return 2
b=math.floor(1.9) #return 1

#6
f=math.pi # П constant

"""1. Basic Functions
sqrt(x) — Square root of 
.
pow(x, y) — Raises 
to the power of 
.
factorial(n) — Factorial of 
.
fabs(x) — Absolute value of 
(as a float).
gcd(a, b) — Greatest common divisor of 
and 
.
isqrt(n) — Integer square root.
2. Rounding 
ceil(x) — Rounds 
up to the nearest integer.
floor(x) — Rounds 
down to the nearest integer.
trunc(x) — Truncates 
(removes the decimal part).
fmod(x, y) — Returns the remainder of division (more precise than %).
3. Trigonometry 
sin(x), cos(x), tan(x) — Sine, cosine, and tangent (input in radians).
asin(x), acos(x), atan(x) — Inverse trigonometric functions.
degrees(x) — Converts radians to degrees.
radians(x) — Converts degrees to radians.
hypot(x, y) — Calculates the hypotenuse 
.
4. Logarithms and Exponents
log(x, [base]) — Logarithm of 
(natural by default).
log10(x) — Base-10 logarithm.
exp(x) — Returns 
.
5. Constants
pi — Mathematical constant 
.
e — Mathematical constant 
.
tau — Mathematical constant 
.
inf — Floating-point positive infinity.
nan — A floating-point "Not a Number" (NaN) value.
"""