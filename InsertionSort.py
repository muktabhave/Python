def InsertionSort(a):
    n=len(a)-1
    
    for i in range(n):
        
        j=i
        while(j>=0):
            if(a[j+1]<a[j]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
            
            j=j-1
            
    return a

if (__name__=="__main__"):
    
    print(InsertionSort([2,10,5,8,3]))
