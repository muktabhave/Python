def primenos(lower, upper):

    for num in range(lower, upper+1):
   # all prime numbers are greater than 1
        if num > 1:
            flag= True
            
            for i in range(2, (num/2 +1)):
                
                if (num % i) == 0:
                    
		            flag= False
		            break
            
            if (flag== True):
                print(num)
            
if (__name__=="__main__"):

	primenos(1,10)
