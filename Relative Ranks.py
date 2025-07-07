class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(score) + 1)]
        
        # Sort indices by their scores in descending order
        sorted_indices = sorted(range(len(score)), key=lambda i: score[i], reverse=True)
        
        # Create result
        res = [""] * len(score)
        for rank, idx in enumerate(sorted_indices):
            res[idx] = ranks[rank]
        return res

'''
brute force solution

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [""] * len(score)
        for i in reversed(range(len(score))):
            smallest_index = score.index(min(score))
            score[smallest_index] = float('inf')
            if i == 0:
                res[smallest_index] = "Gold Medal"
            elif i == 1:
                res[smallest_index] = "Silver Medal"
            elif i == 2:
                res[smallest_index] = "Bronze Medal"
            else:
                res[smallest_index] = str(i+1)
        return res
'''
