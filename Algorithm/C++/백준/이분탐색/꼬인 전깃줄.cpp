// https://www.acmicpc.net/problem/1365
#include <iostream>
#include <vector>
#include <string>

using namespace std;
int N;
vector<int> A;
int bisect(int v, const vector<int>& T)
{
    int idx = -1;
    int start = 0;
    int end = T.size() - 1;
    while(start <= end)
    {
        int mid = (start + end) / 2;

        if(T[mid] >= v)
        {
            idx = mid;
            end = mid - 1;
        }
        else
        {
            start = mid + 1;
        }
    }

    return idx;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N;
    for(int i = 0; i < N; i ++)
    {
        int temp;
        cin >> temp;
        A.push_back(temp);
    }

    vector<int> T;
    for(int v : A)
    {
        int idx = bisect(v, T);
        if(idx == -1)
        {
            T.push_back(v);
        }
        else
        {
            T[idx] = v;
        }
    }

    cout << A.size() - T.size();

}