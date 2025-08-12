class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        char_count = Counter(s)
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        return -1

# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         char_list = list(s)
#         used = set()
#         counter = 0
#         while first_char := (char_list.pop(0) if char_list else None):
#             if first_char not in char_list and first_char not in used:
#                 return counter
#             counter += 1
#             used.add(first_char)
#         return -1
