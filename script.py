marks1 = 94.1
marks2 = 87.9
marks3 = 95.4
marks4 = 66.1
marks5 = 55.4


marks = [94.1, 87.9, 95.4, 66.1, 55.4]
print(marks)

marks1 = 94.1
marks2 = 87.9
marks3 = 95.4
marks4 = 66.1
marks5 = 55.4


marks = [94.1, 87.9, 95.4, 66.1, 55.4]
print(type(marks))
print(marks[0])
print(marks[3])

marks1 = 94.1
marks2 = 87.9
marks3 = 95.4
marks4 = 66.1
marks5 = 55.4


marks = [94.1, 87.9, 95.4, 66.1, 55.4]
print(len(marks))
print(marks[0])
print(marks[3])


student = ["karan", 95.4, 17, "mumbai"]
print(student)
student[0] = "naman"
print(student)

str = "hello"
print(str[0])


student = ["karan", 95.4, 17, "mumbai"]
print(student[1])

marks = [85, 94, 76, 63, 48]
print(marks[1:4])         
  
 #if we miss the last idx then the last will we our last index for example

marks = [85, 94, 76, 63, 48]
print(marks[1:])     #here we miss the last idx      look in terminal the last idx is our last
                     #same in front idx



marks = [85, 94, 76, 63, 48]
print(marks[-3:-1])    


list = [2, 1, 3]
list.append(4)
print(list)



list = [2, 1, 3]
print(list.sort())
print(list)


list = [2, 1, 3]
print(list.append(4))
print(list.sort())                 #accending order
print(list)


list = [2, 1, 3]
print(list.append(4))
print(list.sort(reverse=True))     #decending order
print(list)



list = ["banana", "litchi","apple"]
#print(list.append(4))
print(list.sort(reverse=True))    #decending alphabetically
print(list)



list = ["a", "d", "e", "f", "b"]       #reverse list
list.reverse()    
print(list)


list = [2, 1, 3]
list.insert(1, 5)
print(list)

list = [2, 1, 3, 1]
list.remove(1)
print(list)


list = [5, 4, 3, 3, 2]
list.pop(3)
print(list)


tup = (1, 3, 5, 2, 5, 4)
print(type(tup))
print(tup[0])
print(tup[1])

tup = ()
print(tup)
print(type(tup))

tup = (1,)      #allways write coma with single elemet
print(tup)
print(type(tup))

#if we write with out coma then python think that it is a normal intezer and write class itz for ex


tup = (1)      
print(tup)
print(type(tup)) # same as float and string

tup = ("hello",)
print(tup)
print(type(tup))

tup = (1, 2, 3, 5, 4)
print(tup[1:3])

tup = (4, 2, 1, 5, 8)
print(tup.index(2))

tup = (4, 2, 1, 5, 8, 2)
print(tup.count(2))

movies = []
mov1 = input("entre 1st movie: ")
mov2 = input("entre 2st movie: ")
mov3 = input("entre 3st movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)


ovies = []
movies.append(input("entre 1st movie: "))
movies.append(input("entre 2st movie: "))
movies.append(input("entre 3st movie: "))

list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")  #if it come same as copy after reverse than it is palindrome if not then NOT palendrome