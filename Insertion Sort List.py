# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)  # Dummy node for easier insertion
        current = head
        
        while current:
            next_node = current.next  # Save next before we break the link
            
            # Find the correct position to insert current node
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            # Insert current node after prev
            current.next = prev.next
            prev.next = current
            
            # Move to next node
            current = next_node
        
        return dummy.next
