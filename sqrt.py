"""
Sqrt(x) (LeetCode #69)
Problem Statement

Given a non-negative integer x, return the square root of x rounded down to the nearest integer.

The returned integer should also be non-negative.
You must NOT use built-in exponent functions like:
pow(x, 0.5)
x ** 0.5
Examples
Example 1
Input: x = 4
Output: 2

Explanation:
√4 = 2 → exact value

Example 2
Input: x = 8
Output: 2

Explanation:
√8 ≈ 2.828 → rounded down = 2

Constraints
0 <= x <= 2^31 - 1
Approach (Binary Search)

We use binary search because:

The square root lies between 0 and x
We try a mid value and compare:
mid * mid with x
Key Idea:
If mid * mid <= x, move right (store answer)
Else, move left
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 1, x // 2
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
