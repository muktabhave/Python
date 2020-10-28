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
