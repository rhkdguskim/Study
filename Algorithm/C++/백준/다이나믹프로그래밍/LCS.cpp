#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <tuple>

using namespace std;

string word1;
string word2;
map<tuple<int, int, int, int>, int> dp;

int solve(int s1, int e1, int s2, int e2) {
    if (s1 > e1 || s2 > e2)
        return 0;

    if (dp.find({s1, e1, s2, e2}) != dp.end())
        return dp[{s1, e1, s2, e2}];

    int &temp = dp[{s1, e1, s2, e2}] = 0;

    if (word1[s1] == word2[s2])
        temp = max(temp, solve(s1 + 1, e1, s2 + 1, e2) + 1);

    // 일치하지 않을 경우 다음 문자로 넘어감
    temp = max(temp, solve(s1 + 1, e1, s2, e2));
    temp = max(temp, solve(s1, e1, s2 + 1, e2));

    return temp;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> word1;
    cin >> word2;

    int s1 = 0;
    int e1 = word1.size() - 1;
    int s2 = 0;
    int e2 = word2.size() - 1;

    cout << solve(s1, e1, s2, e2);
}
