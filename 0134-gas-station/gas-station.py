class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start_index = 0
        current_tank = 0
        
        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            
            # If we run out of gas, reset the start position to the next station
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0
                
        return start_index