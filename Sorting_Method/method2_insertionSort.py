# 삽입정렬로 백준 2750번 풀어보기
import sys
input = sys.stdin.readline

def insertionSort(ary):
    n = len(ary)
    for end in range(n):
        for i in range(end, 0, -1):
            if ary[i-1] > ary[i]:
                ary[i-1], ary[i] = ary[i], ary[i-1]
    return ary

N = int(input())
ary = []
for _ in range(N):
    ary += [int(input())]

ary = insertionSort(ary)

for i in ary:
    print(i)

            