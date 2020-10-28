class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        dict1={}
    
        for i in range (len(nums)):
        
            dict1[i]= nums[i]
    
        for j in dict1.keys():
        
            comp=target-dict1[j]
        
            if (comp in dict1.values()):
            
                return (j, int(dict1[comp]))
