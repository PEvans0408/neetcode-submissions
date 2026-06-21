# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer1 = head
        if head and head.next and head.next.next:
            pointer2 = head.next.next
        else: return False
        while pointer1 != pointer2:
            if pointer2 and pointer2.next: #This works because youa re retracing the same linked list
                pointer1 = pointer1.next
                pointer2 = pointer2.next.next
            else: return False
        return True

        