# 퀵정렬로 백준 2750번 풀기
import sys
input = sys.stdin.readline

def quickSort(ary):
    n = len(ary)
    if n <=1:
        return ary
    
    leftAry, midAry, rightAry = [], [], []

    pivot = ary[n//2]
    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)
        else:
            midAry.append(num)
    
    return quickSort(leftAry) + midAry + quickSort(rightAry)

N = int(input())
ary = []
for _ in range(N):
    ary += [int(input())]
ary = quickSort(ary)
for i in ary:
    print(i)