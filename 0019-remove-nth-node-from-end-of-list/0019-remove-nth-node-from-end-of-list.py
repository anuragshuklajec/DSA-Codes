# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        length = len(nodes)

        k = length - n #length from beginning

        # if node is at beginning
        if k == 0:
            return head.next
        elif k == length - 1:
            nodes[length-2].next = None
        else:
            nodes[k-1].next = nodes[k+1]
        return head
        
        


        