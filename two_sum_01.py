class Solution:
    '''
    def twoSum(self, nums: list, target: int):
        numbers = {}
        for key, n in enumerate(nums):
            if target-n in numbers:
                return [key, numbers[target-n]]
            numbers[n] = key
        return [-1, -1]
    ''' 
    # Second Version
    # also using dictioanries 
    # adding more comments
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        idx_map = {}
        for i in range(len(nums)):
            if target-nums[i] in idx_map:
                return [i, idx_map[target-nums[i]]]
            idx_map[nums[i]] = i
        return [-1, -1]
sol = Solution()
print(sol.twoSum([2,7,11,15],9))