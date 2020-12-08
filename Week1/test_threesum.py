

class Solution(object):
    """
    给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
    请你找出所有满足条件且不重复的三元组。
    注意：答案中不可以包含重复的三元组。
    https://leetcode-cn.com/problems/3sum/
    """


    def threeSumBruteForce(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums = sorted(nums)
        ans = []

        for first in range(n):
            if first == 0 or nums[first] != nums[first -1]:
                for second in range(first+1, n):
                    if second == first + 1 or nums[second] != nums[second - 1]:
                        for third in range(second+1, n):
                            if third == second + 1 or nums[third] != nums[third - 1]:
                                if nums[first] + nums[second] + nums[third] == 0:
                                    ans.append([ nums[first], nums[second], nums[third] ])

        return ans


    def threeSumBruteForceHash(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """


        return [
            [-1, 0, 1],
            [-1, -1, 2]
        ]

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        双指针夹逼法
        """
        nums = sorted(nums)
        n = len(nums)
        res = []

        for first in range(n-2):
            if nums[first] > 0:break
            if first > 0 and nums[first] == nums[first-1]:continue
            second, third = first + 1, n - 1
            while second < third:
                s = nums[first] + nums[second] + nums[third]
                if s < 0:
                    second = second + 1
                    while second < third and nums[second - 1] == nums[second]:second = second + 1
                elif s > 0:
                    third = third - 1
                    while second < third and nums[third + 1] == nums[third]:third = third - 1
                else:
                    res.append( [nums[first], nums[second], nums[third]] )
                    second = second + 1
                    third = third - 1
                    while second < third and nums[second - 1] == nums[second]:second = second + 1
                    while second < third and nums[third + 1] == nums[third]:third = third - 1

        return res

    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ret = []
        nums = sorted(nums)
        n = len(nums)

        for first in range(0,n - 2):
            if nums[first] > 0:break
            if first > 0 and nums[first] == nums[first-1]:continue

            second,third = first + 1,n - 1

            print(first, second, third)

            while second < third:
                s = nums[first] + nums[second] + nums[third]
                print ([nums[first],nums[second],nums[third]])
                if s > 0:
                    third = third - 1
                    while second < third and nums[third] == nums[third+1]:third=third-1
                elif s < 0:
                    second = second + 1
                    while second < third and nums[second] == nums[second-1]:second=second+1
                else:
                    ret.append([nums[first],nums[second],nums[third]])
                    second = second + 1
                    third = third - 1
                    while second < third and nums[third] == nums[third+1]:third=third-1
                    while second < third and nums[second] == nums[second-1]:second=second+1


        return ret

def test():

    nums = [-1, 0, 1, 2, -1, -4,0,0]

    s = Solution()

    for ss in s.threeSum(nums):
        assert sum(ss) == 0 and len(ss) != 0

    for ss in s.threeSumBruteForce(nums):
        assert sum(ss) == 0


    nums = [-1, 0, 1, 2, -1, -4]
    ret = s.threeSum2(nums)

    assert len(ret) != 0

    for ss in ret:
        assert sum(ss) == 0



