
def isPowerOfFour( n: int) -> bool:
    if n == 1:
        return True
    if(n <= 0):
        return False
    return (n % 4 == 0) and (isPowerOfFour((n >> 2)))


print(isPowerOfFour(16))
print(isPowerOfFour(5))
print(isPowerOfFour(1))
