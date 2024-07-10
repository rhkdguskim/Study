// https://www.acmicpc.net/problem/2357
#include <iostream>
#include <vector>
#include <string>

using namespace std;
int N, M;
vector<pair<int, int>> tree;
vector<int> nums;
constexpr int MAX_SIZE = -1000000001;
constexpr int MIN_SIZE = 1000000001;

void init(int start, int end, int node)
{
    // leaf 노드에 도달한경우
    if(start == end)
    {
        tree[node].first = nums[start];
        tree[node].second = nums[start];
    } 
    else 
    {
        int mid = (start + end) / 2;
        init(start, mid, node*2);
        init(mid + 1, end, node*2+1);
        tree[node].first = min(tree[node*2].first, tree[node*2+1].first);
        tree[node].second = max(tree[node*2].second, tree[node*2+1].second);
    }
}

pair<int, int> query(int start, int end, int left, int right, int node)
{
    // 범위를 아예 벗어난경우
    if(end < left || start > right)
    {
        return {MIN_SIZE, MAX_SIZE};
    }
    // 범위에 들어온경우
    if(start >= left && end <= right) 
    {
        return tree[node];
    } 
    // 범위에 걸친경우
    else
    {
        int mid = (start+end) / 2;
        auto l = query(start, mid, left, right, node*2);
        auto r = query(mid + 1, end, left, right, node*2+1);
        return {min(l.first, r.first), max(l.second, r.second)};
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;
    nums.resize(N);
    tree.resize(4*N);

    for(int i = 0; i < N; i++) 
    {
        cin >> nums[i];
    }

    init(0, N-1, 1);

    int a, b;
    for(int i = 0; i < M; i++)
    {
        cin >> a >> b;
        a -= 1;
        b -= 1;
        pair<int, int> result;
        if(b > a)
        {
            result = query(0, N-1, a, b, 1);
        }
        else
        {
            result = query(0, N-1, b, a, 1);
        }

        cout << result.first << " " << result.second << "\n";
        
    }
}