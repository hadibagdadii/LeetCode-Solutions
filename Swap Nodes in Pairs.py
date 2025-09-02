class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            # Nodes to be swapped
            first = prev.next
            second = prev.next.next
            
            # Perform swap
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move prev to end of swapped pair
            prev = first
            
        return dummy.next
