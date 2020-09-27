#Method-1: cheching first char with last

def palindrome(s): 
    i=0
    j=len(s)-1
  
    while(i<=j):
        if(s[i]==s[j]):
            i+=1
            j-=1
        else:
            return False

    return True  
if(__name__=="__main__"):
    
    print(palindrome("saliilas"))

#Method-2 using reverse of string

def palindrome(s): 
  return (s==s[::-1])
  
if(__name__=="__main__"):
    
    print(palindrome("saliilas"))


#Method-3: using reversed function

def palindrome(s): 
  return (s==''.join(reversed(s)))
  
if(__name__=="__main__"):
    
    print(palindrome("saliilas"))
