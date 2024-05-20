from typing import List
def sumZero(n: int) -> List[int]:
    el = []
    if n == 1:
        return [0]
    even = lambda n : n % 2 == 0
    pt = 1
    while len(el) < n:
        if even(n):
            el.append(pt)
            el.append(-pt)
        elif not el:
            el.append(0)
        else:
            el.append(pt)
            el.append(-pt)
        pt += 1
    return el

sol = sumZero(4)
sol2 = sumZero(3)
print(sol)
print(sol2)