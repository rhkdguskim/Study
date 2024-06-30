// https://www.acmicpc.net/problem/1756
#include <iostream>
#include <vector>
using namespace std;
int D, N;
vector<int> oven;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> D >> N;
    oven.resize(D, 0);
    cin >> oven[0];

    // 오븐은 항상 오름차순으로 정렬 되어있다.
    for(int i = 1; i < D; i ++) {
        cin >> oven[i];
        // 오븐의 크기를 최소로 갱신한다.
        if(oven[i] > oven[i-1]) oven[i] = oven[i-1];
    }

    int depth = D;
    int pizza;
    for(int i = 0; i < N; i ++) {
        cin >> pizza;
        int start = 0;
        int end = depth - 1;

        // oven의 크기가 더 작은 위치를 찾는다.
        while(end >= start) {
            int mid = (start + end) / 2;
            if (pizza > oven[mid]) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        depth = end;
        if(depth < 0) {
            cout << "0";
            return 0;
        }
    }
    cout << depth + 1;
    return 0;
}