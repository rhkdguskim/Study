// https://www.acmicpc.net/problem/1194

#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <unordered_set>
#include <queue>
using namespace std;
// 0으로 갈 수 없는 경우는 종료한다.
// 너비우선탐색으로, 키와 문과 0을 찾는다.
// 키와 문을 찾았을때, 열 수 있는 곳이 있다면 계속 진행한다. 없다면 갈 수 없으므로 종료
// 3차원 배열로 문제 해결

vector<bool> keys;
vector<vector<char>> graph;
constexpr char WALL = '#';
constexpr char EMPTY = '.';
constexpr char START = '0';
constexpr char END = '1';
constexpr int MAX_DIS = 987654321;
int dy[4] = {0, 0, 1, -1};
int dx[4] = {1, -1, 0, 0};

int N, M;

bool is_lower(char c)
{
    return c >= 'a' && c <= 'z';
}

bool is_upper(char c)
{
    return c >= 'A' && c <= 'Z';
}

bool is_alpha(char c)
{
    return is_upper(c) || is_alpha(c);
}

// key(n_y, n_x, cost), end flag
vector<tuple<int, int, int>> bfs(int y, int x)
{
    vector<tuple<int, int, int>> result;
    unordered_set<char> v_key;
    vector<vector<bool>> v(N, vector<bool>(M, false));
    deque<tuple<int, int, int>> q;
    v[y][x] = true;
    q.push_back({y, x, 0});

    while(!q.empty())
    {
        auto &[cur_y, cur_x, cost] = q.front(); q.pop_front();

        for(int i = 0; i < 4; i ++)
        {
            size_t ny = cur_y + dy[i];
            size_t nx = cur_x + dx[i];

            if(ny >= N || nx >= M || v[ny][nx] || graph[ny][nx] == WALL) continue;

            v[ny][nx] = true;

            // 문이고 키가 없다면
            if(is_upper(graph[ny][nx]) && keys[graph[ny][nx] - 'A'] == false) continue;

            // 열쇠라면 다음에 열 열쇠에 넣는다.
            if(is_lower(graph[ny][nx]) && v_key.find(graph[ny][nx]) == v_key.end() && keys[toupper(graph[ny][nx]) - 'A'] == false)
            {
                v_key.insert(graph[ny][nx]);
                result.push_back({ny, nx, cost + 1});
            }

            if(graph[ny][nx] == END)
            {
                result.clear();
                result.push_back({ny, nx, cost + 1});
                return result;
            }
            
            q.push_back({ny, nx, cost + 1});
        }
    }

    return result;
}

int dfs(int y, int x, int cost)
{
    if(graph[y][x] == END)
    {
        return cost;
    }

    auto next = bfs(y, x);

    int answer = MAX_DIS;

    for(auto [ny, nx, nc] : next)
    {
        auto check = graph[ny][nx];
        
        if(check != END)
        {
            keys[toupper(check) - 'A'] = true;
        }

        //cout << ny << " " << nx << " " << nc << " \n";
        answer = min(answer, dfs(ny, nx, cost + nc));

        if(check != END)
        {
            keys[toupper(check) - 'A'] = false;
        }
    }

    return answer;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N >> M;
    graph.resize(N, vector<char>(M));
    keys.resize(26, false);
    int s_y, s_x;

    for(int i = 0; i < N; i ++)
    {
        string temp;
        cin >> temp;
        for(int j = 0; j < M; j ++)
        {
            graph[i][j] = temp[j];
            if(graph[i][j] == START)
            {
                s_y = i;
                s_x = j;
            }
        }
    }

    graph[s_y][s_x] = WALL;
    auto result = dfs(s_y, s_x, 0);
    if(result == MAX_DIS)
    {
        cout << -1;
    }
    else
    {
        cout << result;
    }
}
