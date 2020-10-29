# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
# Sample Input

# 2 2
# 1 2
# 3 4
# Sample Output

# [[1 3]
#  [2 4]]
# [1 2 3 4]

import numpy

n , m = input().split();
a = [];
for i in range(int(n)):
    my_array = input().split();
    a.append(my_array);
lis1 = numpy.array(a,int);
print(numpy.transpose(lis1))
print(lis1.flatten())

