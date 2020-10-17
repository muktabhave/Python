class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j=0,0
        
        tmp=[]
        
        while(i<m and j<n):
            
            if (nums1[i]<= nums2[j]):
                
                tmp.append(nums1[i])
                i=i+1
            else:
                
                tmp.append(nums2[j])
                j=j+1
                
        while(i<m):
            tmp.append(nums1[i])
            i=i+1
        
        while(j<n):
            tmp.append(nums2[j])
            j=j+1
        
        k=0
        
        for k in range (len(nums1)):
            
            nums1[k]=tmp[k]
        
        return nums1
