class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for x in nums:
            if x in nums_set:
                return True
            nums_set.add(x)
        return False