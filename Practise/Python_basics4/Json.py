#1
import json #import json module
x= '{"age":21, "name":"Ateik", "city":"Almaty"}' #writing data in json variant
y=json.loads(x) #load json data to variable y(y become similar to dict)
print(y["age"])
print(y["name"])
print(y["city"])

#2
z={"age":25, "name":"Jamal", "city":"NY"} #created python dict
t=json.dumps(z) #converted it to JSON type
print(t) 

#3
g={"age":34, "name":"Charles", "city":"Brazil, Favellas", "status":"Married"} #created a dict
h=json.dumps(g, indent=4) #converted to json, gave intend(digit is variate), intend help to upgrade looks of code
print(h)

#4
j={"class":"tank", "inventory":"blade, shield", "HP":4000, "Armor":2000, "Mana":500, "Special Ability":"None"} #created dict
k=json.dumps(j, indent=3, sort_keys=True) #converted to json with 2 parameters, indent to upgrade look, sort_keys=True to sort by alphabet
print(k)