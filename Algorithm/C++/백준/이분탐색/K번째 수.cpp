#include <iostream>
#include <algorithm>
// 1, 2, 3, 4, 5, ... 2, 4, 6, 8
// 이분탐색한다. mid를 기준으로 체크. mid*mid 만큼 개수를 비교해본다.
// 1 부터 mid, 2부터 mid ... N mid

using namespace std;

long long N, k;

long long bisect()
{
    long long start = 1;
    long long end = N * N;
    long long answer = 0;

    while (start <= end)
    {
        long long mid = (start + end) / 2;
        long long cnt = 0;

        for (int i = 1; i <= N; i++)
        {
            cnt += min(mid / i, N);
        }

        if (cnt >= k)
        {
            answer = mid;
            end = mid - 1;
        }
        else
        {
            start = mid + 1;
        }
    }

    return answer;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> k;
    cout << bisect();
}
