class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        a_to_z = [x for x in range(26)]
        
        for w in strs:
            a_to_z_cpy = [*a_to_z]
            for c in w:
                a_to_z_cpy[ord(c) - 97] += 1
            w_data = tuple(a_to_z_cpy)
            try:
                store[w_data].append(w)
            except KeyError:
                store[w_data] = [w]
        return list(store.values())
