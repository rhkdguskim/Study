#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    long T;
    cin >> T;
    int n, m;
    cin >> n;
    vector<int> A(n);
    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    cin >> m;
    vector<int> B(m);
    for (int i = 0; i < m; i++) {
        cin >> B[i];
    }

    vector<long long> sum_A, sum_B;
    for (int i = 0; i < n; i++) {
        long long sum = 0;
        for (int j = i; j < n; j++) {
            sum += A[j];
            sum_A.push_back(sum);
        }
    }

    for (int i = 0; i < m; i++) {
        long long sum = 0;
        for (int j = i; j < m; j++) {
            sum += B[j];
            sum_B.push_back(sum);
        }
    }

    sort(sum_A.begin(), sum_A.end());
    sort(sum_B.begin(), sum_B.end());

    
    long long cnt = 0;
    for (auto v : sum_A) {
        auto lp = lower_bound(sum_B.begin(), sum_B.end(), T - v);
        auto rp = upper_bound(sum_B.begin(), sum_B.end(), T - v);
        cnt += (rp - lp);
    }

    cout << cnt << endl;
    return 0;
}
