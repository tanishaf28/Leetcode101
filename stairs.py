"""
Climbing Stairs (LeetCode #70)
Problem Statement
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps.
Return the number of distinct ways to reach the top.

🧪Examples
Example 1
Input: n = 2
Output: 2

Explanation:
1 + 1
2
Example 2
Input: n = 3
Output: 3

Explanation:
1 + 1 + 1
1 + 2
2 + 1
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev1, prev2 = 2, 1  # ways for step 2 and step 1
        
        for _ in range(3, n + 1):
            curr = prev1 + prev2
            prev2 = prev1
            prev1 = curr
        
        return prev1
