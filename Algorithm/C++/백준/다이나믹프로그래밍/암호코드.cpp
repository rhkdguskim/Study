// https://www.acmicpc.net/problem/2011
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

string word;
int N;
vector<int> dp;

constexpr int DIV = 1000000;
int dfs(int index) {
    // 암호를 끝까지 해석한 경우
    if (index == N) {
        return 1;
    }

    // 이미 계산한 값이 있는 경우
    if (dp[index] != -1) return dp[index];

    int cnt = 0;
    if (index < N - 1) {  // 다음 두 자리를 확인할 수 있는 경우
        int num = (word[index] - '0') * 10 + (word[index + 1] - '0');
        // 10 또는 20인 경우
        if (num == 10 || num == 20) {
            cnt = (cnt + dfs(index + 2)) % DIV;
        }
        // 11부터 26 사이인 경우
        else if (num >= 11 && num <= 26) {
            cnt = (cnt + dfs(index + 2)) % DIV;
        }
    }

    if (word[index] != '0') {  // 한 자리 수 확인 (0으로 시작할 수 없음)
        cnt = (cnt + dfs(index + 1)) % DIV;
    }

    dp[index] = cnt;
    return cnt;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> word;

    if (word[0] == '0') {  // '0'으로 시작하는 경우
        cout << 0;
        return 0;
    }

    N = word.size();
    dp.resize(N, -1);
    cout << dfs(0);
}