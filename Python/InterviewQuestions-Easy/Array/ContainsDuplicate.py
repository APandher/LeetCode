# Attempt #1: O(n) complexity
# Tricks: Using a Dictionary to speed up look up time
# Tricks: Using "if key in dict" is O(n) and using "dict.get(key)" is O(1) 
class Solution(object):
    def containsDuplicate(self, nums):
        
        placeholder = {}
        
        for i in nums:
            if placeholder.get(i):
                return True
            else:
                placeholder[i] = 1
                
        return False
