#equilibrium is the index in array who has sum of its left side elements equal to sum of its right side elements

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

 

Example 1:

Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Example 2:

Input: root1 = [], root2 = []
Output: true
Example 3:

Input: root1 = [], root2 = [1]
Output: false
 

Constraints:

The number of nodes in each tree is in the range [0, 100].
Each tree will have unique node values in the range [0, 99].

ANS:

def equilibrium(a):
    
    n= len(a)
    leftsum=[0]*n
    
    for i in range (1,n):
        leftsum[i]=a[i-1]+leftsum[i-1]
    
    rightsum=[0]*n
    
    i=n-2
    
    while(i>=0):
        rightsum[i]=rightsum[i+1]+a[i+1]
        
        if (rightsum[i]==leftsum[i]):
            return i
        
        i=i-1
    
    return "not found"

if (__name__=="__main__"):
    
    print(equilibrium([10,20,10,-30,60]))
