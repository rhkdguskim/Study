// https://www.acmicpc.net/problem/9935

#include <iostream>
#include <string>
#include <stack>
using namespace std;
string words;
string explode;

int main()
{  
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> words >> explode;
    int n = words.size();
    int m = explode.size();
    string s;

    for(int i = 0; i < n; i ++) {
        s.push_back(words[i]);

        int cnt = s.size();
        while(s.size() >= m && explode == s.substr(cnt - m, m)) {
            for(int j = 0; j < m; j ++) s.pop_back();
        }
    } 

    if(s.size() == 0) cout << "FRULA";
    else cout << s;
}