// https://www.acmicpc.net/problem/2133

#include <iostream>
#include <vector>

using namespace std;

int N;
vector<int> dp;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N;
    if (N % 2 != 0) {
        cout << 0 << endl;
        return 0;  // N이 홀수면 타일링 불가능
    }

    dp.resize(N + 1, 0);
    dp[0] = 1;  // 타일이 없는 경우, 하나의 방법이 존재
    if (N >= 2) dp[2] = 3;  // 3x2 타일링 경우의 수

    for (int i = 4; i <= N; i += 2) {
        dp[i] = dp[i - 2] * 3;  // 기본 3x2 블록을 추가하는 경우
        for (int j = 4; j <= i; j += 2) {
            dp[i] += dp[i - j] * 2;  // 3x4, 3x6, ... 블록을 추가하는 경우
        }
    }

    cout << dp[N] << endl;
    return 0;
}


#include <iostream>
#include <vector>

using namespace std;

int N;
vector<int> dp;

int solve(int n) {
    if (n % 2 != 0) return 0; // 홀수는 타일링 불가능
    if (n == 0) return 1; // 타일이 없는 경우
    if (n == 2) return 3; // 3x2 타일링 경우의 수

    if (dp[n] != -1) return dp[n]; // 이미 계산된 값이 있으면 반환

    dp[n] = solve(n - 2) * 3; // 기본 3x2 블록을 추가하는 경우
    for (int i = 4; i <= n; i += 2) {
        dp[n] += solve(n - i) * 2; // 3x4, 3x6, ... 블록을 추가하는 경우
    }

    return dp[n];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N;
    dp.resize(N + 1, -1); // DP 배열 초기화

    cout << solve(N) << endl;
    return 0;
}
