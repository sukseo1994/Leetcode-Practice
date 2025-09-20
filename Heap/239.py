class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque() 
        ans = [] 
        for i in range(len(nums)):
            while que and i-que[0][1] >= k:
                que.popleft()
            while que and que[-1][0] < nums[i]:
                que.pop()
            
            que.append((nums[i], i))
            if i >= k-1:
                ans.append(que[0][0])
        return ans 
