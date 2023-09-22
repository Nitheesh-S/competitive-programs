class Solution:
    def removeDuplicates(self, s: str) -> str:
        result = ''
        for c in s:
            try:
                if result[-1] == c:
                    result = result[:-1]
                else:
                    result += c
            except IndexError:
                result = c
        return result
        