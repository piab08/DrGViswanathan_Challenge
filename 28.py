class Solution:
    def partition(self, head, x):
        less = ListNode(0)
        great = ListNode(0)
        
        l = less
        g = great
        while head :
            if head.val<x :
                l.next = head
                l = l.next
            
            else :
                g.next = head
                g = g.next
            
            head = head.next
        
        g.next = None
        l.next = great.next

        return less.next