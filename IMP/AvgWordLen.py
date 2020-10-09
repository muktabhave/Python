import math

s= "I am Muks here"

l=s.split()

totlen, count=0,0

for i in l:
    
    totlen=totlen+len(i)
    
    count=count+1
    

print(totlen/count)
