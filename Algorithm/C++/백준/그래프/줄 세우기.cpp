// https://www.acmicpc.net/problem/2252
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int N, M;
vector<int> in_degree;
vector<vector<int>> graph;
vector<bool> v;

void dfs(int student)
{
    cout << student << ' ';
    for(auto next : graph[student])
    {
        in_degree[next] -= 1;
        if(in_degree[next] == 0 && !v[next])
        {
            v[next] = true;
            dfs(next);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N >> M;
    in_degree.resize(N+1);
    graph.resize(N+1);
    v.resize(N+1);

    int A, B;
    for(int i = 0; i < M; i ++)
    {
        cin >> A >> B;
        in_degree[B] += 1;
        graph[A].push_back(B);
    }

    for(int i = 1; i <= N; i ++)
    {
        if(in_degree[i] == 0 && !v[i])
        {
            v[i] = true;
            dfs(i);
        }
    }
}