class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Handle nodes at the head that need to be removed
        while head and head.val == val:
            head = head.next
        
        # Now traverse and remove matching nodes
        curr = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head
