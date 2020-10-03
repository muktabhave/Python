# Accept multiple input lines and find if a set is subset of other set

if (__name__== "__main__"):

    n= int(input())
    a= []
    aele= []
    b= []
    bele=[]

    for i in range(n):
        aele=int(input())

        a=set(map( int, input().split()))

        bele=int(input())

        b= set(map( int, input().split()))

        print(a.issubset(b))

    
