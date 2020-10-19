# find first reccuring items in array
# inputs: [2, 1, 3, 4, 2, 3]
# outputs: 2

def firstRecurringEl1(arr): #O(n^2) ##Wrong
    for i in range(1, len(arr)):
        for j in range(len(arr)):
            if arr[j] == arr[j+i]:
                return arr[j]

def firstRecurringEl2(arr):  #O(n)
    obj = {}
    for i in arr:
        if obj.get(i):
            return i
        obj[i] = 1

print(firstRecurringEl2([]))
print(firstRecurringEl1([2, 1, 5, 5, 3, 4, 5, 6, 7, 21, 54, 2]))
print(firstRecurringEl2([2, 1, 5, 5, 3, 4, 5, 6, 7, 21, 54, 2]))