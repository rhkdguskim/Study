// https://school.programmers.co.kr/learn/courses/30/lessons/250136
#include <string>
#include <vector>
#include <deque>
#include <set>

using namespace std;

struct Point {
    size_t y;
    size_t x;
};

vector<Point> bfs(vector<vector<int>> &land, size_t start_y, size_t start_x, int n, int m, vector<vector<bool>> &v)
{
    deque<Point> queue;
    vector<Point> group;
    queue.push_back({start_y, start_x});
    group.push_back({start_y, start_x});
    v[start_y][start_x] = true;

    vector<std::pair<size_t, size_t>> moves = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    
    while(!queue.empty()) {
        auto cur = queue.front();
        queue.pop_front();

        for(auto move : moves) {
            size_t ny = cur.y + move.first;
            size_t nx = cur.x + move.second;

            if (ny >= n || nx >= m || v[ny][nx] || land[ny][nx] == 0)
                continue;
            
            v[ny][nx] = true;
            queue.push_back({ny, nx});
            group.push_back({ny, nx});
        }
    }

    return group;
}  

int solution(vector<vector<int>> land) {
    int n = land.size();
    int m = land[0].size();
    
    vector<vector<bool>> v(n, vector<bool>(m, 0)); // 크기와 초기값.
    vector<int> col(m, 0);

    int answer = 0;

    for(int i = 0; i < m; i++) {
        int total = 0;
        for(int j = 0; j < n; j++) {
            if(land[j][i] == 1 && !v[j][i]) {
                auto g = bfs(land, j, i, n, m, v);
                set<int> v_x;
                for(const auto &point : g) {
                    if(v_x.find(point.x) == v_x.end()) {
                        col[point.x] += g.size();
                        v_x.insert(point.x);
                    }
                }
            }
        }
    }

    for(auto value : col) {
        answer = max(value, answer);
    }

    return answer;
}
