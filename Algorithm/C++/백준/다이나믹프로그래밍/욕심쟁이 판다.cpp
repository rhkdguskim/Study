// https://www.acmicpc.net/problem/1937
#include <iostream>
#include <vector>
#include <string>

using namespace std;
int N;
vector<vector<int>> graph;
vector<vector<int>> dp; // n x n
int dy[4] = { 0, 0, 1, -1 };
int dx[4] = { 1, -1, 0, 0 };

int dfs(int y, int x);

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    graph.resize(N, vector<int>(N, 0));
    dp.resize(N, vector<int>(N, -1));

    int max_value = 0;
    for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) cin >> graph[i][j];

    for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) max_value = max(max_value, dfs(i, j));

    cout << max_value;
}

int dfs(int y, int x)
{
    if (dp[y][x] != -1) return dp[y][x];

    int max_value = 1;

    for (int k = 0; k < 4; k++)
    {
        int ny = y + dy[k];
        int nx = x + dx[k];

        if (N > ny && ny >= 0 && N > nx && nx >= 0 && graph[ny][nx] > graph[y][x])
        {
            max_value = max(max_value, dfs(ny, nx) + 1);
        }
    }

    dp[y][x] = max_value;

    return max_value;
}
