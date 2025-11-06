Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... s1 = "hello world"
... """
... print(s1)
... 
... #length of string
... print(len(s1))
... 
... 
... #indexing
... print("first char", s1[0])
... print("last char", s1[-1])"""
... 
... """syntax of indexing: string[index]
... syntax of slicing: string[start:end:stop]
... - start: starting index at which the slicing operation starts
... -end: ending index at which the slicing stop (exclusive)
... -step: integer that specifies the step for the slicing
... """
... print(s1[2:7:1])
... print(s1[2:9:2])
... print(s1[1:12:3])
... s1_slice = s1[1:12:4]
... print(s1_slice)
