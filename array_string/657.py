"""
LeetCode 657: Robot return to origin

Author: Jose Renteria

"""

def judgeCircle(moves: str) -> bool:
    hmap = {'x': 0, 'y': 0}
    for c in moves:
        if c == 'L':
            hmap['x'] -= 1
        elif c == 'R':
            hmap['x'] += 1
        elif c == 'U':
            hmap['y'] += 1
        elif c == 'D':
            hmap['y'] -= 1
    return True if list(hmap.values()) == [0, 0] else False

sol = judgeCircle("UL")
print(sol)