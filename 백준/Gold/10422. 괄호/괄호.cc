#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1000000007;
const int L = 5001;

vector<vector<int>> dp(L / 2 + 1, vector<int>(L + 1, -1));

int dfs(int open, int cnt) {
    if (cnt <= 0 || open - cnt > 0) {
        if (open == 0) {
            return 1;
        } else {
            return 0;
        }
    }

    if (dp[open][cnt] != -1) {
        return dp[open][cnt];
    }

    dp[open][cnt] = 0;

    if (open > 0) {
        dp[open][cnt] = (dp[open][cnt] + dfs(open - 1, cnt - 1)) % MOD;
        dp[open][cnt] = (dp[open][cnt] + dfs(open + 1, cnt - 1)) % MOD;
    } else {
        dp[open][cnt] = (dp[open][cnt] + dfs(open + 1, cnt - 1)) % MOD;
    }

    return dp[open][cnt];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    dfs(0, L);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        if (n % 2 == 0) {
            cout << dfs(0, n) << "\n";
        } else {
            cout << 0 << "\n";
        }
    }

    return 0;
}