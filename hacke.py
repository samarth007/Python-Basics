n = int(input())
arr = map(int, input().split())


def runner(n, arr):
    arr = list(set(arr))
    print(arr)
    l = len(arr)
    for i in range(l):
        for j in range(i + 1, l):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    # arr1=list(set(arr)) 
    # print(arr)           
    return arr[1]


print(runner(n, arr))