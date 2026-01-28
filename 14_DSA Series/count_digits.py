import math

def countDigit(n: int) -> int:
    if n == 0:
        return 1
    n = abs(n)
    return int(math.log10(n)) + 1
    
print(countDigit(12345))