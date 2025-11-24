# Brute force:
def buyAndSell(arr):
    max_count = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i]<arr[j]:
                max_count = max(max_count, arr[j]- arr[i])
    return max_count

arr = [7,2,1,5,6,4,8]
print(buyAndSell(arr))
    
#Optimal solution:
def buyAndSell1(arr):
    max_val = 0
    min_val = arr[0]
    for i in arr[1:]:
        max_val = max(max_val, i - min_val)
        min_val = min(min_val, i)
    return max_val

print(buyAndSell1(arr))