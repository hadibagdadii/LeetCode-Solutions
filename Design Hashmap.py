class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 10**4
        self.buckets = [ListNode(0, 0) for _ in range(self.size)]  # Dummy heads
        
    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self._hash(key)]
        cur = bucket
        
        # Check if key already exists
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value  # Update existing
                return
            cur = cur.next
        
        # Add new key-value pair
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        bucket = self.buckets[self._hash(key)]
        cur = bucket.next  # Skip dummy head
        
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        
        return -1  # Key not found

    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        cur = bucket
        
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next  # Remove node
                return
            cur = cur.next
