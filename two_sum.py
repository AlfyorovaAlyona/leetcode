from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    def two_sum_hash(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            dictionary[nums[i]] = i
        for j in range(len(nums)):
            num = target - nums[j]
            if num in dictionary.keys() and dictionary[num] != j:
                return [j, dictionary[num]]
        return []

if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    sol = Solution()
    print(sol.two_sum_hash(nums, target))
