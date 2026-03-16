#tuple 
# (item1, item2, ...)
# it is a seq of item as a colletion 

t1 = 10, 20, 30
print(t1)
print(type(t1))

l1 = [1, 2, 3]
print(l1 , type(l1))

ti = tuple(l1)
print(l1 , type(t1))


fruits = ("mango" , "orange" , "banana")
print(type(fruits))

l1 = list(fruits)
print(l1 , type(l1))



#operartions

#+

student_details1 = (101 , "naman")
student_details2 = (98.3 , 87.5 , 89.5)
student_details = student_details1 + student_details2

print(student_details , type(student_details))

#*


t1 = ("students are alive " )
print(t1 * 5 )


# in , not in

student_details1 = (101 , "naman")
student_details2 = (98.3 , 87.5 , 89.5)

print(89.5 in student_details2)
print(90.5  in student_details2)

print(89.5 not in student_details2)
print(98.3  in student_details2)


#count

t1 = (1,2,3,1,3,4,1,4)
print(t1.count(1))


#index

t1 = (1 , 32,3 ,4 ,3, 2, 4,1) 
print(t1.index(4))


t1 = (4 ,5 , 6, 5,4 ,4,3, 1 )
print(f"smallest number :{min(t1)}" )
print(f"biggest number :{max(t1)}" )
print(f"total :{sum(t1)}" )

