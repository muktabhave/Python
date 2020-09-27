#Method-1:

def reverse(s): 
  return s[::-1]
  
if(__name__=="__main__"):
    
    print(reverse("Geeksforgeeks"))

#Method-2:
  
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
if(__name__=="__main__"):
    
    print(reverse("Geeksforgeeks"))
