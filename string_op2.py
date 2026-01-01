Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# counting substring from a string
#count()
#string.count(substring)
s1 = "we are learning python . python is fun."
s2 = "python"
print(f"occurrences of {s2} is {s1.count(s2)}")



s1 = "we are learning python . python is fun."
s2 = "e"
print(f"occurrences of {s2} is {s1.count(s2)}")


s1 = "we are learning python . python is fun."
s2 = " "
print(f"occurrences of space is {s1.count(s2)}")


#changing case of string
#upper(), lower(), tittle(), capatilize()


s1 = "python"
print(s1.upper())


s1 = "python3.13"
print(s1.upper())


s1 = "python3.13"
print(s1.upper())
print(s1.lower())

s1 = "we are learing python is 2026"
... print(s1.upper())
... print(s1.lower())
... 
... 
... s1 = "we are learning python is 2026"
... print(s1.upper())
... print(s1.lower())
... print(s1.title())
... 
... 
... 
... s1 = "we are learning python is 2026"
... print(s1.upper())
... print(s1.lower())
... print(s1.title())
... print(s1.capitalize())
... 
... 
... #starting and learning of a string
... 
... 
... s1 = "we are learning python"
... 
... 
... #startswith()
... #string.startswith(substring)
... 
... 
... print(s1.startswith("w"))
... 
... print(s1.startswith("we are"))
... 
... print(s1.startswith(" are"))
... 
... 
... print(s1.endswith("python"))
... 
... print(s1.endswith("pytho"))
... 
