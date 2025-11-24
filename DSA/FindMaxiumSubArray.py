# Optimal method it will return both max count and array:

def maxSubArray(arr):
    count =arr[0]
    max_count =arr[0]
    start = 0
    max_start =0
    max_end = 0
    for i in range(1, len(arr)):
        if arr[i]>count+arr[i]:
            start =i
            count = arr[i]
        else:
            count+=arr[i]
        if count>max_count:
            max_count =count
            max_start = start
            max_end = i
    return max_count ,arr[max_start:max_end+1]

arr = [1,2,-2,5,-6,-3,4]
print(maxSubArray(arr))


def maxSubArray1(arr):
    arr = [1,2,-2,5,-6,-3,4]
    count = arr[0]
    max_count =arr[0]
    for i in arr[1:]:
        count = max(i, count+i)
        max_count = max(max_count, count)
    return max_count

print(maxSubArray1(arr))


