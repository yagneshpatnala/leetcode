class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        result = []
        factorial = 1
        for i in range(1, n):
            factorial *= i

        k -= 1

        while numbers:
            index = k // factorial
            result.append(str(numbers[index]))
            numbers.pop(index)

            if numbers:
                k %= factorial
                factorial //= len(numbers)

        return ''.join(result)