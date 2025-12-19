def palindrome(s):
    s = str(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    while n > 1:
        result = result * n
        n = n - 1
    return result   

while n >= 1:
    result = result * n
    n = n -1

