class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # Calculate prefix sum to know how many candies are available before a type
        prefix = [0]
        for count in candiesCount:
            prefix.append(prefix[-1] + count)
        
        result = []
        for query in queries:
            favoriteType, favoriteDay, dailyCap = query
            
            # Earliest day to eat the first candy of this type
            earliest_day = prefix[favoriteType] // dailyCap
            
            # Latest day to eat the last candy of this type
            latest_day = prefix[favoriteType + 1] - 1
            
            # Check if we can eat a candy of the favorite type on the favorite day
            can_eat = earliest_day <= favoriteDay <= latest_day
            
            # A different way to check:
            # Min candies eaten by favoriteDay (if eating 1 per day)
            min_eaten = favoriteDay + 1
            
            # Max candies eaten by favoriteDay (if eating dailyCap per day)
            max_eaten = (favoriteDay + 1) * dailyCap
            
            # Can we eat a candy of favorite type?
            # This means min_eaten <= prefix[favoriteType+1] and max_eaten > prefix[favoriteType]
            can_eat = min_eaten <= prefix[favoriteType + 1] and max_eaten > prefix[favoriteType]
            
            result.append(can_eat)
        
        return result
