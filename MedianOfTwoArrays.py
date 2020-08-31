class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = sorted(nums1 + nums2)
        
        size = len(merged_list)
        
        if size % 2 != 0:
            median = merged_list[floor(size/2)]
        else:    
            median = (merged_list[floor(size/2)] + merged_list[floor(size/2)-1])/2.0
            
        return median
