def validateip(ip):
    
    itemlist= ip.split('.')
    
    if(len(itemlist)!=4):
        
        return False
    
    for item in itemlist:
        
        if not item.isdigit():
            
            return False
        
        integer= int(item)
        
        if(integer<0 or integer>255):
            
            return False
    return True
    
if (__name__== "__main__"):
    
    print(validateip("102.888.37.a"))
