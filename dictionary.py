#{key1 : value1 , key2 : value2 , .....}

groceries = {'milk' : 45 , 'coffee' : 12 , 'bread' : 32}
print(groceries)
print(type(groceries))
print(len(groceries))
print(groceries['milk'])

#dict are mutable

groceries = {'milk' : 45 , 'coffee' : 12 , 'bread' : 32}

groceries['milk'] = 50
print(groceries)

groceries = {'milk' : 45 , 'coffee' : 12 , 'bread' : 32}
groceries['egg'] = 11
print(groceries)


#operations in dict

student1 = {"maths" : 98 , "phy" : 88 , "c" : 99}
print(student1)
print(student1.get("phy"))

numbers = {"cafe" : 1001 , "room" : 2121 , "mam" : 555}
print(numbers.get("cafe" , 7575))
print(numbers.get("hotel" , 7575))

#in

emp1 = {'sourav' : 9798787248 , 'pushkar' : 5924437544 , 'dev' : 32325345353}
print(emp1)
print('dev' in emp1)

#update 

sem1 = {'maths' : 98 , 'c' : 99 , 'chem': 78}
sem2 = {'python' :99 , 'java' : 88}
sem1.update(sem2)

print(sem1)

#pop = remove

sem1.pop('maths')
print(sem1)