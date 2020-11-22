# Find mismatching (not common) words from two given sentences

string1= "Firstly this is the first string" 
string2= "Next is the second string"
res=[]

l1=(string1.split())+string2.split()

for i in l1:
    if (l1.count(i)==1):
        res.append(i)

print res
