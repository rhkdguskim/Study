# 삽입정렬 (Insertion Sort)

## 목표
- Insertion Sort에 대해 설명할 수 있다.
- Insertion Sort 과정에 대해 설명할 수 있다.
- Insertion Sort을 구현할 수 있다.
- Insertion Sort의 시간복잡도와 공간복잡도를 계산 할 수 있다.
- Insertion Sort와 Selection Sort 차이에 대해 설명할 수 있다.

## 요약
손 안의 카드를 정렬하는 방법과 유사합니다.

Insertion Sort는 Selection Sort 와 유사하지만, 조금 더 효율적인 알고르즘 입니다.

Insertion Sort는 2번째 원소부터 시작하여 그 앞(왼쪽)의 원소들과 비교하여 삽입할 위치를 지정한 후, 원소를 뒤로 옮기고 지정된 자리에 자료를 삽입하여 정렬하는 알고리즘 입니다.

최선의 경우 O(n)이라는 엄청나게 빠른 효율성을 가지고 있어, 다른 정렬 알고리즘 일부로 사용될 만큼 좋은 알고리즘입니다.

## 과정
1. 정렬은 2번째 위치(index)의 값을 temp에 저장합니다.
2. temp와 이전에 있는 원소들과 비교하여 삽입해 나갑니다.
3. '1'번으로 돌아가 다음 위치(index)의 값을 저장하고, 반복합니다.

## 기능구현
1. 첫 번째 원소 앞(왼쪽)에는 어떤 원소도 갖고 있지 않기 때문에, 두 번째 위치(index)부터 탐색을 시작합니다. temp에 임시로 해당 위치(index)값을 저장하고, prev에는 해당 위치(index)를 저장합니다.
2. 이전위치(index)를 가리키는 prev가 음수가 되지 않고, 이전 위치(index)값이 '1번'에서 선택한 값보다 크면, 서로 그 값을 교환해주고 prev를 더 이전위치 (index)를 가리키도록 합니다.
3. '2'번에서 반복문이 끝나고 난 뒤, prev에는 현재 temp 값보다 작은 값들 중 제일 큰 값의(index)를 가리키게 됩니다. 따라서, (prev+1)에 temp 값을 삽입해줍니다.

## 참조 이미지
![screensh](https://github.com/GimunLee/tech-refrigerator/blob/master/Algorithm/resources/insertion-sort-001.gif)