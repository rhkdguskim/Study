// https://www.acmicpc.net/problem/3020

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

int N, H;
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> H;

    vector<int> a;
    vector<int> b;
    int temp;
    for(int i = 0; i < N; i ++)
    {
        cin >> temp;
        if(i % 2 == 0)
        {
            a.push_back(temp);
        }
        else
        {
            b.push_back(temp);
        }
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    
    unordered_map<int, int> answer;
    for(int h = 1; h <= H; h ++)
    {
        int cnt = a.end() - lower_bound(a.begin(), a.end(), h);
        int cnt2 = b.end() - lower_bound(b.begin(), b.end(), H - h + 1);
        answer[cnt+cnt2] += 1;
        
        //cout << cnt << " " << cnt2 << "\n";
    }

    int min_v = N;
    for(auto it : answer)
    {
        if(min_v > it.first)
        {
            min_v = it.first;
        }
    }
    
    cout << min_v << " " << answer[min_v];
}
