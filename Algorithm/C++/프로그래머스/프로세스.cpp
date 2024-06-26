#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> priorities, int location) {

    // priority_queue는 기본적으로 내림차순 정렬
    priority_queue<int> pq;
    queue<pair<int, int>> q;
    int answer = 0;

    int index = 0;
    for(int process : priorities)
    {
        pq.push(process);
        q.push({index, process});
        index += 1;
    }

    while(q.size() > 0) {

        // 실행 대기 큐에서 대기중인 프로세스를 하나 꺼냅니다.
        auto pair = q.front();
        int idx_process = pair.first;
        int cur_process = pair.second;
        q.pop();

        auto max_process = pq.top();
        // 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 큐에 다시 넣는다.
        if (max_process > cur_process) {
            q.push({idx_process, cur_process});
        // 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행시킵니다.
        } else {
            pq.pop();
            answer += 1;
            if (idx_process == location) {
                break;
            }
        }
    }
    return answer;
}
