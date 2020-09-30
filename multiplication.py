# program to giev two elements of array having maximum multiplication
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
                print ("maxe", maxe)
            
                print ("secmax",secmax)
        else:
            
            if(a[i]<= mine):
                
                secmin= mine
                mine= a[i]
            elif (a[i]<=secmin):
                secmin=a[i]
                
                
    print(maxe,secmax, mine, secmin)
    
    if ((maxe*secmax)> (mine*secmin)):
        
        return maxe,secmax
    
    else:
        return mine, secmin
        
if (__name__=="__main__"):
    
    print(multiplication([-9,-2,-2,9,6]))
