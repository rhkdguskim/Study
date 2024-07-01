// https://www.acmicpc.net/problem/2493
#include <iostream>
#include <stack>
#include <vector>

using namespace std;
vector<int> answer;
int N;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    stack<pair<int, int>> s;
    cin >> N;
    int tmp;
    for(int i = 1; i <= N; i ++) {
        cin >> tmp;

        while(!s.empty() && tmp >= s.top().first) {
            s.pop();
        }

        if(!s.empty()) {
            cout << s.top().second << " ";
        } else {
            cout << 0 << " ";
        }
        
        s.push({tmp, i});
    }
}