class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a = []
        for b in nums[:]:
            if b == val:
                nums.remove(b)
            else:
                a.append(b)
        return len(nums) 