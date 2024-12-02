"""
LeetCode #1721. Swapping Nodes in a Linked List

Author: Jose Renteria
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    curr = head
    for i in range(k - 1):
        curr = curr.next
    left = curr
    right = head
    while curr.next:
        curr = curr.next
        right = right.next
    left.val, right.val = right.val, left.val
    return head