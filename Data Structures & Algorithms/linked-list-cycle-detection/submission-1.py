# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer1 = head

        try:
            pointer2 = head.next.next
            while (pointer1 != pointer2):
                pointer1 = pointer1.next
                pointer2 = pointer2.next.next
        except AttributeError:
            return False
        return True

        