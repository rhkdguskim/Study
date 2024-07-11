// https://www.acmicpc.net/problem/1987
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;
int R, C;
constexpr int ALPHA = 'A';
vector<vector<char>> graph;
vector<vector<bool>> v;
vector<bool> color_v;
int answer = 1;
int dy[4] = {0, 0, -1, 1};
int dx[4] = {-1, 1, 0, 0};

void dfs(int i, int j, int cnt)
{
    answer = max(cnt, answer);

    for(int k = 0; k < 4; k ++)
    {
        size_t ny = dy[k] + i;
        size_t nx = dx[k] + j;
        
        if(ny >= R || nx >= C || v[ny][nx] || color_v[graph[ny][nx]-ALPHA]) continue;

        v[ny][nx] = true;
        color_v[graph[ny][nx]-ALPHA] = true;
        dfs(ny, nx, cnt + 1);
        v[ny][nx] = false;
        color_v[graph[ny][nx]-ALPHA] = false;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> R >> C;


    graph.resize(R, vector<char>(C));
    v.resize(R, vector<bool>(C, false));
    color_v.resize(26, false);
    string temp;
    for(int i = 0; i < R; i ++)
    {
        cin >> temp;
        for(int j = 0; j < C; j ++)
        {
            graph[i][j] = temp[j];
        }
    }

    color_v[graph[0][0]-ALPHA] = true;
    dfs(0, 0, 1);

    cout << answer;
}