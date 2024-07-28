// https://www.acmicpc.net/problem/10942
#include <iostream>
#include <vector>
#include <string>

using namespace std;
vector<int> nums;
// visited, flag
vector<vector<pair<bool, bool>>> dp;
int N, M;

bool dfs(int start, int end);
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    nums.resize(N);
    for(int i = 0; i < N; i ++) cin >> nums[i];
    dp.resize(N, vector<pair<bool, bool>>(N, {false, false}));

    cin >> M;
    int S, E;
    for(int i = 0; i < M; i ++)
    {
        cin >> S >> E;
        if(dfs(S-1, E-1)) cout << 1 << '\n';
        else cout << 0 << '\n';
    }
}

bool dfs(int start, int end)
{
    // 한자리는 팰린드롬이다.
    if (start >= end)
        return true;

    if(dp[start][end].first) return dp[start][end].second;
    
    dp[start][end].first = true;

    // 양끝이 같다면 하나를 줄여서 펠린드롬을 찾아본다.
    if(nums[start] == nums[end])
    {
        dp[start][end].second = dfs(start + 1, end - 1);
    }
    // 양끝이 같지 않다면 팰린드롬이아니다.
    else
    {
        return dp[start][end].second = false;
    }
    
    return dp[start][end].second;
}