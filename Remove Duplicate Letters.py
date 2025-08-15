class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Count frequency of each character
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # Track which characters are already in result
        in_stack = set()
        stack = []
        
        for char in s:
            # Decrease count as we process each character
            count[char] -= 1
            
            # Skip if already in result
            if char in in_stack:
                continue
            
            # Remove characters from stack if:
            # 1. Current char is smaller (lexicographically)
            # 2. The character we're removing appears later in string
            while (stack and stack[-1] > char and count[stack[-1]] > 0):
                removed = stack.pop()
                in_stack.remove(removed)
            
            # Add current character
            stack.append(char)
            in_stack.add(char)
        
        return ''.join(stack)
