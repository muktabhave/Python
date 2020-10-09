# Hello World program in Python

def CompareString(itemlist, query):
    
    for string in itemlist:
        
        if(len(string)== len(query)):
            
            i=0
            isvalid= False
            
            while (i< len(string)):
                
                if(string[i]== query[i] or query[i]=="."):
                    
                    isvalid= True
                    i=i+1
                else:
                    isvalid= False
                    break
                    
            if(isvalid== True):
                return True
    
    return False
    
if (__name__=="__main__"):
    
    print(CompareString(['cat', 'bat', 'rat'], 'ra.'))
                
                
