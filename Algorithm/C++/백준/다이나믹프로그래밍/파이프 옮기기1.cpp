#include <iostream>
#include <vector>
#include <string>

using namespace std;

constexpr int EMPTY = 0;
constexpr int WALL = 1;
int N;
vector<vector<int>> graph;
vector<vector<vector<int>>> dp;

constexpr int HOR = 0;
constexpr int VAR = 1;
constexpr int CROSS = 2;
// 가로, 세로, 대각선
int dy[3] = { 0, 1, 1 };
int dx[3] = { 1, 0, 1 };

bool check(int y, int x, int cur_dir, int next_dir)
{
    if (cur_dir == HOR)
    {
        if (next_dir == VAR) return false;

        if (next_dir == HOR && graph[y][x] == WALL) return false;

        if (next_dir == CROSS && (graph[y][x] == WALL || graph[y - 1][x] == WALL || graph[y][x - 1] == WALL)) return false;
    }
    else if (cur_dir == VAR)
    {
        if (next_dir == HOR) return false;

        if (next_dir == VAR && graph[y][x] == WALL) return false;

        if (next_dir == CROSS && (graph[y][x] == WALL || graph[y - 1][x] == WALL || graph[y][x - 1] == WALL)) return false;
    }

    else
    {
        if (next_dir == CROSS && (graph[y][x] == WALL || graph[y - 1][x] == WALL || graph[y][x - 1] == WALL)) return false;

        if (next_dir == VAR && graph[y][x] == WALL) return false;

        if (next_dir == HOR && graph[y][x] == WALL) return false;
    }

    return true;
}


int dfs(int y, int x, int dir)
{
    if (y == N - 1 && x == N - 1) 
        return 1;

    if (dp[y][x][dir] != -1) return dp[y][x][dir];

    int cnt = 0;
    for (int k = 0; k < 3; k++)
    {
        size_t ny = y + dy[k];
        size_t nx = x + dx[k];

        if (ny >= N || nx >= N || !check(ny, nx, dir, k)) continue;

        cnt += dfs(ny, nx, k);
    }

    dp[y][x][dir] = cnt;
    return cnt;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    graph.resize(N, vector<int>(N));
    dp.resize(N, vector<vector<int>>(N, vector<int>(3, -1)));

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> graph[i][j];
        }
    }

    cout << dfs(0, 1, HOR);
}