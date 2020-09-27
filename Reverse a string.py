def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
if(__name__=="__main__"):
    
    print(reverse("Geeksforgeeks"))
