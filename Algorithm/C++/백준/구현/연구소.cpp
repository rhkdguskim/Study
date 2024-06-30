#include <iostream>
#include <string>
#include <vector>
#include <deque>
using namespace std;

int n, m;
int answer = 0;
int dy[4] = {1, -1, 0, 0};
int dx[4] = {0, 0, 1, -1};
vector<vector<int>> map;
vector<pair<int, int>> virus;

int empty_size = 0;
constexpr int EMPTY = 0;
constexpr int WALL = 1;
constexpr int VIRUS = 2;

int get_safe_area()
{
    vector<vector<bool>> v(n, vector<bool>(m, false));
    
    for(auto pair : virus)
    {
        v[pair.first][pair.second] = true;
    }

    deque<pair<int, int>> q(virus.begin(), virus.end());

    int safe_area = empty_size;
    safe_area -= 3;

    while(!q.empty())
    {
        auto pair = q.front(); q.pop_front();
        
        auto y = pair.first;
        auto x = pair.second;

        for(int i = 0; i < 4; i ++) 
        {
            size_t ny = dy[i] + y;
            size_t nx = dx[i] + x;
            if(ny >= n || nx >= m)  continue;

            if(!v[ny][nx] && map[ny][nx] == EMPTY)
            {
                v[ny][nx] = true;
                q.push_back({ny, nx});
                safe_area -= 1;
            }
        }
    }

    return safe_area;
}

void go(int idx, int cnt)
{
    if(cnt == 3 || idx == n*m) {
        if(cnt == 3)
        {
            answer = max(answer, get_safe_area());
        }
        return;
    }

    for(int i = idx; i < n*m; i ++)
    {
        auto y = i / m;
        auto x = i % m;
        if(map[y][x] == EMPTY)
        {
            map[y][x] = WALL;
            go(i + 1, cnt + 1);
            map[y][x] = EMPTY;
        }
    }
}

int main()
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
    cin >> n >> m;
    map.resize(n, vector<int>(m, 0));

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            cin >> map[i][j];
            if(map[i][j] == VIRUS)
            {
                virus.push_back({i, j});
            }
            else if(map[i][j] == EMPTY)
            {
                empty_size += 1;
            }
        }
    }

    go(0, 0);
    cout << answer;
}