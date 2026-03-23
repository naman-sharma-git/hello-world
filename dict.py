#more operations

#allowed key = string , int , float , bool , tuple => immutable
#not allowed key = list , set , dict => mutable
# keys can only a immutable data type 
# value can b e any thing like list  , set , string

d1 = {("rohit") : 2 , ("rahul") : 9}
print(d1 , type(d1))

d2 = {(1) : True , (2) : False}
print(d2)

d3 = {(True) : 2 , (False) : 4}
print(d3)

l1 = {"number" : 101 , "marks" : [79.6 , 88.6 , 98.5] , "idea" : {1 ,3, 5}}
print(l1, type(l1))
print(l1["marks"][1])
k1 = {"number" : 101 , "marks" : {"eng" : 79.6 ,"maths" : 88.6 ,"c" : 98.5} , "idea" : {1 ,3, 5}}
print(k1["marks"])
print(k1["marks"]["eng"])

print(k1.keys())

print(k1.values())

print(k1.items())