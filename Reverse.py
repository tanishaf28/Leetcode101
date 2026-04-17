"""
leetcode 190: reverse Bits: Reverse bits of a given 32 bits signed integer.
"""
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
