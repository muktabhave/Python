Method#2 using reverse of string

def palindrome(s): 
  return (s==s[::-1])
  
if(__name__=="__main__"):
    
    print(palindrome("saliilas"))


#Method-3: using reversed function

def palindrome(s): 
  return (s==''.join(reversed(s)))
  
if(__name__=="__main__"):
    
    print(palindrome("saliilas"))
