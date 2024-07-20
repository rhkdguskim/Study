// https://www.acmicpc.net/problem/2352


#include <iostream>
#include <vector>
#include <string>

using namespace std;
int n;
vector<int> ls;

int bisect(const int v)
{
    int start = 0;
    int end = ls.size() - 1;
    int answer = -1;
    while(start <= end)
    {
        int mid = (start + end) / 2;

        if(ls[mid] >= v)
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
    
    cin >> n;
    int temp;
    for(int i = 0; i < n; i ++)
    {
        cin >> temp;
        int idx = bisect(temp);
        if(idx == -1)
        {
            ls.push_back(temp);
        }
        else
        {
            ls[idx] = temp;
        }
    }
    
    cout << ls.size();
}