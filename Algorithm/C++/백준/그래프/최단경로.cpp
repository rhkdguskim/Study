#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;
constexpr int MAX_DISTANCE = 987654321;
int V, E, K;

struct Point
{
    int distance;
    int node;
};

struct Comp
{
    bool operator()(const Point& lhs, const Point& rhs)
    {
        return lhs.distance < rhs.distance;
    }
};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> V >> E >> K;

    vector<vector<pair<int, int>>> graph(V + 1);
    
    int u, v, w;
    for(int i = 0; i < E; i++)
    {
        cin >> u >> v >> w;
        graph[u].emplace_back(v, w);
    }

    vector<int> distance(V + 1, MAX_DISTANCE);

    distance[K] = 0;
    priority_queue<Point, vector<Point>, Comp> q;
    q.push({0, K});

    while (!q.empty())
    {
        auto cur = q.top(); q.pop();

        int cur_distance = cur.distance;
        int cur_node = cur.node;

        if(distance[cur_node] < cur_distance) continue;

        for(auto& next : graph[cur_node])
        {
            int next_node = next.first;
            int next_distance = next.second + cur_distance;

            if(distance[next_node] > next_distance) {
                distance[next_node] = next_distance;
                q.push({next_distance, next_node});
            }
        }
    }
    
    for(int i = 1; i <= V; i++)
    {
        if(distance[i] == MAX_DISTANCE)
        {
            cout << "INF" << '\n';
        }
        else
        {
            cout << distance[i] << '\n';
        }
    }
}
