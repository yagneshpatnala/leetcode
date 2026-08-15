class Solution:
    def longestSubsequence(self, nums):
        total_xor = 0

        for num in nums:
            total_xor ^= num

        # If XOR of all elements is non-zero,
        # we can take the entire array.
        if total_xor != 0:
            return len(nums)

        # If total XOR is 0, remove any non-zero element.
        for num in nums:
            if num != 0:
                return len(nums) - 1

        # All elements are 0
        return 0