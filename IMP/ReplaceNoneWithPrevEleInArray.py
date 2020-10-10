itemlist=  [1,None,2,3,None,None,5,None]

for i in range (len(itemlist)):
    
    if (itemlist[i]== None):
        
        itemlist[i]= itemlist[i-1]

print (itemlist)
    
