class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(arr1)
        result = []
        
        # Add elements in arr2 order
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]  # Remove from counter
        
        # Add remaining elements in sorted order
        for num in sorted(count.keys()):
            result.extend([num] * count[num])
        
        return result
        
# class Solution:
#     def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

#         def move_to_front(arr, target):
#             targets = [x for x in arr if x == target]
#             others = [x for x in arr if x != target]
#             return targets + others

#         arr1.sort()
#         for n in reversed(arr2):
#             arr1 = move_to_front(arr1, n)
#         return arr1
