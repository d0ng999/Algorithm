# 선택정렬로 백준 2750문제 풀어보기
import sys
input = sys.stdin.readline

def selectionSort(ary):
    n = len(ary)
    for i in range(n-1):
        minIdx = i
        for k in range(i+1, n):
            if ary[minIdx] > ary[k]:
                minIdx = k

        ary[i], ary[minIdx] = ary[minIdx], ary[i]
    return ary

N = int(input())
ary = []
for i in range(N):
    ary += [int(input())]


ary = selectionSort(ary)

for i in ary:
    print(i)