import math
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m=-math.inf
    s=-math.inf

    for i in range (0, n):
        if(arr[i]> m):
            m=arr[i]
        
    for i in range (0, n):
        if(arr[i]!=m and arr[i]>s):

            s=arr[i]
    
    print(s)
