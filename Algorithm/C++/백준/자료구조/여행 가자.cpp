#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
int N, M;
vector<int> parent;

int Find(int v1)
{
    if(parent[v1] == v1)
    {
        return v1;
    }

    v1 = Find(parent[v1]);
    return v1;
}

void Union(int v1, int v2)
{
    auto p1 = Find(v1);
    auto p2 = Find(v2);

    if(p1 == p2) return;

    if(p1 > p2) {
        parent[p1] = p2;
    } else {
        parent[p2] = p1;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    parent.resize(N+1);

    for(int i = 0; i < N+1; i ++) {
        parent[i] = i;
    }

    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j ++) {
            int temp;
            cin >> temp;
            if( i != j ) {
                if(temp == 1) {
                    Union(i, j);
                }
            }
        }
    }

    int city;
    cin >> city;
    auto first = Find(city);
    for(int i = 0; i < M-1; i ++) {
        cin >> city;
        // 단 한번이라도 다르면
        if(first != Find(city)) {
            cout << "NO";
            return 0;
        }
    }
    
    // 모두다 같다면 여행가능
    cout << "YES";
    return 0;
}