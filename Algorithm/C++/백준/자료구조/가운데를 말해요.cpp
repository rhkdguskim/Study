#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    priority_queue<int> l_q; // 최대 힙
    priority_queue<int, vector<int>, greater<int>> r_q; // 최소 힙
    int N;
    cin >> N;

    for(int i = 0; i < N; i++) {
        int temp;
        cin >> temp;

        if (l_q.empty() || temp <= l_q.top()) {
            l_q.push(temp);
        } else {
            r_q.push(temp);
        }

        // 균형 맞추기
        if (l_q.size() > r_q.size() + 1) {
            r_q.push(l_q.top());
            l_q.pop();
        } else if (r_q.size() > l_q.size()) {
            l_q.push(r_q.top());
            r_q.pop();
        }

        // 가운데 값 출력
        cout << l_q.top() << "\n";
    }

    return 0;
}
