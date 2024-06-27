#include <iostream>
#include <deque>
using namespace std;

int n, w, L;
constexpr int EMPTY = 0;

int main() {
    cin >> n >> w >> L;
    deque<int> bridge(w, EMPTY);
    deque<int> trucks;
    int bridge_weight = 0;

    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        trucks.push_back(t);
    }

    int answer = 0;
    while (!trucks.empty()) {
        answer++;

        // 다리를 건너고 있는 마지막 트럭이 다리 끝에 도달하면 다리에서 내린다
        bridge_weight -= bridge.back();
        bridge.pop_back();

        // 새 트럭이 다리에 올라갈 수 있는지 검사
        if (bridge_weight + trucks.front() <= L) {
            int new_truck = trucks.front();
            trucks.pop_front();
            bridge.push_front(new_truck);
            bridge_weight += new_truck;
        } else {
            bridge.push_front(EMPTY);
        }
    }

    cout << answer + bridge.size() << endl;
    return 0;
}
