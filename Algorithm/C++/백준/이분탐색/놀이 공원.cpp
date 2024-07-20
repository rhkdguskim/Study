// https://www.acmicpc.net/problem/1561
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

long long N;
int M;

using namespace std;
vector<int> plays;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N >> M;
    plays.resize(M);
    for(int i = 0; i < M; i++)
    {
        cin >> plays[i];
    }

    if(M >= N)
    {
        cout << N;
        return 0;
    }

    N -= M;
 
    long long start = 1;
    long long end = N * M * 30;
    long long cycle = 0;
    long long child_cnt = 0;

    // 시간안에 아이들을 태울 수 있는 횟수를 구한다.
    while(start <= end)
    {
        auto mid = (start + end) / 2;
        long cnt = 0;
        for(int i = 0; i < M; i ++)
        {
            auto v = mid / plays[i];
            cnt += v;
        }

        if (cnt >= N)
        {
            end = mid - 1;
        }
        else
        {
            cycle = mid;
            child_cnt = cnt;
            start = mid + 1;
        }
    }

    N -= child_cnt;
    int idx = 0;
    while(N)
    {
        if((cycle + 1) % plays[idx] == 0) N -= 1;

        idx += 1;
    }

    cout << idx;
    return 0;
}
