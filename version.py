# First Bad Version Leetcode 278

def isBadVersion(version: int) -> bool:
    if version == 4:
        return True

def firstBadVersion(n: int) -> int:
    start = 1
    while(start <= n):
        mid = start + (n - start) // 2
        if(isBadVersion(mid)):
            n = mid - 1
        else:
            start = mid + 1
    return start     

