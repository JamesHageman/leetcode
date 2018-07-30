from typing import List


class Solution(object):
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        start = 0
        end = len(A) - 1
        m = (start + end) // 2
        while not (A[m - 1] < A[m] and A[m] > A[m + 1]):
            if A[m - 1] < A[m]:
                start = m
            else:
                end = m
            m = (start + end) // 2
        return m


s = Solution()
print(s.peakIndexInMountainArray([3, 4, 5, 4]))
