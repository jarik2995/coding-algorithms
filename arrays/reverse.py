# input: "ABCD"
# output: "DCBA"
def reverseString1(string):
    return string[::-1]

def reverseString2(string):
    arr = list(string)
    length = len(arr)
    for i in range(length // 2):
        tmp = arr[i]
        arr[i] = arr[length-i-1]
        arr[length-i-1] = tmp
    return "".join(arr)

def reverseString3(string):
    reverse = ""
    for i in string:
        reverse = i + reverse
    return reverse


def reverseString4(string):
    if len(string) == 0:
        return string
    return reverseString4(string[1:]) + string[0]


a = ""
print(reverseString1(a))
print(reverseString2(a))
print(reverseString3(a))
print(reverseString4(a))