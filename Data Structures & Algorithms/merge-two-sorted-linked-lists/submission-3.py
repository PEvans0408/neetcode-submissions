# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def MergeSections(self, list1node: Optional[ListNode], list2node: Optional[ListNode]) -> Optional[ListNode]:
        if list1node is None:           # CHANGED: added base case. The recursive calls inside this function
            return list2node             # can legitimately pass an exhausted (None) sub-list once one side
        if list2node is None:            # runs out — the original code had no guard for this and crashed
            return list1node             # (or relied on AttributeError handling that didn't actually cover it).
        
        curr1 = list1node
        curr2 = list2node
        
        if curr2.val < curr1.val:
            curr1, curr2 = curr2, curr1
            list1node = curr1
        
        try: 
            while curr1.next and (curr2.val >= (curr1.next).val):
                curr1 = curr1.next
            holder = curr1.next
            curr1.next = curr2
            curr2.next = self.MergeSections(curr2.next, holder)
            return list1node
        except AttributeError:
            curr1.next = curr2
            return list1node
    
    def mergeTwoLists(self, list1node: Optional[ListNode], list2node: Optional[ListNode]) -> Optional[ListNode]:
        if not list2node:
            return list1node
        if not list1node:
            return list2node
        else:
            return self.MergeSections(list1node, list2node)  # CHANGED: return the result directly instead of
            









