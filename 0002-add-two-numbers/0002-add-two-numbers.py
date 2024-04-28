# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            newHead = None
            currHead = None
            rem = 0
            while l1 and l2:
                currSum = l1.val + l2.val + rem
                rem = currSum // 10
                to_add = currSum % 10
                curr_ele = ListNode(to_add)
                if newHead is None:
                    newHead = curr_ele
                    currHead = newHead
                else:
                    currHead.next = curr_ele
                    currHead = curr_ele
                l1 = l1.next
                l2 = l2.next

            while l1 or l2:
                currSum = l1.val + rem if l1 else l2.val + rem
                rem = currSum // 10
                to_add = currSum % 10
                curr_ele = ListNode(to_add)
                currHead.next = curr_ele
                currHead = curr_ele
                if l1: l1 = l1.next
                if l2: l2 = l2.next

            if rem != 0:
                currHead.next = ListNode(rem)
            return newHead


        