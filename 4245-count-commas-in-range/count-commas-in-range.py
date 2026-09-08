class Solution:
    def countCommas(self, n):
        count = 0

        # Numbers from 1,000 to n
        if n >= 1000:
            count += n - 999

        return count