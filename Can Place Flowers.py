class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        skip = False
        
        for i in range(len(flowerbed)):
            if n == 0:
                return True
                
            if flowerbed[i] == 1:
                skip = True
            elif skip:
                skip = False
            elif i + 1 < len(flowerbed) and flowerbed[i + 1] == 1:
                skip = True
            else:
                n -= 1
                skip = True
        
        return n <= 0
