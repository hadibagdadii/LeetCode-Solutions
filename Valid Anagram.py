class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return True
        if len(s) != len(t):
            return False
        myDict = {}
        for letter in s:
            if letter in myDict:
                myDict[letter] = myDict[letter] + 1
            else:
                myDict[letter] = 1
        for letter in t:
            if letter in myDict:
                myDict[letter] = myDict[letter] - 1
                if myDict[letter] == 0:
                    myDict.pop(letter)
            else:
                return False
        if len(myDict) != 0:
            return False
        return True
