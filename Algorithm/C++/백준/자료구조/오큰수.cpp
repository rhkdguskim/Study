#include <iostream>
#include <vector>
#include <stack>

using namespace std;
int N;
vector<int> NGE;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    cin >> N;

    stack<pair<int, int>> s;
    NGE.resize(N, -1);
    int temp;
    for(int i = 0; i < N; i ++) {
        cin >> temp;

        // 다음수가 더 큰수가 나왔을경우
        while(!s.empty() && temp > s.top().first) {
            auto v = s.top();
            s.pop();
            NGE[v.second] = temp;
        }

        s.push({temp, i});
    }

    for(auto v : NGE) {
        cout << v << " ";
    }
}