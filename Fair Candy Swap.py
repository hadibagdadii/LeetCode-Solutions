class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        
        # The difference that needs to be balanced
        diff = (sum_alice - sum_bob) // 2
        
        # Convert Bob's sizes to a set for O(1) lookup
        bob_set = set(bobSizes)
        
        # For each candy Alice has, check if Bob has the required candy
        for alice_candy in aliceSizes:
            bob_candy = alice_candy - diff
            if bob_candy in bob_set:
                return [alice_candy, bob_candy]
