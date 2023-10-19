class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store = set()

        for n in nums:
            if n in store:
                store.remove(n)
                continue
            
            store.add(n)
        
        return next(iter(store))
