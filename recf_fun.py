def factrec(num):
    if num == 1:
        return 1
    else :
          factorial = num * factrec(num - 1)
          return factorial

print(factrec(4))

n = 1 #GLOBAL VARIABLE

def fn():
     global n
     n = 4
     print("in",n)

fn()

print("out" ,n)


def add_1(num):
     return num + 1


def square(num):
     return num ** 2

num = int(input("enter the number: "))

result_1 = add_1(num)
result_2 = square(add_1(num))
print(f"result is {result_2}")


fun = lambda a, b : a + b
print(fun(10 , 20))


print("hello world")

# FILTER FUNCTION

seq = [ 1 , 2, 3, 5, 6, ]
odd = lambda x : True if x % 2 != 0 else False
filtered = filter(odd , seq)

print(f"odd numbers in above sequence are {list(filtered)}")
