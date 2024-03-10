class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        total = 1
        for n in nums:
            if n == 0:
                if zeros == 0:
                    zeros = 1
                    n = 1
                elif zeros == 1:
                    zeros = 2
                    
            total *= n
        result = [] 
        if zeros == 1: 
            for n in nums:
                if n == 0:
                    result.append(total)
                else:
                    result.append(0) 
        elif zeros == 2:
            result = [0] * len(nums)
        else: 
            for n in nums:
                result.append(int(total/n))
        
        return result
        