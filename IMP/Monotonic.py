An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105

ANS:

def ismonotonic(a):
    
    increasing= False
    decreasing= False
    
    for i in range (0, len(a)-1):
        
        if(a[i]> a[i+1]):
            
            decreasing= True
            
        if (a[i]< a[i+1]):
            
            increasing= True
    
    if (decreasing== True and increasing==True):
        
        return True
    
    return False
    
    
if (__name__=="__main__"):
    
    print(ismonotonic([1,2,8,2]))
