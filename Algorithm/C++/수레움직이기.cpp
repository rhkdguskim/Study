// https://school.programmers.co.kr/learn/courses/30/lessons/250134
// 빨간색이 움직이거나 파란색이 먼저 움직여야한다.
// 빨간색이 움직였다면 다음은 파란색이다.
// 0빈칸, 1빨간수레시작, 2 파란수레시작, 3빨간수레도착, 4파란수레도착, 5벽
#include <string>
#include <vector>
#include <iostream>
using namespace std;

struct Point
{
    int y;
    int x;
};

static vector<vector<bool>> r_v;
static vector<vector<bool>> b_v;
static Point start_r;
static Point start_b;
static Point end_r;
static Point end_b;
static int n, m;
static int dy[4] = {0, 0, 1, -1};
static int dx[4] = {1, -1, 0, 0};
constexpr int MAX_SIZE = 987654321;

bool is_equal(Point &start, Point &end)
{
    return start.x == end.x && start.y == end.y;
}

vector<Point> get_target(vector<vector<int>> &maze, vector<vector<bool>> &v, Point &red, Point &blue, bool is_red)
{
    vector<Point> target;
    Point t = is_red ? red : blue;
    Point cmp = is_red ? blue : red;

    for(int i{0}; i < 4; i ++) {
        size_t ny = t.y + dy[i];
        size_t nx = t.x + dx[i];

        if(ny >= n || nx >= m || v[ny][nx] || maze[ny][nx] == 5)
            continue;
        
        target.push_back({(int)ny, (int)nx});
    }
    return target;
}

int back_tracking(vector<vector<int>> &maze, int cnt)
{
    bool end_red = is_equal(start_r, end_r);
    bool end_blue = is_equal(start_b, end_b);

    if(end_red && end_blue) {
        return cnt;
    }
    
    vector<Point> red_moves;
    vector<Point> blue_moves;
    if(!end_red)
        red_moves = get_target(maze, r_v, start_r, start_b, true);
    
    if(!end_blue)
        blue_moves = get_target(maze, b_v, start_r, start_b, false);

    int move = MAX_SIZE;
    // 빨간색 파란색 둘다 움직이여하는경우
    if(!end_red && !end_blue) {
        for(auto red : red_moves) {
            for(auto blue : blue_moves) {                
                // 수레끼리 서로 자리를 바꿀수 없는경우.
                if(is_equal(start_r, blue) && is_equal(start_b, red))
                    continue;
                
                // 같은 칸으로 움직일수 없는경우
                if(is_equal(red, blue))
                    continue;
                
                auto temp_r = start_r;
                auto temp_b = start_b;
                start_r = red;
                start_b = blue;
                r_v[red.y][red.x] = true;
                b_v[blue.y][blue.x] = true;
                move = min(back_tracking(maze, cnt + 1), move);
                start_r = temp_r;
                start_b = temp_b;
                r_v[red.y][red.x] = false;
                b_v[blue.y][blue.x] = false;
            }
        }
    }
    // 빨간색만 움직여야하는 경우
    else if(end_blue) {
        for(auto red : red_moves) {
            // 파란색 도착칸에 가는경우 제외
            if(is_equal(end_b, red))
                continue;

            auto temp = start_r;
            start_r = red;
            r_v[red.y][red.x] = true;
            move = min(back_tracking(maze, cnt + 1), move);
            start_r = temp;
            r_v[red.y][red.x] = false;
        }
    }
    // 파란색만 움직여야하는 경우
    else {
        for(auto blue : blue_moves) {
            // 빨간색 도착칸에 가는 경우 제외
            if(is_equal(end_r, blue))
                continue;

            auto temp = start_b;
            start_b = blue;
            b_v[blue.y][blue.x] = true;
            move = min(back_tracking(maze, cnt + 1), move);
            start_b = temp;
            b_v[blue.y][blue.x] = false;
        }
    }

    return move;
};

int solution(vector<vector<int>> maze) {
    n = maze.size();
    m = maze[0].size();
    for(int i{0}; i < n; i ++) {
        for(int j{0}; j < m; j ++) {
            auto cur = maze[i][j];
            switch(cur)
            {
                case 1:
                    start_r = {i, j};
                    break;
                case 2:
                    start_b = {i, j};
                    break;
                case 3:
                    end_r = {i, j};
                    break;    
                case 4:
                    end_b = {i ,j};
                    break;
                default:
                    break;
            }
        }
    }

    r_v.resize(n, vector<bool>(m, false));
    b_v.resize(n, vector<bool>(m, false));
    r_v[start_r.y][start_r.x] = true;
    b_v[start_b.y][start_b.x] = true;
    auto answer = back_tracking(maze, 0);
    return answer == MAX_SIZE ? 0 : answer;
}