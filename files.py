f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("demo.txt", "r")

data = f.read(5)
print(data)

f.close()


f = open("demo.txt", "r")

line1 = f.readline()
print(line1)

f.close()


f = open("demo.txt", "r")


line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()

f = open("demo.txt", "r")


line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)


line3 = f.readline()
print(line3)

f.close()


f = open("demo.txt", "w")

f.write("I want to learn js tomorrow. 123")

f.close()


f = open("demo.txt", "a")

f.write("then i i'll move to reactJS")

f.close()



f = open("demo.txt", "a")

f.write("\nAfter that nodejs")

f.close()


#f = open("sample.txt", "w")
#f.close()

f = open("sample.txt", "a")
f.close()

f = open("demo.txt", "r+")
#f.write("abc")
print(f.read())
f.close()


f = open("demo.txt", "w+")
#f.write("abc")
f.write("abc")
print(f.read())
f.close()


f = open("demo.txt", "a+")
#f.write("abc")
#f.write("abc")
print(f.read())
f.close()




