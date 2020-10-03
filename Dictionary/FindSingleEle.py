# https://www.hackerrank.com/challenges/py-the-captains-room/problem?h_r=next-challenge&h_v=zen

if (__name__=="__main__"):

    k= int(input())
    arr= list(map(int,input().split()))
    dict1=dict()

    for i in arr:

        if (dict1.get(i)):
            val=dict1.get(i)
            dict1[i]=val+1
        else:
            dict1[i]=1
    
    for key, value in dict1.items():

        if(value==1):
            print(key)
