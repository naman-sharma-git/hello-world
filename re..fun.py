import re

message = "i am learning the python language of 3.13 version and the number is 213, 54, 34"

object = re.search('13', message)
print(object)

if re.search('13', message):
    print("found")

else:
    print("not found")

print(message[34:39])

message = " i am naman and i will becoome rech and i will become , today i am learning python in 3.12 version"

object = re.search('[0-9][0-9]' , message)
print(object)


object = re.search('[0-9].[0-9]' , "house number is 231/as")
print(object)



object = re.search('[0-9].' , "house number is 231/as")
print(object)


object = re.search('[0-9][.][0-9][0-9]' , message)
print(object)

s1 = "python is a programing language and the version is python4.31 yeah" 


pat = r"[a-z][a-z][a-z]\d"
match_obj = re.search(pat,s1)
print(match_obj)

pat = r"[a-z][a-z][a-z]\D"  
match_obj = re.search(pat,s1)
print(match_obj)

sub = """hi there we are learning the python language.
so i can make the website
"""
#\s is use to count the space 
pat = r"[a-z][a-z][a-z]\s"
match_obj = re.search(pat,s1)
print(match_obj)

#\S is use to don't count the space 
pat = r"[a-z][a-z][a-z]\S"
match_obj = re.search(pat,s1)
print(match_obj)

#\w is use for 0-9 a-z A-Z _ 
pat = r"[a-z][a-z][a-z]\w"
match_obj = re.search(pat,s1)
print(match_obj)

#\w is use for 0-9 a-z A-Z _ 
pat = r"[a-z][a-z][a-z]\W"
match_obj = re.search(pat,s1)
print(match_obj)

