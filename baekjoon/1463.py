# 시간제한 1.5초

n = int(input())
arr = [0]*10000000

for i in range(2,n+1):
    arr[i] = arr[i-1]+1
    if i % 2 == 0:
        arr[i] = min(arr[i//2]+1,arr[i])
    if i % 3 == 0:
        arr[i] = min(arr[i//3]+1,arr[i])

        

print(arr[n])
    
