class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = nums.pop(0)
        index = 0
        length = len(nums)
        
        while index < length:
            other_number = target - i
              
            if other_number in nums:
                return [index, nums.index(other_number)+index+1]
            
            i = nums.pop(0)
            index = index + 1
