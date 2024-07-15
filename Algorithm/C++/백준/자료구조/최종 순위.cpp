#include <iostream>
#include <vector>
#include <string>

// 진입차수가 가장 낮으면서 순위도 가장 낮은 노드부터 탐색
// 진입차수가 0이고 순위가 낮은순서대로 하나씩 탐색한다.
using namespace std;
int T;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> T;
    int n, m;
    for(int i = 0; i < T; i ++)
    {
        cin >> n;
        vector<vector<int>> graph(n+1);
        vector<pair<int, int>> nodes(n+1, {0, 0}); // rank, indegree
        
        int temp;
        for(int j = 1; j <= n; j ++)
        {
            cin >> temp;
            nodes[temp].first = j;
        }

        cin >> m;
        for(int j = 0; j < m; j ++)
        {
            
        }

    }
    
    

}