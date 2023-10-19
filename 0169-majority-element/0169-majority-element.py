class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        store = {}

        if len(nums) <= 2:
            return nums[0]

        mid = len(nums) / 2
        for n in nums:
            if n in store:
                store[n] += 1
                if store[n] >= mid:
                    return n
            else:
                store[n] = 1
        
        return -1
