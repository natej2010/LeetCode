# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def create_node(node1, node2, carry_over=0):

        if not node1 and not node2 and not carry_over:
            return None
        
        elif not node1 and not node2 and carry_over:
            val = 1
            link_node = None
        
        elif not node1:
            val = node2.val + carry_over
            
            if val >= 10:
                carry_over = 1
                val = val - 10
            else:
                carry_over = 0
                
            link_node = create_node(None, node2.next, carry_over)
            
        elif not node2:
            val = node1.val + carry_over
            
            if val >= 10:
                carry_over = 1
                val = val - 10
            else:
                carry_over = 0
                
            link_node = create_node(node1.next, None, carry_over)
            
        else:
            val = node1.val + node2.val + carry_over

            if val >= 10:
                carry_over = 1
                val = val - 10
            else:
                carry_over = 0
                
            link_node = create_node(node1.next, node2.next, carry_over)
        
        return ListNode(val, link_node)
    
class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:    
        return create_node(l1, l2)
