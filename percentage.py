/* https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen */

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    op= list(student_marks.get(query_name))

    suma=count=0

    for i in op:

        suma=suma+i
        count=count+1
    
    print ("{:.2f}".format(suma/count))

    
