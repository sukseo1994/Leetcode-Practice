class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stck = [-1] 
        max_area = 0 

        for i in range(len(heights)):
            while stck and heights[stck[-1]]  > heights[i]:
                h = heights[stck.pop()]
                w = i - stck[-1] - 1
                area = h * w
                max_area = max(max_area, area)
            stck.append(i)
        return max_area