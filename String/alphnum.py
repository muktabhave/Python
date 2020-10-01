# Find if the string contains number, character and upper lowercase

if __name__ == '__main__':
    s = input()

    alpha=False
    digit= False
    upper= False
    lower= False
    alphanum= False
    
    for i in s:
        
        if (i.isalpha()):
            
            alpha= True
            
            if (i.isupper()):
                
                upper= True
            elif (i.islower()):
                
                lower= True
        elif (i.isdigit()):
            
            digit=True
    
    print(alpha==True or digit== True)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)

  # Alternate approach

if __name__ == '__main__':
    
    str='123'

    print any(c.isalnum()  for c in str)
    print any(c.isalpha() for c in str)
    print any(c.isdigit() for c in str)
    print any(c.islower() for c in str)
    print any(c.isupper() for c in str)
