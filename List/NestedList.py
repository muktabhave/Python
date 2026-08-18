Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and digits.

ANS:

#Print the name(s) of any student(s) having the second lowest grade in. 
#If there are multiple students, order their names alphabetically and print each one on a new line.

import math
if __name__ == '__main__':

    marks= dict()
    for i in range(int(input())):
        name = input()
        score = float(input())
        marks[name]= score
    
    v=marks.values()
    sec_small= sorted(list(set(v)))[1]

    sec_grade_names=[]

    for key, value in marks.items():

        if(value==sec_small):

            sec_grade_names.append(key)
    sec_grade_names.sort()
    
    for i in sec_grade_names:
        print(i)
