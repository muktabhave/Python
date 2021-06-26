# find no of students enrolled either in english or in french but not both


if (__name__=="__main__"):

    e=int(input())
    eset= set(input().split())
    f=int(input())
    fset=set(input().split())

    l= fset^eset
    count=0
    
    print(len(l))
