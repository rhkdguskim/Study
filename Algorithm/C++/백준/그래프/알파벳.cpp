// https://www.acmicpc.net/problem/1987
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>
using namespace std;
int R, C;
vector<vector<char>> graph;
vector<vector<vector<pair<unordered_set<char>, int>>>> dp;
int dy[4] = {0, 0, -1, 1};
int dx[4] = {-1, 1, 0, 0};

void copy(unordered_set<char> &src, unordered_set<char> &dst)
{    
    for(auto &v : dst)
    {
        src.insert(v);
    }
}

void dfs(int i, int j, int dir, unordered_set<char> current)
{
    copy(dp[i][j][dir].first, current);
    dp[i][j][dir].second = current.size();

    for(int k = 0; k < 4; k ++)
    {
        size_t ny = dy[k] + i;
        size_t nx = dx[k] + j;


        dfs(ny, nx, dir, current);
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> R >> C;

    graph.resize(R, vector<char>(C));
    dp.resize(R, vector<vector<pair<unordered_set<char>, int>>>(C, vector<pair<unordered_set<char>, int>>(4)));
    
    for(int i = 0; i < R; i ++)
    {
        string temp;
        cin >> temp;
        for(int j = 0; j < C; j ++)
        {
            graph[i][j] = temp[j];
            for(int k = 0; k < 4; k ++)
            {
                dp[i][j][k].second = 1;
                dp[i][j][k].first.insert(temp[j]);
            }
            
        }
    }
}