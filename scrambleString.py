#  Problem (Short)
# Given two strings s1 and s2, return True if s2 is a scrambled version of s1.
# Scrambling means:
# - Recursively split the string into two non-empty parts
# - Optionally swap the two parts
# - Continue this process on each substring

#  Intuition
# Try all possible split positions.
# For each split, check:
#   1. No Swap  → left matches left AND right matches right
#   2. Swap     → left matches right AND right matches left

# Use recursion + memoization to avoid recomputing same cases.

class Solution(object):
    def isScramble(self, s1, s2):
        memo = {}  # stores (a, b) → True/False

        def dfs(a, b):
            # If already computed, return stored result
            if (a, b) in memo:
                return memo[(a, b)]

            # If strings are equal → valid scramble
            if a == b:
                return True

            # If characters don’t match → impossible
            if sorted(a) != sorted(b):
                return False

            n = len(a)

            # Try all split positions
            for i in range(1, n):

                #  Case 1: No swap
                # a[:i] matches b[:i] AND a[i:] matches b[i:]
                if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True

                #  Case 2: Swap
                # a[:i] matches b[n-i:] AND a[i:] matches b[:n-i]
                if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):
                    memo[(a, b)] = True
                    return True

            # If no split works → not a scramble
            memo[(a, b)] = False
            return False

        return dfs(s1, s2)


# Summary:
# - Try every split
# - Check both swap & no-swap
# - Use memo to speed up
