# find out if A is supersets of a all given sets

if (__name__=="__main__"):
    a= set(map(int, input().split()))

    n= int(input())

    res= True
    for i in range (n):
        b= set(map(int, input().split()))

        res= (res and a.issuperset(b))
    
    print (res)   
