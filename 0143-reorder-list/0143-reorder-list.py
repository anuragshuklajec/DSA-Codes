# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        length = len(nodes)
        mid = length//2
        nodes[mid].next = None

        l,r = 0,length-1
        to_run = length - 1 - mid
        while l < to_run :
            nextEle = nodes[l].next
            nodes[l].next = nodes[r]
            nodes[r].next = nextEle
            l+=1
            r-=1

            


        


        