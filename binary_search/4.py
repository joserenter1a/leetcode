from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    for el in nums2:
        nums1.append(el)
    nums1 = sorted(nums1)
    
    even = lambda l : (len(l) % 2) == 0
    mid = lambda l, i : (len(l) // 2 ) + i
    avg = lambda l : float((l[mid(l, 0)] + l[mid(l, -1)]) / 2)
    print(even(nums1))
    print(nums1)
    if len(nums1) == 1:
        return float(nums1[0]) 
    elif even(nums1) == False:
        return nums1[mid(nums1, 0)]
    else:
        return avg(nums1)

sol = findMedianSortedArrays([1, 3], [2])
print(sol)

sol2 = findMedianSortedArrays([1, 2], [3, 4])
print(sol2)