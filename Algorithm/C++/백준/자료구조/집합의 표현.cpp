// https://www.acmicpc.net/problem/1717
#include <iostream>
#include <vector>

using namespace std;
int n, m;
vector<int> parent;

int find(int node)
{
    if (parent[node] == node) return node;

    parent[node] = find(parent[node]);
    return parent[node];
}

void sum_subset(int a, int b)
{
    auto p1 = find(a);
    auto p2 = find(b);

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
    cin >> n >> m;

    parent.resize(n+1, 0);

    for(int i = 0; i < n+1; i ++) {
        parent[i] = i;
    }

    for(int i = 0; i < m; i ++) {
        int op, a, b;
        cin >> op >> a >> b;
        if(op == 0) {
            sum_subset(a, b);
        } else {
            auto p1 = find(a);
            auto p2 = find(b);
            if(p1 == p2) {
                cout << "YES\n";
            } else {
                cout << "NO\n";
            }
        }
    }
}