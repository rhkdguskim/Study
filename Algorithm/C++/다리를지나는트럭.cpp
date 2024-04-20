#include <string>
#include <vector>
#include <deque>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {

    int answer = 0;
    int currentWeight = 0;
    int currentCnt = 0;
    deque<int> q;

    for(int i = 0; i < bridge_length; i ++)
    {
        q.push_back(0);
    }

    for(int i = 0; i < truck_weights.size(); i ++)
    {
        // 마지막 deque에서 트럭을 꺼낸다. 트럭이 있다면 무게와 개수를 줄이고 없다면 무시
        int truck = q.back();
        q.pop_back();
        // 트럭이 존재한다면
        if(truck > 0) {
            currentWeight -= truck;
            currentCnt -= 1;
        }

        // 주어진 조건에 만족하면 트럭을 추가한다.
        int new_truck = truck_weights[i];
        if(weight >= currentWeight + new_truck && bridge_length >= currentCnt + 1) {
            q.push_front(new_truck);
            currentWeight += new_truck;
            currentCnt += 1;
        }
        // 넣을 수 없는 트럭이 없다면 다음 리터레이션에서 트럭을 넣을 수 있게 i를 증감한다.
        else {
            q.push_front(0);
            i -= 1;
        }

        answer += 1;
    }

    while(!q.empty())
    {
        q.pop_back();
        answer += 1;
    }

    
    return answer;
}