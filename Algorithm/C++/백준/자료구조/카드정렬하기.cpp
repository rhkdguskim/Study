#include <iostream>
#include <queue>

using namespace std;
int N;
priority_queue<int, vector<int>, greater<int>> cards;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> N;
    int tmp;
    for(int i = 0; i < N; i ++) {
        cin >> tmp;
        cards.push(tmp);
    }

    int answer  = 0;

    while(cards.size() > 1) {
        auto v1 = cards.top(); cards.pop();
        auto v2 = cards.top(); cards.pop();

        auto v3 = v1 + v2;
        answer += v3;
        
        cards.push(v3);
    }

    cout << answer;

}