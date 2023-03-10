# Algorithm
자료구조 및 알고리즘 모음
## 선택정렬, 삽입정렬, 퀵정렬, 병합정렬 성능 비교
- 백준 2750번을 기준으로 비교했음
- 선택, 삽입, 퀵정렬은 범위가 비교적 적은 경우에 사용할 것
- 병합정렬은 큰 범위인 경우에 사용할 것

1. 선택정렬
[Source Code](https://github.com/d0ng999/Algorithm/blob/main/Sorting_Method/method1_selectionSort.py)
- 시간은 약 64ms로 2번째로 빠르고, 메모리는 모두 같은 상황이다. 코드의 길이는 약 412B로 2번쨰로 많은 무난난 정렬인것으로 보인다.

2. 삽입정렬
[Source Code](https://github.com/d0ng999/Algorithm/blob/main/Sorting_Method/method2_insertionSort.py)
- 시간은 약 88ms로 가장 느린 정렬로 보이고, 메모리는 같은 상황. 코드의 길이는 367B로 급한 상황이나, 빠르고 쉬운 정렬을 구현하고자 할 때 사용해보기!

3. 퀵정렬
[Source Code](https://github.com/d0ng999/Algorithm/blob/main/Sorting_Method/method3_quickSort.py)
- 시간은 44ms로 정말 Quick한 것을 볼 수 있다. 다만, 코드의 길이가 550B로 3위를 차지했다. 문제에 시간에 대한 조건이 빡빡하다면 사용해보는 것을 추천한다.

4. 병합정렬
[Source Code](https://github.com/d0ng999/Algorithm/blob/main/Sorting_Method/method4_mergeSort.py)
- 시간은 84ms로 3위를 했으나, 이 정렬의 경우 범위가 적은 문제에 해당하기보단 큰 범위에 쓰이는 문제에 하는 것을 추천한다. 물론 문자의 코드는 813B로 가장 길긴 하지만, 범위가 커지면 앞의 3가지 정렬로도 문제를 풀 수 없는 상황이 생기므로 특별한 상황에서만 사용할 것!(아니면 이거만 써도 될수도 ㅎㅎ)
