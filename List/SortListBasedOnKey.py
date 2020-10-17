# Leetcode- 937. Reorder Data in Log Files

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def getkey (log):
    
            id, rest= (log.split(" ", maxsplit=1))
    
            if (rest[0].isalpha()):
    	        return (0, rest, id)
            else:
    	        return (1,)

        return sorted(logs, key= getkey)  
