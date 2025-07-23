class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
            
        intervals.sort(key=lambda interval: interval[0])
        result = []
        
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            
            while i + 1 < len(intervals) and end >= intervals[i + 1][0]:
                i += 1
                end = max(end, intervals[i][1])
            
            result.append([start, end])
            i += 1
        
        return result
