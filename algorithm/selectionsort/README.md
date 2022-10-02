# 선택 정렬 (Selection Sort)

### 목표
- Selection Sort에 대해 설명 할 수있다.
- Selection Sort 과정에 대해 설명 할 수 있다.
- Selection Sort을 구현할 수 있다.
- Selection Sort의 시간복잡도와 공간복잡도를 계산할 수 있다.

### 요약
- Selection Sort는 Bubble Sort과 유사한 알고리즘으로, 해당 순서에 원소를 넣을 위치는 이미 정해져있고, 어떤 원소를 넣을지 선택하는 알고리즘 입니다. Selection Sort와 Bubble Sort를 햇갈려하시는 분들이 종종 있는데 Selection Sort는 배열에서 해당 자리를 선택하고, 그자리에 오는 값을 찾는 것이라고 생각하시면 편합니다.

### 과정
1. 주어진 배열 중에 최소값을 찾는다.
2. 그 값을 맨 앞에 위치한 값과 교체합니다.
3. 맨 처음에 위치를 뺀 나머지 배열을 같은 방법으로 교체합니다.