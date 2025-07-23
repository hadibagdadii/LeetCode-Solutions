# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []

        temp = head
        while temp:
            result.append(temp.val)
            temp = temp.next

        result.sort()

        temp = head
        for n in result:
            temp.val = n
            temp = temp.next

        return head
