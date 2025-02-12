class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list) # mapping charCount to List of Anagrams
        
        for s in strs:
            count = [0] * 26 # a ... z
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            result[tuple(count)].append(s)
            
        return result.values()
