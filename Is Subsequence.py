class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        if not s:
            return True
        for char in t:
            if char == s[s_pointer]:
                s_pointer += 1
                if s_pointer == len(s):
                    return True
        return False

# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         if s == "":
#             return True
#         for letter in t:
#             if letter == s[0]:
#                 s = s[1:]
#             if s == "":
#                 return True
#         return False
