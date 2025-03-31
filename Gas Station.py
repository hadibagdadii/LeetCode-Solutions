class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, no solution exists
        if sum(gas) < sum(cost):
            return -1
        
        start = 0
        tank = 0
        
        for i in range(len(gas)):
            # Calculate net gas after visiting station i and moving to i+1
            tank += gas[i] - cost[i]
            
            # If we can't reach the next station, reset and try starting from the next station
            if tank < 0:
                start = i + 1
                tank = 0
        
        return start
