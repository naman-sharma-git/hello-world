import copy

l1 = [1 , 3.2 , [21, 43, 76] , 'python']

l2 = copy.copy(l1)

print(l2)
print(id(l1))
print(id(l2))

l1[0] = 100
print(f"l1 --> {l1}" , id(l1))
print(f"l2 -->  {l2}" , id(l2))


