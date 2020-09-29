# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        nodes = []
        fast = head
        slow = head
        i = 0
        
        for i in range(n):
            fast = fast.next
        
        if fast == None:
            return head.next

        while fast.next:
                
            fast = fast.next
            slow = slow.next
        
        slow.next.next, slow.next = None, slow.next.next
        
        return head
