class solution(object):
    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevmap = {}
        for i, n in enumerate(nums):
            difference = target -n
            if difference in prevmap:
                return [prevmap[difference], i]
            prevmap[n] = i
            return []
