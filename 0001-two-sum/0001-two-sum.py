class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i in range(len(nums)):
            diff =  target - nums[i]
            try:
                return [index_map[nums[i]], i]
            except KeyError:
                index_map[diff] = i