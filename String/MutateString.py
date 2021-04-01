# Change 6th character in a string

def mutate_string(string, position, character):
    
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return(''.join(string))

#string = string[:5] + "k" + string[6:]
#print string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Alternative:
    
# def mutate_string(string, position, character):
#     return (string[:position]+character+ string[position+1:])

# if (__name__=="__main__"):
#     string = input('enter string')
#     position=int(input('enter no'))
#     character=input('enter char')
#     print(mutate_string(string, position, character))
