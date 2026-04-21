class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        """
        the main difference between set and list 
        is that set stores distinct elements 
        so if we cast a list to a set
        and check if the length of this set 
        is less than the length of list 
        which means that the list contains duplicates  
        """