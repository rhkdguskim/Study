// https://www.acmicpc.net/problem/2011
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

string word;
int N;
vector<unordered_map<string, int>> dp;
unordered_map<int, char> alpha;

int dfs(int index, string cur)
{
    // 더이상 암호할 수 없는경우
    if(index >= N-1) return 1;

    if(dp[index].find(cur) != dp[index].end()) return dp[index][cur];

    int cnt = 0;
    if(index + 1 >= N-1)
    {
        auto new_word = word.substr(index, index + 2);
        int num = stoi(new_word);
        if(26 >= num)
        {
            cnt += dfs(index + 2, cur + new_word);
        }
    }

    auto new_word = word.substr(index, index + 1);

    cnt += dfs(index + 1, cur + new_word);
    dp[index][cur] = cnt;
    return cnt;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> word;
    N = word.size();
    dp.resize(N);

    char temp = 'A';
    for(int i = 1; i <= 26; i ++)
    {
        alpha[i] = temp + i-1;
    }

    cout << dfs(0, "");
}