# program to giev two elements of array having maximum multiplication

You are given an array of integers nums.

Choose two different indices i and j of that array.

Return the maximum value of (nums[i] - 1) * (nums[j] - 1).

 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12
 

Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3


ANS:


import math

def multiplication(a):
    
    maxe=0
    secmax=0
    
    mine=0
    
    secmin=0
    
    
    for i in range (0,len(a)):
        
        if(a[i]>0):
        
            if (a[i]>= maxe):
            
                secmax= maxe
                maxe= a[i]
            elif (a[i]>= secmax):
                
                secmax= a[i]

        else:
            
            if(a[i]<= mine):
                
                secmin= mine
                mine= a[i]
            elif (a[i]<=secmin):
                secmin=a[i]
                    
    
    if ((maxe*secmax)> (mine*secmin)):
        
        return maxe,secmax
    
    else:
        return mine, secmin
        
if (__name__=="__main__"):
    
    print(multiplication([-9,-2,-2,9,6]))
