# 정렬 - Counting Sort

def countingSort(array, max):
    countingAry = [0] * (max+1)

    for i in array:
        countingAry[i] += 1
    
    for i in range(max):
        countingAry[i+1] += countingAry[i]
    
    outputAry = [-1] * len(array)

    for i in array:
        outputAry[countingAry[i]-1] = i
        countingAry[i] -= 1
    return outputAry

a = int(input())
ary = []
for i in range(a):
    ary += map(int, input().split())

outputary = countingSort(ary, max(ary))

for i in outputary:
    print(i)
