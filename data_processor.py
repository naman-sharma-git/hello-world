info = {
    "key" : "value",
    "name" : "naman",
    "learning" : "coding",
    "age" : 19,
    "is_adult" : True,
    "marks" : 93.4
}

print(info)


info = {
    "name" : "naman",
    "subject" : ["python", "c", "java", "html"],
    "topics" : ("dict", "set"),
    "age" : 19,
    "is_adult" : True,
    "marks" : 93.4
}

print(info)


info = {
    "name" : "naman",
    "subject" : ["python", "c", "java", "html"],
    "topics" : ("dict", "set"),
    "age" : 19,
    "is_adult" : True,
    "marks" : 93.4
}

print(type(info))

info = {
    "name" : "naman",
    "subject" : ["python", "c", "java", "html"],
    "topics" : ("dict", "set"),
    "age" : 19,
    "is_adult" : True,
    "marks" : 93.4
}

print(info["name"])
print(info["topics"])
print(info["age"])


info = {
    "name" : "naman",
    "subject" : ["python", "c", "java", "html"],
    "topics" : ("dict", "set"),
    "age" : 19,
    "is_adult" : True,
    "marks" : 93.4
}

info["name"] = "python"
print(info)


info = {
    "name" : "naman",
    "subject" : ["python", "c", "java", "html"],
    "topics" : ("dict", "set"),
    "age" : 19,
    "is_adult" : True,
    "marks" : 93.4
}

info["name"] = "python"     #if we do it again our old value become overwrite so not posible
info["surname"] = "sharma"
info["college"] = "SRM"
print(info)


null_dict = {}
print(null_dict)


null_dict = {}
null_dict["name"] = "naman"
null_dict["age"] = "18"
print(null_dict)


student = {
    "name" : "daksh",
    "subjects" : ["phy", "maths"]
    }
print(student)


student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,

    }
}

#nested dict


print(student)


student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,

    }
}

#nested dict


print(student["subjects"])


student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,
        "chem" : 87

    }
}

#nested dict


print(student["subjects"]["math"])


student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,
        "chem" : 87

    }
}


print(student.keys())    #only outer layer keys


student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,
        "chem" : 87

    }
}

print(len(student))
print(student.keys())   #we also add here len()


student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,
        "chem" : 87

    }
}

print(list(student.values()))


student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,
        "chem" : 87

    }
}

print(student.items())


student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,
        "chem" : 87

    }
}

pairs = list(student.items())
print(pairs[0])


student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,
        "chem" : 87

    }
}

print(student["name"])
print(student.get("name"))    #but


student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,
        "chem" : 87

    }
}

#print(student["name2"])   #error
print(student.get("name2"))   #no error -> none


student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,
        "chem" : 87

    }
}

#print(student["name2"])   #error
print("hi")
print("welcone to")
print("README.py")
print("we are learning")
print("coding")


a = 2 
b = 5
sum = a+b




student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,
        "chem" : 87

    }
}

student.update({"city" : "sonipat"})

print(student)


student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,
        "chem" : 87

    }
}

student.update({"city" : "sonipat", "age" : 18})

print(student)


student = {
    "name" : "daksh",
    "subjects" : {
        "phy" : 88,
        "math" : 98,
        "chem" : 87

    }
}

student.update({"name" : "naman sharma", "age" : 18})

print(student)