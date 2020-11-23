

class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = []
        m = {}
        i = 0

        for num in nums:
            s = target - num
            if s in m:  
                return [i, m[s]]
            m[num] = i
            i = i + 1

        return [] 

    def twoSum2(self, nums, target):
        m = {}
        for i, num in enumerate(nums):
            s = target - num
            if s in m:
                return [i, m[s]]
            m[num] = i

        return []

def test():

    nums = [2, 7, 11, 15]
    target = 9

    s = Solution()

    assert sorted(s.twoSum(nums, target)) == [0, 1]
    assert sorted(s.twoSum2(nums, target)) == [0, 1]





