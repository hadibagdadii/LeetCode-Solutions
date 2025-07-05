class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total_poisoned = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration > timeSeries[i + 1]:
                total_poisoned += timeSeries[i + 1] - timeSeries[i]
            else:
                total_poisoned += duration
        total_poisoned += duration
        return total_poisoned
