class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        dict1={}
    
        for i in range (len(nums)):
        
            dict1[i]= nums[i]
    
        for j in dict1.keys():
        
            comp=val-dict1[j]
        
            if (comp in dict1.values()):
            
                for x, y in dict1.items():
                    if (comp==y):
                        return (j,x)
