class Solution:
    def isHappy(self, n: int) -> bool:
        sum_squared = 0
        sums = [n]
        if n == 1:
            return True
        while n != 1:
            for digit in str(n):
                sum_squared += int(digit)**2
            if sum_squared == 1:
                return True
            n = sum_squared
            if n in sums:
                return False
            sums.append(sum_squared)
            sum_squared = 0

if __name__ == '__main__':
    sol = Solution()
