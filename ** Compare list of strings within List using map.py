# 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/

def isAlienSorted( words, order ):
    order_map = {}
    
    for k in range (len(order)):
        order_map[order[k]]= k

    for i in range (len(words)-1):
        
        for j in range (len(words[i])):
            
            if (j>= len(words[i+1])):
                return False
            
            if (words[i][j]!= words[i+1][j]):
                
                if (order_map[words[i][j]]> order_map[words[i+1][j]]):
                    return False
                
                break
                
    return True    

if (__name__=="__main__"):
    print(isAlienSorted( ["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz" ))
