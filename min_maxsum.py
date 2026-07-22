



for num in range(10):
    if num % 3 == 0: 
        continue

    print(num)
  
     

for num in range(1 , 10):
    if num % 3 == 0: 
        break

    print(num)

print()
#while loops 

num = 1 
while num < 5:
    print(num)
    num = num + 1


#correct_password = "Python"
#w#hile True:
 #   user_password = input("Enter the password: ")
  #  if user_password == correct_password:
   #     print("welcome naman ")
#
 #   else:
  #


num = 10
while num <= 20:
    print(num)

    num = num + 1 



import random

print(random.random())



import random

print(random.randint(10 ,33))

import random 


num  = (1 , 2 , 54 , 65 , 44 , 12)

print(random.choice(num))


import random 

fruits = ['apple' , 'orange' , 'kiwi' , 'banana']

print(random.choice(fruits))


import random 
cars = ['siziki' , 'toyota', 'bmw' , 'volvo']

print(random.choice(cars))



import random 
fruits = ['apple' , 'orange' , 'kiwi' , 'banana']
print(random.shuffle(fruits))
print(fruits)


for j in range(3):
    for i in range(2):
        print(f"i={i}  , j={j}")



for i in range(1 , 6):
    for j in range(1 , i + 1 ):
        print("*" , end=" ")
    print()


rows = int(input("enter the number of rows:"))
for i in range(1 , rows + 1):
    print("*" * i )


for i in range(1 , 6):
    for j in range(1 , i + 1 ):
        print(i , end=" ")
    print()
