
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)

        ret = 0

        for first in range(n):
            for second in range(first+1, n):
                area = min(height[first],height[second]) * (second - first) 
                ret = max(area, ret)
                



        return ret

    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        ret = 0

        first,second = 0,n-1

        while first < second:

            area = min(height[first], height[second]) * (second - first) 

            ret = max(area, ret)

            if height[first] < height[second]:
                first = first + 1
            else:
                second = second - 1

        return ret


def test():
    ss = [1,8,6,2,5,4,8,3,7]


    s = Solution()

    assert s.maxArea(ss) == 49
    assert s.maxArea2(ss) == 49
