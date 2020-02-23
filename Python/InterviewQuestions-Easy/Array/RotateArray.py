
#Slow solution O(2n) and O(n) Space Complexity
#Trick: Modulo operator is important for not allowing the loop to go out of range
def rotate(self, nums: List[int], k: int) -> None:

    if len(nums) == 1 or k == 0:
        return

    auxillary = []
    j = len(nums) - k

    for i in range(len(nums)):
        auxillary.append(nums[j])
        j = (j + 1) % len(nums)

    for i in range(len(nums)):
        nums[i] = auxillary[i] 

# TODO Repeat question using only O(1) Space Complexity
    





