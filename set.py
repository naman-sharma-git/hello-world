collection = {1, 2, 3, 4}

print(collection)
print(type(collection))

collection = {1, 2, 3, 4, "hello", "world", "python"}

print(collection)
print(type(collection))


collection = {1, 2, 2, 2, "hello", "world", "hello"}     #python ignore the dublicate value in set

print(collection)
print(type(collection))


collection = {1, 2, 2, 2, "world", "world", "python", "python"}

print(collection)
print(len(collection))       #python also ignore the dublicate no in length



collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

print(collection)

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)

print(collection)


collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
#collection.remove(6)

print(collection)



collection = set()
collection.add(1)
collection.add(2)
collection.add("srmuniversity")
collection.add((1, 3, 2))
collection.add("namansharma")

print(collection)


collection = set()
collection.add(1)
collection.add(2)
collection.add("srmuniversity")
collection.add((1, 3, 2))
collection.add("namansharma")

collection.clear()
print(len(collection))


collection = {"hello", "namansharma", "coding", "python", "world"}

print(collection.pop())
print(collection.pop())

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))     #{1, 2, 3, 4}
print(set1)
print(set2)


set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.intersection(set2))


dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}


print(dictionary)



subjects = {
    "python", "java", "c++", "c", "python", "javascript", "java", "python"
}

print(len(subjects))