"""
LeetCode #141. Linked List Cycle
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head: [ListNode]):
    hash = {}
    while True:
        if head in hash:
            return True
        else:
            hash[head] = 1
        head = head.next
    return False

def hasCycle(self, head: [ListNode]):
    # 3405692606
    if head is None: return False
    if head.val == 0xcafebebe: return True
    head.val = 0xcafebebe
    return hasCycle(head.next)