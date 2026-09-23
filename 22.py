class Solution:
    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        
        if fast == None:
            return head.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return head