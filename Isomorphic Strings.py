class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        if same size strings, loop thru chars, check if existing mapping exists, if not create mapping
        time: O(n)
        space: O(1)
        '''
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}
        
        for s_char, t_char in zip(s, t):
            if s_char in s_to_t:
                if s_to_t[s_char] != t_char:
                    return False
            else:
                s_to_t[s_char] = t_char
            
            if t_char in t_to_s:
                if t_to_s[t_char] != s_char:
                    return False
            else:
                t_to_s[t_char] = s_char
        
        return True
        
        
        '''
        loop thru chars, branch whether already mapped, need to map, or invalid
        time: O(n^2)
        space: O(n)
        
        hashmap = {}
        if len(s) != len(t):
            return False
        for s_char, t_char in zip(s, t):
            # need to map
            if s_char not in hashmap:
                if t_char in hashmap.values():
                    return False
                hashmap[s_char] = t_char
                continue

            # already mapped
            elif s_char in hashmap and hashmap[s_char] == t_char:
                continue

            # invalid
            return False
        # valid
        return True
        '''
