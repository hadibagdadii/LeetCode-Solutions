import random

class RandomizedSet:

    def __init__(self):
        self.data = []  # List to store actual values
        self.indices = {}  # Dict to map value -> index in data list
        

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        
        # Add value to the end of list
        self.data.append(val)
        # Store its index in the dictionary
        self.indices[val] = len(self.data) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        # Get index of element to remove
        index = self.indices[val]
        last_val = self.data[-1]
        
        # Move last element to the position of element to remove
        self.data[index] = last_val
        # Update the index of the moved element
        self.indices[last_val] = index
        
        # Remove the last element
        self.data.pop()
        # Remove from dictionary
        del self.indices[val]
        
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.data)
