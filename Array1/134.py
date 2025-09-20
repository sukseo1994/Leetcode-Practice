class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        idx = 0 
        cursum = 0
        totalsum = 0  
        for i in range(len(gas)):
            cursum += gas[i]-cost[i]  
            totalsum += gas[i]-cost[i] 
            if cursum < 0:
                idx = i + 1
                cursum = 0 
        return -1 if totalsum < 0 else idx 