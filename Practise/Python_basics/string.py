#1
x="Hello"
y='Hello'
print(x,y) #would give us the same answer, because we can use "" instead of '' and reverse

#2
x='''Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;''' 
print(x) #we could make a multiline string

#3
x="How are you?"
print(x[1]) #we could use any string like array

if "you?" in x:
    print("Great") #also  do operations like that
    
print(x[:4]) #and cut need parts like that

#4  
x="Github"
print(x.upper()) # to get GITHUB
print(x.lower()) # to ger github
print(x.replace("G", "K")) #to replace

#5
x="Git"
y="Hub"
print(x+y) #to get GitHub

#6
x = 18
y = f"My name is Ben, I am {x}"
print(y) #to format string

