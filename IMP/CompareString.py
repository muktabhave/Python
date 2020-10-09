def CompareString(itemlist, query):
    
    for string in itemlist:
        
        if(len(string)== len(query)):
            
            i=0
            isvalid= True
            
            while (i< len(string)):
                
                if(string[i]!= query[i] and query[i]!="."):
                    
                    isvalid= False
                    break
                else:
                    i=i+1
                    
            if(i==len(string)):
                return True
    
    return False
    
if (__name__=="__main__"):
    
    print(CompareString(['cat', 'bat', 'rat'], 'r..'))
                
