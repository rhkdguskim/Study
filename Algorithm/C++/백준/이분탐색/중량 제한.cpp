// https://www.acmicpc.net/problem/1939
#include <iostream>
#include <vector>
#include <deque>
#include <utility>

using namespace std;

int N, M;
int S, E;
vector<vector<pair<int, int>>> graph;

bool bfs(int weight) {
    vector<bool> visited(N+1, false);
    deque<int> q;
    q.push_back(S);
    visited[S] = true;
    
    while (!q.empty()) {
        int current = q.front();
        q.pop_front();
        
        for (auto& edge : graph[current]) {
            int next = edge.first;
            int limit = edge.second;
            if (!visited[next] && limit >= weight) {
                if (next == E) return true; 
                visited[next] = true;
                q.push_back(next);
            }
        }
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N >> M;
    graph.resize(N+1);
    int A, B, C;
    for (int i = 0; i < M; i++) {
        cin >> A >> B >> C;
        graph[A].push_back({B, C});
        graph[B].push_back({A, C});
    }

    cin >> S >> E;

    long start = 0; long end = 1000000000;
    long result = 0;

    while (start <= end) {
        long mid = (start + end) / 2;
        if (bfs(mid)) {
            result = mid;
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }

    cout << result << endl;

    return 0;
}
