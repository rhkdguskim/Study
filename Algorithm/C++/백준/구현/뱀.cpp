#include <iostream>
#include <deque>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

constexpr int RIGHT = 0;
constexpr int DOWN = 1;
constexpr int LEFT = 2;
constexpr int UP = 3;
int dy[4] = {0, 1, 0, -1};
int dx[4] = {1, 0, -1, 0};
int N, K, L;

namespace std {
    template<>
    struct hash<pair<int, int>> {
        size_t operator()(const pair<int, int>& t) const {
            auto hash1 = t.first;
            auto hash2 = t.second;
            return hash1 ^ (hash2 << 1);
        }
    };
}
deque<pair<int, int>> tail;
vector<vector<bool>> v;
unordered_map<int, string> time_d;
unordered_set<pair<int, int>> apple;

int change_direction(int direction, const bool reversed)
{
    if(reversed) {
        direction += 3;
    } else {
        direction += 1;
    }

    return direction % 4;
}

pair<int, int> move(const pair<int, int> &cur_pos, const int direction)
{
    size_t ny = dy[direction] + cur_pos.first;
    size_t nx = dx[direction] + cur_pos.second;

    // 벽을 벗어나거나 자기자신과 충돌할 경우 현재위치를 리턴한다.
    if(ny >= N || nx >= N || v[ny][nx])
        return cur_pos;
    
    v[ny][nx] = true;
    tail.push_back({ny, nx});
    return {ny, nx};
}

void eat_apple(const pair<int, int> &cur_pos)
{
    int y = cur_pos.first;
    int x = cur_pos.second;

    // 사과가 없다면
    if(apple.find({y, x}) == apple.end())
    {
        // 꼬리를 삭제한다.
        auto remove = tail.front();
        tail.pop_front();
        v[remove.first][remove.second] = false;
    }
    else {
        // 사과를 먹는다.
        apple.erase({y, x});
    }
}

int main()
{
    cin >> N >> K;
    v.resize(N, vector<bool>(N, false));

    for(int i = 0; i < K; i++) {
        int y, x;
        cin >> y >> x;
        y -= 1; x -= 1;
        apple.insert({y, x});
    }

    cin >> L;
    for(int i = 0; i < L; i ++) {
        int time;
        string d;
        cin >> time >> d;
        time_d[time] = d;
    }

    int time = 0;
    int direction = RIGHT;
    pair<int, int> cur_pos(0, 0);
    v[0][0] = true;
    tail.push_back({0 ,0});
    while(true) {
        // 시간에 도달하면 방향을 바꾼다.
        if(time_d.find(time) != time_d.end()) {
            bool reverse = time_d[time] == "L";
            direction = change_direction(direction, reverse);
        }

        auto next_pos = move(cur_pos, direction);
        
        time += 1;
        // 움직이지 못하는 상황이면 게임을 종료한다.
        if(next_pos == cur_pos) {
            break;
        }

        cur_pos = next_pos;
        eat_apple(cur_pos);
        
    }

    cout << time;
}
