#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <limits>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<long long> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    sort(A.begin(), A.end());

    long long closestSum = numeric_limits<long long>::max();
    vector<long long> answer(3);

    for (int i = 0; i < N - 2; ++i) {
        for (int j = i + 1; j < N - 1; ++j) {
            long long target = -(A[i] + A[j]);
            int left = j + 1, right = N - 1;
            while (left <= right) {
                int mid = (left + right) / 2;
                long long diff = A[mid] + target;
                if (abs(diff) < abs(closestSum)) {
                    closestSum = diff;
                    answer = {A[i], A[j], A[mid]};
                }
                if (diff == 0) {
                    cout << A[i] << " " << A[j] << " " << A[mid] << "\n";
                    return 0;
                } else if (diff < 0) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
    }

    sort(answer.begin(), answer.end());
    for (long long v : answer) {
        cout << v << ' ';
    }
    cout << '\n';

    return 0;
}
