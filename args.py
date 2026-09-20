def add(*args):
    print(*args , type(args))

add(10 , 23 , 7 ,5 ,3 ,11 , 45 , 6 ,7 ,2)


def add(*args):
    return sum(args)

   

result = add(10 , 23 , 7 ,5 ,3 ,11 , 45 , 6 ,7 ,2)
print(result)


def student_details(sid , sname, *marks):
    if len(marks) == 0:
        print(f"{sid} with id {sname} was absent in all exams.")
    else:
        persentage = sum(marks) / len(marks)
        print(f"{sid} with id {sname} got {persentage} %" )

student_details( 121 , "jhon" ,  98 , 87 , 89 , 91 , 79)
student_details( 103 , "ritik" ,  63 ,23 , 29 , 41 , 75)
student_details( 101 , "naman" ,  93 ,89 , 97 , 91 , 85)
student_details( 101 , "sahil" )


def student_details(sid , sname, **marks):
    if len(marks) == 0:
        print(f"{sname} is absent in all exams")

    else:
        persentage = sum(marks.values()) / len(marks)
        print(f"{sname} with id {sid} scored {persentage}%")

student_details(103 , "ritik" , sub1 = 98 , sub2 = 87 , sub3 = 78)
student_details(101 , "naman" , sub1 = 90 , sub2 = 98 , sub3 = 96)
student_details(104 , "sanya")


#doc string

def fun():
    """
    this is a doctring
    we can write what the function does here 
    :return: None
    """

    return None

print(help(fun))


def devide(num1 , num2):
    """
    num1= numenitor
    num2 = denomenator
    return: float
    """
    if num2 == 0:
        return "can't divide by zero"
    else:

        result = num1 / num2
        return result

print(devide(10 , 0))

