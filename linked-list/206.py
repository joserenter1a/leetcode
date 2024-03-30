"""
Leetcode #206. Reverse Linked list

Author: Jose Renteria
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        curr_node = head
        prev = None
        next = None
        while(curr_node is not None):
            next = curr_node.next # store the next node with a ptr in next
            curr_node.next = prev # connect current to prev " <- " (reverse node)
            prev = curr_node # move previous ptr along to current
            curr_node = next # move curr 
        return prev # 
