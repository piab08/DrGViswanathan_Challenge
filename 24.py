class Solution:
    def insertGreatestCommonDivisors(self, head):
        temp = head

        while temp.next :
            a = temp.val
            b = temp.next.val
        
            while b :
                a, b = b, a%b
        
            new = ListNode(a)

            new.next = temp.next
            temp.next = new
            temp = new.next

        return head