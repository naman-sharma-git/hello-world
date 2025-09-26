#with open("eg.txt", "r") as f:
    #data = f.read()
    #print(data)


#with open("eg.txt", "w") as f:
    #f.write("new data")


with open("practice.txt", "w") as f:
    f.write("hi everyone\nwe are learning files I\O\n")
    f.write("using java\nI like programing in java.")



with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)


word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")


def check_for_word():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(word in data):
            print("found")
        else:
            print("not found")

check_for_word()


def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line()




def check_for_line():
    word = "programing"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line()


def check_for_line():
    word = "abc"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

print(check_for_line())



