// https://www.acmicpc.net/problem/14500
#include <iostream>
#include <vector>
using namespace std;

int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 0};
int N, M;
vector<vector<int>> graph;
vector<vector<bool>> v;
// ㅗ 모양만 특별하게 구현해서 구한다.
// ㅗ, ㅏ, ㅜ, ㅓ
vector<vector<vector<int>>> speicalmoves = {{{0, 1}, {-1, 1}, {0, 2}}, {{1, 0}, {2, 0}, {1, 1}}, {{0, 1}, {0, 2}, {1, 1}}, {{1, 0}, {2, 0}, {1, -1}}};

int dfs(int y, int x, int depth, int value, int d_y, int d_x)
{
    if (depth == 3)
    {
        return value;
    }

    int max_value = 0;
    for(int k = 0; k < 4; k ++) {
        size_t ny = dy[k] + y;
        size_t nx = dx[k] + x;
        d_y += dy[k];
        d_x += dx[k];

        if(ny >= N || nx >= M || v[ny][nx]) continue;

        v[ny][nx] = true;
        max_value = max(max_value, dfs(ny, nx, depth + 1, value + graph[ny][nx], d_y, d_x));
        v[ny][nx] = false;
    }

    return max_value;
}

int main()
{
    cin >> N >> M;
    graph.resize(N, vector<int>(M, 0));
    v.resize(N, vector<bool>(M, false));
    
    for(int i = 0; i < N; i ++) {
        for(int j = 0; j < M; j++) {
            cin >> graph[i][j];
        }
    }

    int max_value = 0;
    for(int i = 0; i < N; i ++) {
        for(int j = 0; j < M; j ++) {
            v[i][j] = true;
            max_value = max(max_value, dfs(i, j, 0, graph[i][j],0, 0));
            v[i][j] = false;

            for(auto s_p : speicalmoves) {
                int value = graph[i][j];
                for(auto s_p_m : s_p) {
                    size_t ny = s_p_m[0] + i;
                    size_t nx = s_p_m[1] + j;

                    if(ny >= N || nx >= M) continue;

                    value += graph[ny][nx];
                }

                max_value = max(value, max_value);
            }
        }
    }

    cout << max_value;
}