// https://www.acmicpc.net/problem/14503
#include <iostream>
#include <vector>

using namespace std;

constexpr int DIRTY = 0;
constexpr int WALL = 1;
constexpr int CLEAN = 2;

constexpr int NORTH = 0;
constexpr int EAST = 1;
constexpr int SOUTH = 2;
constexpr int WEST = 3;

int n, m, answer;
int start_y, start_x, direction;
vector<vector<int>> map;
vector<vector<int>> moves = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}}; // 북 동 남 서 순

void clean_up(int y, int x) // 방을 청소한다.
{
    if(map[y][x] == DIRTY)
    {
        map[y][x] = CLEAN;
        answer += 1;
    }
}

bool find_dirty_room(int y, int x) // 빈칸을 찾는다.
{
    for(auto d : moves)
    {
        size_t ny = d[0] + y;
        size_t nx = d[1] + x;

        if (ny >= n || nx >= m) continue;

        if(map[ny][nx] == DIRTY)
        {
            return true;
        }
    }
    return false;
}

int rotate(int dir) // 반 시계 방향으로 90도 회전
{
    if(dir == 0) {
        return 3;
    }
    else {
        return dir - 1;
    }
}

pair<int, int> go(int y, int x, int dir, bool reverse)
{
    // 후진해야하면 반시계방향으로 2번 회전시킨 방향으로 회전.
    if(reverse)
    {
        dir = rotate(rotate(dir));
    }

    size_t ny = moves[dir][0] + y;
    size_t nx = moves[dir][1] + x;

    if(ny >= n || nx >= m)
    {
        return {y, x};
    }

    // 반대방향으로 움직인다면
    if(reverse) {
        // 벽이면 종료.
        if(map[ny][nx] == WALL) return {y, x};
    } else {
        // 청소되지 않는 빈칸인 경우만
        if(map[ny][nx] == CLEAN || map[ny][nx] == WALL) return {y, x};
    }

    // 다음 Pos로 움직인다.
    return {ny, nx};
}


int main()
{
    answer = 0;
    cin >> n >> m >> start_y >> start_x >> direction;

    map.resize(n, vector<int>(m, DIRTY));
    for(int i = 0; i < n; i ++)
    {
        for(int j = 0; j < m; j++)
        {
            cin >> map[i][j];
        }
    }

    while(true) {
        clean_up(start_y, start_x);
        auto ret = find_dirty_room(start_y, start_x);
        if(!ret) {
            // 빈칸이 없는경우
            auto n_p = go(start_y, start_x, direction, true);

            // 후진할 수 없다면 동작을 멈춘다.
            if(n_p.first == start_y && n_p.second == start_x) break;

            // 후진한다.
            start_y = n_p.first;
            start_x = n_p.second;
        } else {
            // 반시계 방향으로 회전한다.
            direction = rotate(direction);

            // 바라보는 방향으로 빈칸인 경우 전진한다.
            auto n_p = go(start_y, start_x, direction, false);
            start_y = n_p.first;
            start_x = n_p.second;
        }
    }

    cout << answer;
}