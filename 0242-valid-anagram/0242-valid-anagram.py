class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        store = {}
        for c in s:
            try:
                store[c] += 1
            except KeyError:
                store[c] = 1
        
        for c in t:
            try:
                store[c] -= 1
            except KeyError:
                return False
            
            if store[c] == 0:
                del store[c]
        
        return not bool(store)