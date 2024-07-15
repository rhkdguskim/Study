// https://www.acmicpc.net/problem/9370

#include <iostream>
#include <vector>
#include <string>
#include <queue>
// 출발지에서 다른 목적지까지의 최단경로
// g에서 다른 목적지까지의 최단경로
// h에서 다른 목적지까지의 최단경로

// 아래의 둘중 하나라도 만족할경우 g,h를 반드시 거친다.
// 출발지 -> g -> h -> 목적지 == 출발지 -> 목적지
// 출발지 -> h -> g -> 목적지 == 출발지 -> 목적지

using namespace std;
constexpr int MAX_DISTANCE = 987654321;

int T;
int n, m, t;
int s, g, h;
int a, b, d;

vector<int> dijikstra(int start, const vector<vector<pair<int, int>>> &graph)
{
    vector<int> d(n+1, MAX_DISTANCE);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
    q.push({0, start});

    while(!q.empty())
    {
        auto [distance, node] = q.top(); q.pop();

        if(distance > d[node]) continue;

        d[node] = distance;

        for(auto p : graph[node])
        {
            auto new_distance = p.second;
            auto next = p.first;
            auto cost = new_distance + distance;
            if(d[next] > cost)
            {
                d[next] = cost;
                q.push({cost, next});
            }
        }
    }

    return d;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    while(T--)
    {
        vector<vector<pair<int, int>>> graph;
        vector<int> dst;
        priority_queue<int, vector<int>, greater<int>> answer;

        
        cin >> n >> m >> t;
        cin >> s >> g >> h;
        graph.resize(n+1);
        
        for(int i = 0; i < m; i ++)
        {
            cin >> a >> b >> d; // a with b cost d
            graph[a].push_back({b, d});
            graph[b].push_back({a, d});
        }

        int temp;
        for(int i = 0; i < t; i ++)
        {
            cin >> temp;
            dst.push_back(temp);
        }

        auto d_s = dijikstra(s, graph);
        auto d_g = dijikstra(g, graph);
        auto d_h = dijikstra(h, graph);

        for(auto node : dst)
        {
            auto chk = d_s[node];
            auto chk1 = d_s[h] + d_h[g] + d_g[node];
            auto chk2 = d_s[g] + d_g[h] + d_h[node];

            if(chk != MAX_DISTANCE && (chk == chk1 || chk == chk2))
            {
                answer.push(node);
            }
        }
        
        while(!answer.empty())
        {
            auto v1 = answer.top(); answer.pop();
            cout << v1 << ' ';
        }
    
        cout << '\n';
    }
}
