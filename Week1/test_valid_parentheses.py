class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {
               ']':'[', 
               '}':'{', 
               ')':'('
            }

        stack = []

        for c in s:
            if c in dic.values():
                stack.append(c)
            elif c in dic.keys():
                if stack == [] or dic[c] != stack.pop():
                    return False
            else:
                return False

        return len(stack) == 0

def test():

    s = '{({})}'
    s2 = '({})}'

    so = Solution()

    assert so.isValid(s) is True
    assert so.isValid(s2) is False


