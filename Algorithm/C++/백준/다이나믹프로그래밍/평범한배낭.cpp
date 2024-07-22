// https://www.acmicpc.net/problem/12865

#include <iostream>
#include <vector>
#include <string>

using namespace std;
int N, K;
vector<int> w;
vector<int> v;
vector<vector<int>> dp;
// 무게를 포함하는경우, 포함하지 않는 경우 두가지로

int dfs(int index, int weight)
{
    // 무게를 초과한경우
    if (weight > K)  return -1e9;

    // 모든 아이템을 다 순회했을경우
    if (index == N) return 0;

    // 이미 계산한 이력이 있다면
    if (dp[index][weight] != -1) return dp[index][weight];

    // 현재 무게를 포함한경우, 포함하지않는경우 두가지 중 최대값.
    dp[index][weight] = max(dfs(index + 1, w[index] + weight) + v[index], dfs(index + 1, weight));

    return dp[index][weight];
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> K;

    int W, V;
    dp.resize(N, vector<int>(K + 1, -1));

    for (int i = 0; i < N; i++)
    {
        cin >> W >> V;
        w.push_back(W);
        v.push_back(V);
    }

    cout << dfs(0, 0);


}