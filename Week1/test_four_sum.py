class Solution:
    def fourSum(self, nums, target):
        ret = []
        nums = sorted(nums)
        n = len(nums)
        if n < 4:return ret
        first = 0
        for first in range(n-3):
            if nums[first] + nums[first+1] + nums[first+2] + nums[first+3] > target:break
            if nums[first] + nums[n-1] + nums[n-2] + nums[n-3] < target:continue
            if first > 0 and first < n - 3 and nums[first] == nums[first-1]:continue
            for second in range(first+1, n-2):
                if nums[first] + nums[second] + nums[second+1] + nums[second+2] > target:break
                if nums[first] + nums[second] + nums[n-1] + nums[n-2] < target:continue
                if second>first+1 and second < n - 2 and nums[second] == nums[second-1]:continue
                i = second + 1
                j = n - 1

                while i < j:
                    s = nums[first] + nums[second] + nums[i] + nums[j]
                    if s == target:
                        ret.append([nums[first],nums[second],nums[i],nums[j]])
                        i = i + 1
                        j = j - 1
                        while i < j and nums[i] == nums[i-1]:i = i + 1
                        while i < j and nums[j] == nums[j+1]:j = j - 1
                    elif s < target:
                        i = i + 1
                        while i < j and nums[i] == nums[i-1]:i = i + 1
                    else:
                        j = j - 1
                        while i < j and nums[j] == nums[j+1]:j = j - 1

        return ret



def test():

    nums = [1, 0, -1, 0, -2, 2]

    target = 0

    s = Solution()

    ret = s.fourSum(nums,0)

    assert len( s.fourSum(nums, 0) ) == 3


    nums = [0, 0, 0, 0]
    ret = s.fourSum(nums, 0)

    assert len( ret ) == 1

