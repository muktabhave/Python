Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104

ANS:


import math
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m=-math.inf
    s=-math.inf

    for i in range (0, n):
        if(arr[i]> m):
            m=arr[i]
        
    for i in range (0, n):
        if(arr[i]!=m and arr[i]>s):

            s=arr[i]
    
    print(s)


or_______________________________________________

class Solution:
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k - 1]
