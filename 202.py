"""
Leetcode #202. Happy Number

Author: Jose Renteria
"""
def isHappy(n: int) -> bool:
    def next_num(num):
        return sum(map(lambda x:int(x)**2, str(num)))
    slow, fast = n, next_num(n)
    while slow != fast and fast != 1:
        slow = next_num(slow)
        fast = next_num(next_num(fast))
    return fast == 1 or not slow == fast

print(isHappy(19))
