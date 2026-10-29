
class Solution:
    def containDup(self, nums: list[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
            return False