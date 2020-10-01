def solve(s):

    l=s.split(' ')
    p=[]

    for i in l:
        p.append(i.capitalize())
    
    return (' '.join(p))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
