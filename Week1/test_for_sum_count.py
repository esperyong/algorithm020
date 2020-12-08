class Solution(object):

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        A = sorted(A)
        B = sorted(B)
        C = sorted(C)
        D = sorted(D)

        a,b,c,d = 0,0,0,0
        n = len(A)
        ret = 0

        for a in range(n):
            while a > 0 and a < n and A[a - 1] == A[a]:continue 
            for b in range(n):
                while b > 0 and b < n and B[b - 1] == B[b]:continue
                for c in range(n):
                    while c > 0 and c < n and C[c - 1] == C[c]:continue 
                    for d in range(n):
                        while d > 0 and d < n and D[d - 1] == D[d]:continue
                        s = A[a] + B[b] + C[c] + D[d]
                        if s == 0:
                            ret = ret + 1
                        elif s > 0:
                            break
        return ret


    def fourSumCountHash(self, A, B, C, D):
        n = len(A)
        m = {}
        ret = 0
        for a in range(n):
            for b in range(n):
                sab = A[a] + B[b]
                if sab in m:
                    m[sab] = m[sab] + 1
                else:
                    m[sab] = 1

        for c in range(n):
            for d in range(n):
                scd = C[c] + D[d]
                if -scd in m:
                    ret = ret + m[-scd]

        return ret

                
def test():

    A = [1,2]
    B = [-2,-1]
    C = [-1,2]
    D = [0,2]

    s = Solution()

    ret = s.fourSumCount(A,B,C,D)
    assert ret == 2

    ret = s.fourSumCountHash(A,B,C,D)
    assert ret == 2

