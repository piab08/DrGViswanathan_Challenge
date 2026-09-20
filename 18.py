class Solution :
    def swapNodes(self, head, k):
        n = 0
        temp = head

        while temp:
            temp = temp.next
            n+= 1
        
        first = head
        for i in range(k-1):
            first = first.next
        
        second = head
        for i in range(n-k):
            second = second.next
        
        first.val, second.val = second.val, first.val

        return head