import math
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr= list(arr)
    m=-math.inf
    s=-math.inf

    for i in range (0, n):
        if(arr[i]> m):
            m=arr[i]
        
    for i in range (0, n):
        if(arr[i]!=m and arr[i]>s):

            s=arr[i]
    
    print(s)
