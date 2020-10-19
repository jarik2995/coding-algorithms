
def fibonacciRecursive(n):
    if n < 2:
        return n
    return fibonacciRecursive(n-1)+fibonacciRecursive(n-2)

def fibonacciIterative(n):
    arr = [0, 1]
    for i in range(1,n):
        arr.append(arr[i]+arr[i-1])
    return arr[n]

print(fibonacciRecursive(7))
print(fibonacciIterative(7))
#0 1 1 2 3 5