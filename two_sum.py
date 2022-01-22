from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    sol = Solution()
    print(sol.two_sum(nums, target))
