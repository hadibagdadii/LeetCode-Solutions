class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        mindiff, result = float("inf"), []

        arr.sort()

        for i in range(1, len(arr)):
            mindiff = min(arr[i] - arr[i-1], mindiff)
        
        for i in range(1, len(arr)):
            if (arr[i] - arr[i-1]) == mindiff:
                result.append([arr[i-1], arr[i]])
        
        return result


# class Solution:
#     def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
#         arr.sort()
#         mindiff = float("inf")
#         result = []
        
#         for i in range(1, len(arr)):
#             diff = arr[i] - arr[i-1]
            
#             if diff < mindiff:
#                 mindiff = diff
#                 result = [[arr[i-1], arr[i]]]  # Reset result with new minimum
#             elif diff == mindiff:
#                 result.append([arr[i-1], arr[i]])  # Add to existing results
        
#         return result
