
# Attempt #1: Brute Force O(n^2)
# Notable Mention 1: Python count method counts the number of instances of an element in an array
# Notable Mention 2: Python index method returns the index of the first matched element found in the array  

def removeDuplicates(self, nums: List[int]) -> int:
    for num in nums:
        while nums.count(num) > 1:
            indexNum = nums.index(num)
            indexNum += 1
            nums.remove(nums[indexNum])

    return len(nums)


# Attempt #2 O(n) 
# Notable Mention 1: Two pointer method can reduce the need for an extra loop
# Notable Mention 2: del method can be used to delete a specific index in an array

def removeDuplicates(self, nums: List[int]) -> int:
    i = 1
    j = 0

    while i < len(nums):
        if nums[i] == nums[j]:
            del nums[j]
        else:
            i += 1
            j += 1

    return len(nums)
        
