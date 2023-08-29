location, k = map(int, input().split())

arr = [['_']*5 for _ in range(3)]
arr[0][location] = k
arr[1][location+1] = k-1



for i in arr:
    print(*i, sep = '')