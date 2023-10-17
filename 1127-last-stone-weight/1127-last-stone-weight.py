class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s_stones = sorted(stones)

        while len(s_stones) > 1:
            *rest, x, y = s_stones

            if x == y:
                s_stones = rest
                continue
            
            if x != y:
                s_stones = sorted([*rest, y - x])
        
        if len(s_stones) == 1:
            return s_stones[0]
        return 0