# inputs: [0,3,4,21] [4,6,30]
# output: [0,3,4,4,6,21,30]

def mergeSortedArrays1(arr1, arr2):
    merge = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr2[j] < arr1[i]:
                merge.append(arr2[j])
            else:
                merge.append(arr1[i])
                if i == len(arr1)-1 and j < len(arr2):
                    merge.append(arr2[j])
                else:
                    break
    return merge

def mergeSortedArrays2(arr1, arr2):
    merge = []
    len1 = len(arr1)
    len2 = len(arr2)
    i=0
    j=0
    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            merge.append(arr1[i])
            i+=1
        else:
            merge.append(arr2[j])
            j+=1

    while i < len1:
        merge.append(arr1[i])
        i+=1
    while j < len2:
        merge.append(arr2[j])
        j+=1
    return merge
print(mergeSortedArrays2([0,3,4,21],[4,6,30]))