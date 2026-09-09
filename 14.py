class Solution:
    def rotateRight(self, head, k) :
        if not head or not head.next or k ==0 :
            return head
        
        curr = head
        length = 1

        while curr.next :
            curr = curr.next
            length += 1
        
        k = k%length

        if k == 0 :
            return head
        
        curr.next = head
        steps = length - k
        curr = head

        for i in range(steps-1):
            curr = curr.next
        
        head = curr.next
        curr.next = None

        return head
        