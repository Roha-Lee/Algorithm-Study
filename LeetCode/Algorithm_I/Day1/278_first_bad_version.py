# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        origin = 1
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid - 1
                origin = mid
            else:
                start = mid + 1
        return origin