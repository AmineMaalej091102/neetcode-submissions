class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = 0
        c = []
        for b in nums:
            if b == 1:
                a += 1
            else:
                c.append(a)
                a = 0
        c.append(a)
        return max(c)