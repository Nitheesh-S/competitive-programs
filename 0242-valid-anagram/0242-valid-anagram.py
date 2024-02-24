class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        store = {}
        
        for c in s:
            if c not in store:
                store[c] = 0
            store[c] += 1
        
        for c in t:
            if c not in store:
                return False
            
            if store[c] == 0:
                return False
            
            if store[c] == 1:
                del store[c] 
                continue
            
            store[c] -= 1
            
        
        if len(store) > 0:
            return False
        
        return True