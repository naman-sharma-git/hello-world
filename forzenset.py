#forzen set are immutable sets
s1 = {1, 2, 5, 10}
s1.add(-1)
print(s1)


fs1 = frozenset({10 , 12 , 54})
print(fs1 , type(fs1))

fs2 = frozenset({10 , 50 , 100 , 200})
print(fs2 , type(fs2))

print(fs1 & fs2)

fs1 = frozenset({10 , 12 , 54})
print(fs1 , type(fs1))

fs2 = frozenset({10 , 50 , 100 , 200})
print(fs2 , type(fs2))

print(fs1 | fs2)


fs1 = frozenset({10 , 12 , 54})
print(fs1 , type(fs1))

fs2 = frozenset({10 , 50 , 100 , 200})
print(fs2 , type(fs2))

print(fs1 - fs2)
