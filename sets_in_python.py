Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
KeyboardInterrupt
nums = {1, 2, 3, 0, -3}
... 
... #membership operator -in, not in
... print(0 in nums)
... print(10 not in nums)
... print(10 in nums)
... 
... 
... nums_1 = {1, 2, 3, 0, -5}
... nums_2 = {6, 8}
... print(nums_1 , nums_2)
... 
... weekdays = ("mon", "tue", "wed", "thu", "fri")
... weekdays = set(weekdays)
... print(weekdays)
... 
... # mutable or immutable?
... set1 = {2, 0, -4}
... print(set1)
... #add()
... set1.add(5)
... print(set1)
... 
... #remove
... set1.remove(0)
... print(set1)
... 
... 
... #add
... set1.add(0)
... print(set1)
... 
... 
... #add
... set1.add(0)
... print(set1)     #no change if we have the same number in set
... 
... 
... #discard
... set1.discard(10)
... print(set1)
... 
