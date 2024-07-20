#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;
// -3, -2, -7, 5, 8
int N, S;
vector<int> arr;
unordered_map<int, int> map;
long long answer = 0;
void right(int mid, int sum)
{
    if(mid == N)
    {
        map[sum] += 1;
        return;
    }

    right(mid + 1, sum);
    right(mid + 1, sum + arr[mid]);
}

void left(int start, int sum)
{
    if(start == N / 2)
    {
        answer += map[S-sum];
        return;
    }

    left(start + 1, sum);
    left(start + 1, sum + arr[start]);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> S;
    arr.resize(N, 0);

    for(int i = 0; i < N; i ++)
    {
        cin >> arr[i];
    }

    right(N/2, 0);
    left(0, 0);
    if(S == 0)
    {
        cout << answer - 1;
    }
    else
    {
        cout << answer;
    }
}