n = int(input())
for i in range(n):
    arr = list(map(int,input().split()))
    size = len(arr) - 1
    arr.remove(size)
    print(max(arr))