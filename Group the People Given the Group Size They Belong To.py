class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        buckets = {}
        keys = []
        
        # ✅ Your code - perfectly correct so far
        for index, size in enumerate(groupSizes):
            if size in buckets:
                buckets[size].append(index)
            else:
                buckets[size] = [index]
                keys.append(size)
        
        # 🔧 Missing: Split buckets into groups of correct size
        result = []
        for size in keys:  # Or just: for size in buckets.keys()
            people = buckets[size]
            
            # Split people into groups of 'size'
            for i in range(0, len(people), size):
                group = people[i:i + size]
                result.append(group)
        
        return result
