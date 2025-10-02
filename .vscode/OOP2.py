a = 10 
b = 20

sun = a + b
print(sum)


diff = a - b
print(diff)


class Student:
    name = "naman"

s1 = Student()
print(s1)




class Student:
    name = "naman"

s1 = Student()
print(s1.name)


s2 = Student()
print(s2.name)


class car:
    color = "blue"

car1 = car()
print(car1.color)



class car:
    color = "blue"
    brand = "BMW"

car1 = car()
print(car1.color)
print(car1.brand)


class Student:
    name = "naman"
    def __init__(self):
        print(self)
        print("adding new student in database..")


s1 = Student()
print(s1)




#class Student:
   # name = "naman"


class Student:
    
    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in database..")


s1 = Student("ishant")
print(s1.name)



class Student:
    
    def __init__(abcd, fullname):
        abcd.name = fullname
        print("adding new student in database..")


s1 = Student("ishant")
print(s1.name)




class Student:
    
    def __init__(abcd, fullname):
        abcd.name = fullname
        print("adding new student in database..")


s1 = Student("ishant")
print(s1.name)

s2 = Student("jay")
print(s2.name)



class Student:

    #default constructors
    def __init__(self):
       pass

    #parameterized constructors
    def __init__(self, name , marks):
       self.name = name
       self.marks = marks
       print("adding new student in database..")


s1 = Student("ishant" , 88)
print(s1.name, s1.marks)

s2 = Student("jay" , 98)
print(s2.name, s2.marks)



def __init__(self, name , marks):
       self.name = name
       self.marks = marks
       print("adding new student in database..")

s1 = Student("ishant" , 88)
print(s1.name, s1.marks)

s2 = Student("jay" , 98)
print(s2.name, s2.marks)


class Student:
    college_name = " SRM college"
    
    def __init__(abcd, fullname):
        abcd.name = fullname
        print("adding new student in database..")


s1 = Student("ishant")
print(s1.name)

s2 = Student("jay")
print(s2.name)

print(s2.college_name)

class Student:
    college_name = " SRM college"
    name = "jay"         #class attr
    
    def __init__(self, name, marks):
        self.name = name     #object attr > class attr
        self.marks = marks

        print("adding new student in database..")


s1 = Student("ishant" , 98)     
print(s1.name)



class Student:
    college_name = " SRM college"
    name = "jay"         #class attr
    
    def __init__(self, name, marks):
        self.name = name     #object attr > class attr
        self.marks = marks

    def welcome(self):
         print("welcome student")


s1 = Student("ishant" , 98) 
s1.welcome()    




class Student:
    college_name = " SRM college"
    name = "jay"         
    
    def __init__(self, name, marks):
        self.name = name    
        self.marks = marks

    def welcome(self):
         print("welcome student,", self.name)


s1 = Student("ishant" , 98) 
s1.welcome()    



class Student:
    college_name = " SRM college"
    name = "jay"         #class attr
    
    def __init__(self, name, marks):
        self.name = name     #object attr > class attr
        self.marks = marks

    def welcome(self):
         print("welcome student")

    def get_marks(self):
        return self.marks
       


s1 = Student("ishant" , 98) 
s1.welcome()    
print(s1.get_marks())




class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val

        print("hi", self.name, "your avg marks is:", sum/3)

s1 = student("sanjay dutt", [88, 99, 98])
s1.get_avg()



class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val

        print("hi", self.name, "your avg marks is:", sum/3)

s1 = student("sanjay dutt", [88, 99, 98])
s1.get_avg()


s1.name = "salman khan"
s1.get_avg()


class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


    @staticmethod
    def hello():
        print("hello")


    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val

        print("hi", self.name, "your avg marks is:", sum/3)

s1 = student("sanjay dutt", [88, 99, 98])
s1.get_avg()



class car:
    def start(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = car()
car1.start()


class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc


    
    def debit(self, ammount):
        self.balance -= ammount
        print("Rs.", ammount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, ammount):
        self.balance += ammount
        print("Rs.", ammount, "was credited")
        print("total balance = ", self.get_balance())


def get_balance(self):
    return self.balance


        

acc1 = account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)



