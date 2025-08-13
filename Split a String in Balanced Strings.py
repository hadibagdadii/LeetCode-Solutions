class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = count = 0
        for letter in s:
            if letter == 'R':
                balance += 1
            elif letter == 'L':
                balance -= 1
            if balance == 0:
                count += 1
        return count
