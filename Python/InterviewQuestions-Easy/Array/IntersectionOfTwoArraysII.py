#Starting to get more comfortable with dictionaries
# Done in O(n)
class Solution(object):
    def intersect(self, nums1, nums2):
        
        frequency_nums1 = {}
        
        intersection = []
        
        for num in nums1:
            if frequency_nums1.get(num):
                frequency_nums1[num] += 1
            
            else:
                frequency_nums1[num] = 1
                
        for num in nums2:
            if frequency_nums1.get(num) and frequency_nums1[num] > 0:
                intersection.append(num)
                frequency_nums1[num] -= 1
            
        return intersection
