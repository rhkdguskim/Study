#include <string>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    set<int> my_lottos;
    int zero_cnt {0};

    for(const auto& l : lottos) {
        if(l == 0) 
            zero_cnt += 1;
        else 
            my_lottos.insert(l);
    }

    set<int> win;
    for(auto w : win_nums) {
        win.insert(w);
    }

    int rank = 7;
    for(const auto&l : my_lottos) {
        if(win.find(l) != win.end())
            rank -= 1;
    }

    vector<int> answer;
    answer.push_back(min(rank - zero_cnt, 6)); // 무조건 맞춤
    answer.push_back(min(rank, 6)); // 무조건 틀림
    return answer;
}