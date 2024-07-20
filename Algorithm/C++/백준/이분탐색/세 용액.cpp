#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<long long> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    sort(A.begin(), A.end());

    long long closestSum = 9876543219876543321;
    vector<long long> answer(3);

    for (int i = 0; i < N-2; i++) {
        int left = i + 1, right = N - 1;
        while (left < right) {
            long long sum = A[i] + A[left] + A[right];
            if (abs(sum) < abs(closestSum)) {
                closestSum = sum;
                answer = {A[i], A[left], A[right]};
            }
            if (sum > 0) right--;
            else if (sum < 0) left++;
            else break; // sum이 0인 경우 최적 해를 찾음
        }
        if (closestSum == 0) break; // 최적 해를 찾으면 더 이상 탐색 중지
    }

    sort(answer.begin(), answer.end());
    for (long long v : answer) cout << v << ' ';
    cout << '\n';

    return 0;
}