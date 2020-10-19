def findFactorialRecursive(number):
    if number <= 1:
        return number
    return findFactorialRecursive(number-1)*number

def findFactorialIterative(number):
    result = 1
    for i in range(number):
        result*=(i+1)
    return result

print(findFactorialRecursive(3))
print(findFactorialIterative(3))