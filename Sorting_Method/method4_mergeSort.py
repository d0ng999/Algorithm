# 병합정렬로 백준 2750번 풀어보기
A = []
tmp = []
def mergeSort(s, e):
    if e - s < 1:
        return
    m = (s+e)//2
    mergeSort(s, m)
    mergeSort(m+1, e)

    for i in range(s, e+1):
        tmp[i] = A[i]
    
    k = s
    index1 = s
    index2 = m+1

    while index1 <= m and index2 <= e:
        if tmp[index1] < tmp[index2]:
            A[k] = tmp[index2]
            k+=1
            index2+=1

        else:
            A[k] = tmp[index1]
            k+=1
            index1 += 1
    
    while index2 <= e:
        A[k] = tmp[index2]
        k+=1
        index2+=1
    
    while index1 <= m:
        A[k] = tmp[index1]
        k+=1
        index1 +=1
    
    return A

N = int(input())
A = [0] * (N+1)
tmp = [0] * (N+1)

for i in range(1, N+1):
    A[i] = int(input())

mergeSort(1, N)

for i in range(N, 0, -1):
    print(A[i])