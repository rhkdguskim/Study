// https://www.acmicpc.net/problem/1450
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
// 넣은경우와 넣지 않는 경우를 구한다.

using namespace std;
int N;
long long C;
vector<long long> weights;

int dfs(int idx, long long weight)
{
    if(weight > C) return 0;

    if(idx == N)
    {
        if(C >= weight) return 1;
        else return 0;
    }   

    return dfs(idx+1, weights[idx] + weight) + dfs(idx+1, weight);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N >> C;
    weights.reserve(N);
    for(int i = 0; i < N; i ++)
    {
        cin >> weights[i];
    }

    sort(weights.begin(), weights.end());
    cout << dfs(0, 0);
}