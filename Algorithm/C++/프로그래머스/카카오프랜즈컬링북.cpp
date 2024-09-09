// https://school.programmers.co.kr/learn/courses/30/lessons/1829
#include <vector>
#include <deque>

using namespace std;
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int bfs(vector<vector<bool>> &v, vector<vector<int>> &picture, int y, int x);

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    vector<vector<bool>> v(m, vector<bool>(n, false));
    vector<int> answer(2);

    for(int y = 0; y < m; y ++) {
        for(int x = 0; x < n; x ++) {
            if(picture[y][x] != 0 && v[y][x] == false) {
                max_size_of_one_area = max(max_size_of_one_area, bfs(v, picture, y, x));
                number_of_area += 1;
            }
        }
    }
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}

int bfs(vector<vector<bool>> &v, vector<vector<int>> &picture, int y, int x)
{
    int m = picture.size();
    int n = picture[0].size();

    int dy[4] = {0 , 0, 1, -1};
    int dx[4] = {1, -1, 0, 0};

    int cnt = 1;
    deque<pair<int, int>> q;
    q.push_back({y, x});
    v[y][x] = true;
    int cur_color = picture[y][x];

    while (!q.empty()) {
        auto cur = q.front(); q.pop_front();
        
        for(int i = 0; i < 4; i ++) {
            int ny = dy[i] + cur.first;
            int nx = dx[i] + cur.second;

            // 범위를 벗어난경우 무시
            if (ny >= m || ny < 0 || nx >= n || nx < 0) continue;

            // 이미 방문했거나 색상이 다른경우 무시
            if(picture[ny][nx] != cur_color || v[ny][nx]) continue;

            v[ny][nx] = true;

            q.push_back({ny, nx});
            cnt += 1;
        }
    }

    return cnt;
}