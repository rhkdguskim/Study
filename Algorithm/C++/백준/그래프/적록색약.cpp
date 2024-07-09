#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <functional>

using namespace std;
int N;
int dy[4] = {0, 0, 1, -1};
int dx[4] = {1, -1, 0, 0};
vector<vector<char>> graph;

void bfs(int i, int j, vector<vector<bool>> &v, function<bool(void)> cmp)
{
    function<bool(void)> cmp;
    auto color = graph[i][j];
    deque<pair<int, int>> q;
    v[i][j] = true;
    q.push_back({i, j});

    while(!q.empty())
    {
        auto cur = q.front(); q.pop_front();
        for(int k = 0; k < 4; k ++)
        {
            size_t ny = cur.first + dy[k];
            size_t nx = cur.second + dx[k];

            if(ny >= N || nx >= N || v[ny][nx] || cmp) continue;

            v[ny][nx] = true;
            q.push_back({ny, nx});
        }   
    }
}


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int group, group2;
    
    cin >> N;

    graph.resize(N, vector<char>(N));
    vector<vector<bool>> v1(N, vector<bool>(N));
    vector<vector<bool>> v2(N, vector<bool>(N));
    string temp;
    for(int i = 0; i < N; i ++)
    {
        cin >> temp;
        for(int j = 0; j < N; j++)
        {
            graph[i][j] = temp[j];
        }
    }

    for(int i = 0; i < N; i ++)
    {
        for(int j = 0; j < N; j ++)
        {
            
            if(!v1[i][j])
            {
                group += 1;
                bfs(i, j, v1, (void)[]
                {
                    return true;
                });
            }
            
            if(!v2[i][j])
            {
                group2 += 1;
                bfs(i, j, v2);
            }
        }
    }
}