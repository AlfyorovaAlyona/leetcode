from typing import Optional
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict.keys() and abs(i-dict[nums[i]] <= k):
                return True
            dict[nums[i]] = i
        return False

if __name__ == '__main__':
    nums = [1,2,3,1,2,3]
    k = 2
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))



