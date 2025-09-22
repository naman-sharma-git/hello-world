i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

print("end of loop")



i = 1
while i <= 10:
    if (i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1


i = 1
while i <= 10:
    if (i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1


nums = [1, 2, 3, 4, 5]

for val in nums:
    print(val)


veggies = ["apple", "banana", "allu", "orange"]

for val in veggies:
    print(val)


tup = (1, 2, 3, 4, 8, 4, 3, 9)

for nums in tup:
    print(nums)


str = "namansharma"

for char in str:
    print(char)
else:
    print("END")


str = "namansharma"

for char in str:
    if(char == 's'):
        print("s found")
        break
    print(char)
else:
    print("END")


str = "namansharma"

for char in str:
    if(char == 's'):
        print("s found")
    print(char)
else:
    print("END")


str = "namansharma"

for char in str:
    if(char == 's'):
        print("s found")
    print(char)

print("END")


list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for val in list:
    print(val)


num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 64


idx = 0
for val in num:
    if(val == x):
        print("number found at idx", idx)
    idx += 1


print(range(5))


seq = range (5)

for i in seq:
    print(i)


seq = range (17)

for i in seq:
    print(i)


for i in range(10):    #range(stop)
    print(i)


for i in range(2, 10):    #range(start, stop)
    print(i)


for i in range(2, 10, 2):    #range(start, stop, step)
    print(i)


for i in range(2, 100, 2):
    print(i)

for i in range(1, 100, 2):
    print(i)


for i in range(1, 101):
    print(i)

for i in range (100, 0, -1):
    print(i)



for i in range(5):
    pass

print("some useful work")


n = 5 

for i in range(1, n+1):
    print(i)

n = 5 

sum = 0
for i in range(1, n+1):
    sum += i

print("totalsum=", sum)



n = 6

sum = 0
for i in range(1, n+1):
    sum += i

print("totalsum=", sum)



n = 7

sum = 0
for i in range(1, n+1):
    sum += i

print("totalsum=", sum)

n = 7

sum = 0

i = 1
while i<= n:
    sum += i
    i += 1

print("totalsum=", sum)


n = 5

fact = 1

i = 1
while i<= n:
    fact *= i
    i += 1

print("factorial =", fact)



n = 3

fact = 1

i = 1
while i<= n:
    fact *= i
    i += 1

print("factorial =", fact)


n = 5 
fact = 1 

for i in range(1, n+1):
    fact *= i

print("factorial =", fact)


n = int(input("enter number :"))

for i in range(1, 11):
    print(n*1)