# 202. Happy Number
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is defined by the following process:
# - Start with any positive integer.
# - Replace the number by the sum of the squares of its digits.
# - Repeat the process until:
#     * the number becomes 1 → happy number
#     * OR it loops endlessly → not a happy number
#
# Return True if n is a happy number, otherwise False.
#
# Example 1:
# Input: n = 19
# Output: True
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
# Example 2:
# Input: n = 2
# Output: False
#
# Constraints:
# 1 <= n <= 2^31 - 1


class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1
