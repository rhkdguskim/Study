#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <functional>

using namespace std;

int N, P, K;
vector<vector<pair<int, int>>> graph;

int modifiedDijkstra() {
    // Min-heap을 사용하되, 각 노드에 대해 K+1 개의 경로를 저장합니다.
    vector<vector<int>> costs(N + 1, vector<int>(K + 1, INT_MAX));
    priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
    pq.push({0, 1, 0});  // cost, node, used worst K edges

    while (!pq.empty()) {
        auto [cost, node, used] = pq.top();
        pq.pop();

        if (node == N) {
            return cost;
        }

        for (auto &[next, weight] : graph[node]) {
            int newCost = max(cost, weight);
            if (newCost < costs[next][used]) {
                costs[next][used] = newCost;
                pq.push({newCost, next, used});
            }
            if (used < K && cost < costs[next][used + 1]) {
                costs[next][used + 1] = cost;
                pq.push({cost, next, used + 1});
            }
        }
    }

    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> P >> K;
    graph.resize(N + 1);

    for (int i = 0; i < P; ++i) {
        int a, b, cost;
        cin >> a >> b >> cost;
        graph[a].push_back({b, cost});
        graph[b].push_back({a, cost});
    }

    int result = modifiedDijkstra();
    cout << (result == INT_MAX ? -1 : result) << endl;

    return 0;
}
