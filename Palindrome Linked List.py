class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        curr = head
        while curr:
            array.append(curr.val)
            curr = curr.next
        
        return array == array[::-1]  # Can simplify the if/else
