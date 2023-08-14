class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        store = {}
        longest = 1
        
        def get_root(num):
            while store[num][0] != num:
                store[num][0] = store[store[num][0]][0]
                num = store[num][0]
            return num

        def union(a,b):
            nonlocal longest
            a_root = get_root(a)
            b_root = get_root(b)

            if a_root == b_root:
                return

            if store[a_root][1] < store[b_root][1]:
                store[a_root][0] = store[b_root][0]
                store[b_root][1] += store[a_root][1]

                longest = max(longest, store[b_root][1])
            else:
                store[b_root][0] = store[a_root][0]
                store[a_root][1] += store[b_root][1]

                longest = max(longest, store[a_root][1])

        for num in nums:
            if num in store:
                continue
            
            store[num] = [num, 1]

            if num+1 in store:
                union(num, num+1)
            if num-1 in store:
                union(num, num-1)
            
        return longest
            