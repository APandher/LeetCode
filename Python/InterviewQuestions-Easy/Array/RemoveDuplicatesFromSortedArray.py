
nums = [0,0,1,1,1,2,2,3,3,4]

# Attempt #1: Brute Force 
# Notable Mention 1: Python count method counts the number of instances of an element in an array
# Notable Mention 2: Python index method returns the index of the first matched element found in the array  
def removeDuplicates(nums):
    for i in nums:
        while nums.count(i) > 1:
            indexNum = nums.index(i)
            indexNum += 1
            nums.remove(nums[indexNum])

    return len(nums)


print(removeDuplicates(nums))

