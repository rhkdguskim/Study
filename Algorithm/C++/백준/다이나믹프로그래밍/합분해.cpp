// https://www.acmicpc.net/problem/2225

#include <iostream>
#include <vector>
#include <string>

using namespace std;

constexpr int DIV = 1000000000;

vector<vector<int>> dp;
int N, K;

int dfs(int value, int cnt)
{
    if (cnt > K || value > N)
    {
        return 0;
    }

    if (cnt == K && value == N)
    {
        return 1;
    }

    if (dp[value][cnt] != -1) return dp[value][cnt];

    int sum = 0;

    for (int n = 0; n <= N; n++)
    {
        sum += dfs(value + n, cnt + 1);
        sum %= DIV;
    }
    
    dp[value][cnt] = sum;
    return dp[value][cnt];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> K;

    dp.resize(N+1, vector<int>(K + 1, -1));

    cout << dfs(0, 0);
}
