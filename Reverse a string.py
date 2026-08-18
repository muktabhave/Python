Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

ANS:

#Method-1:

def reverse(s): 
  return s[::-1]
  
if(__name__=="__main__"):
    
    print(reverse("Geeksforgeeks"))

#Method-2:

def reverse(s): 
  return ''.join(reversed(s))
  
if(__name__=="__main__"):
    
    print(reverse("Geeksforgeeks"))
    
#Method-3:
  
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
if(__name__=="__main__"):
    
    print(reverse("Geeksforgeeks"))
