// https://www.acmicpc.net/problem/9251

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <tuple>

using namespace std;

string word1;
string word2;
vector<vector<int>> cache;
int s1, s2;

int solve(int s1, int s2) {
    if (0 > s1  || 0 > s2)
        return 0;

    if(cache[s1][s2] != -1) return cache[s1][s2];

    cache[s1][s2] = 0;

    if (word1[s1] == word2[s2])
    {
        cache[s1][s2] = max(cache[s1][s2], solve(s1 - 1, s2 - 1) + 1);
    }
    else 
    {
        cache[s1][s2] = max(cache[s1][s2], solve(s1 - 1, s2));
        cache[s1][s2] = max(cache[s1][s2], solve(s1, s2 - 1));
    }

    return cache[s1][s2];
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> word1;
    cin >> word2;

    s1 = word1.size() - 1;
    s2 = word2.size() - 1;

    cache.resize(word1.size(), vector<int>(word2.size(), -1));
    

    cout << solve(s1, s2);
}
