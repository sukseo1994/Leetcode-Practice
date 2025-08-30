class Solution:
    def twoSum(self, nums: list, target: int):
        numbers = {}
        for key, n in enumerate(nums):
            if target-n in numbers:
                return [key, numbers[target-n]]
            numbers[n] = key
        return [-1, -1]
    
sol = Solution()
print(sol.twoSum([2,7,11,15],9))