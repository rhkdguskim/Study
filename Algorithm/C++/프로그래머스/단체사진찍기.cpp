#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;
typedef std::unordered_map<char, std::unordered_map<char, std::vector<std::pair<char, int>>>> ConditionMap;
string friends = "ACFJMNRT";

bool check(const string& row, char next, ConditionMap &map)
{
    auto length = row.length();
    // 이전에 있던 row들이 현재 next와 부합하는지 확인한다.
    for(int i = 0; i < length; i++) {
        for(auto [oper, v] : map[row[i]][next]) {
            auto distance = length - i - 1;
            switch(oper)
            {
                case '=':
                    if(v != distance) {
                        return false;
                    }
                    break;
                // 커야한다.
                case '>':
                    if(v >= distance) {
                        return false;
                    }
                    break;
                // 작아야한다.
                case '<':
                    if(v <= distance) {
                        return false;
                    }
                    break;
            }
        }

    }

    return true;
}

int dfs(string &row, ConditionMap &map)
{
    if(row.length() == 8) {
        //cout << row << "\n";
        return 1;
    }

    int cnt = 0;
    for(int i = 0; i < 8; i ++) 
    {    
        auto next = friends[i];
        // 이미 존재하는 경우 놓을 수 없음
        if(string::npos != row.find(next)) continue;

        // 조건이 맞지않을경우 무시
        if(!check(row, next, map)) continue;

        row.push_back(next);
        cnt += dfs(row, map);
        row.pop_back();
    }

    return cnt;
}
// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, vector<string> data) {
    ConditionMap map;
    for(auto temp : data) {
        char first = temp.at(0);
        char second = temp.at(2);

        char comp = temp.at(3);
        int  comp2 = temp.at(4) - '0';

        map[first][second].push_back({comp, comp2});
        map[second][first].push_back({comp, comp2});
    }

    string a = "";
    int answer = dfs(a, map);
    return answer;
}