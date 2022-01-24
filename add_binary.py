

class Solution:
    def add_binary(self, a: str, b: str) -> str:
        binary1 = '0b' + a
        binary2 = '0b' + b
        binary_sum = bin(int(binary1, 2) + int(binary2, 2))
        return str(binary_sum)[2:]


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    sol = Solution()
    print(sol.add_binary(a, b))
