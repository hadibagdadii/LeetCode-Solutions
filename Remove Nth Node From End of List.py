# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
            
        if count == n:
            return head.next
            
        pop = count - n
        temp = head
        while pop > 1:
            temp = temp.next
            pop -= 1
            
        temp.next = temp.next.next
        return head
