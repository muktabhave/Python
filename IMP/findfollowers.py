def findfollowers(a):
    
    dict1= dict()
    
    for i in a:
        
        for j in range(len(i)):
            
            if (i[j] in dict1):
                
                val= dict1.get(i[j])
            
                dict1[i[j]]= val+1
            else:
                dict1[i[j]]= 0

    for key, value in dict1.items():
        
        print (key, value)
        



if (__name__=="__main__"):
    
    arr=[['D'],['A','B'],['A','C'],['C','A']]
    
    findfollowers(arr)
