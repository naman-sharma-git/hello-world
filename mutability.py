#mutability & immutability
#list are mutable 

s1 = "python is fun"
s2 = s1.replace("python" , "java")
print(s1)
print(s2)

l1 = ["mango", "aalu", "orange"]
print(id(l1))
l1.append("banana")
print(l1)
print(id(l1))

l1 = ["mango", "aalu", "orange"]
l1[-1] = "apple"
print(l1)
