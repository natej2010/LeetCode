class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:   
        nums.sort()
        sum_ = nums[0] + nums[1] + nums[2]
        closest = {'sum': sum_, 'diff': abs(target - sum_)}
        i = 0
        
        while i < len(nums) - 2:
            if i != 0 and nums[i] == nums[i-1]:
                i += 1
                continue
                
            j = i + 1
            k = len(nums) - 1 
            
            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                
                if sum_ > target:
                    k -= 1
                elif sum_ < target:
                    j += 1
                else:
                    while j < k and nums[j] == nums[j+1]: j += 1
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    j += 1
                    k -= 1
                    
                if abs(target - sum_) < closest['diff']:
                    closest = {'sum': sum_, 'diff': abs(target - sum_)}
            i += 1
        
        return closest['sum']
