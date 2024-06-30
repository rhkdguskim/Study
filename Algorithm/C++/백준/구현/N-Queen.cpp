#include <iostream>
#include <vector>

using namespace std;

vector<vector<bool>> map;
int n;
int answer = 0;

bool check(int r, int c) {
    for(int i = r-1, cnt = 1; i >= 0; i--, cnt++) {
        // 열 체크
        if(map[i][c])
            return false;
        // 대각선 체크
        // 왼쪽위 대각선
        if(c - cnt >= 0 && map[i][c - cnt])
            return false;
        // 오른쪽 위 대각선
        if(c + cnt < n && map[i][c + cnt])
            return false;
    }
    return true;
}

void solve(int r) {
    if(r == n) {
        answer++;
        return;
    }
    for(int c = 0; c < n; c++) {
        if(check(r, c)) {
            map[r][c] = true;
            solve(r + 1);
            map[r][c] = false;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    map.resize(n, vector<bool>(n, false));
    
    solve(0);
    cout << answer;
}