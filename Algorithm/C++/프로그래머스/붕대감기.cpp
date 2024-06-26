// https://school.programmers.co.kr/learn/courses/30/lessons/250137
#include <string>
#include <vector>

// t초 동안 붕대를 감으면 1초마다 x만큼 체력을 회복
// t초 연속으로 붕대를 감는데 성공하면 y만큼 체력을 추가 회복
// 최대 채력보다 커지는 것은 불가능
using namespace std;

int solution(vector<int> bandage, int health, vector<vector<int>> attacks) {
    int t = bandage[0];
    int x = bandage[1];
    int y = bandage[2];
    auto attack_idx = 0;
    auto time = 0;
    auto recover_cnt = 0;
    int max_health = health;

    while(attacks.size() > attack_idx) {
        auto attacked_time = attacks[attack_idx][0];
        auto damage = attacks[attack_idx][1];

        // 공격을 받는 경우라면 health가 감소하고, revocer_cnt를 0으로 만든다.
        if (time == attacked_time) {
            health -= damage;
            recover_cnt = 0;
            attack_idx += 1;

            // health가 0보다 작거나 같다면 게임을 종료한다.
            if(0 >= health)
                return -1;
            
        } else {
            recover_cnt += 1;
            health += x;

            // 만약 recover_cnt가 t와 같아진다면 추가 회복을 한다.
            if(recover_cnt == t) {
                health += y;
                recover_cnt = 0;
            }

            // 최대 체력보다 커지는 것은 불가능
            health = min(health, max_health);
        }

        time += 1;
    }

    return health;
}