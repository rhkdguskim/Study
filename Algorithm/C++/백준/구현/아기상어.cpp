// https://www.acmicpc.net/problem/16236
#include <iostream>
#include <queue>
#include <deque>
#include <vector>
#include <tuple>

using namespace std;
struct Point {
    int y, x, distance;
};

struct Cmp {
    bool operator()(const Point& p1, const Point &p2) const
    {
        if(p1.distance == p2.distance) {
            if(p1.y == p2.y) {
            return p1.x > p2.x; // x가 작은게 우선순위가 높다.
        }
        // y가 작은게 우선순위가 높다.
        return p1.y > p2.y;
        }
        
        // 거리가 작은게 우선순위가 높다.
        return p1.distance > p2.distance;
    }
};
constexpr int EMPTY = 0;
constexpr int SHARK = 9;
int N;
vector<vector<int>> graph;
pair<int, int> shark_pos;
int shark_size = 2;

int dy[4] = {0, 0, 1, -1};
int dx[4] = {1, -1, 0, 0};

priority_queue<Point, std::vector<Point>, Cmp> get_fishs(pair<int, int> &shark_pos, int shark_size)
{
    priority_queue<Point, std::vector<Point>, Cmp> fishs;
    deque<tuple<int, int, int>> q;
    vector<vector<bool>> v(N, vector<bool>(N, false));
    v[shark_pos.first][shark_pos.second] = true;
    q.push_back({shark_pos.first, shark_pos.second, 0});

    while(!q.empty()) {
        auto cur = q.front(); q.pop_front();
        int y = get<0>(cur);
        int x = get<1>(cur);
        int distance = get<2>(cur);
        for(int i = 0; i < 4; i ++) {
            size_t ny = y + dy[i];
            size_t nx = x + dx[i];

            if(ny >= N || nx >= N || v[ny][nx]) continue;

            // 상어가 자기자신보다 작거나 같은 경우만 지나갈 수 있음.
            if(graph[ny][nx] > shark_size) continue;
            
            v[ny][nx] = true;
            // 자기자신보다 작은 상어만 먹을 수 있음.
            Point t {(int)ny, (int)nx, distance + 1};
            if(graph[ny][nx] != shark_size && graph[ny][nx] != EMPTY) {
                fishs.push(t);
            }

            q.push_back(make_tuple(ny, nx, distance + 1));
        }
    }
    return fishs;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    graph.resize(N, vector<int>(N, 0));

    for(int i = 0; i < N; i ++) {
        for(int j = 0; j < N; j ++) {
            cin >> graph[i][j];
            if(graph[i][j] == SHARK) {
                shark_pos = {i, j};
                graph[i][j] = EMPTY;
            }
        }
    }
    int answer = 0;
    int eat_count = 0;
    while(true) {
        auto fishs = get_fishs(shark_pos, shark_size);
        if(fishs.empty())
            break;

        Point fish = fishs.top();
        answer += fish.distance;
        eat_count += 1;
        graph[fish.y][fish.x] = EMPTY;
        shark_pos = {fish.y, fish.x};
        if(eat_count == shark_size) {
            eat_count = 0;
            shark_size += 1;
        }
    }

    cout << answer;
}
