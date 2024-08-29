#include <string>
#include <vector>
#include <iostream>

using namespace std;

void dfs(int idx, int n, const vector<int> &apich, vector<int> &lion, vector<int> &answer, int &maxDiff);

vector<int> solution(int n, vector<int> info) {
    vector<int> answer(11, -1);
    vector<int> lion(11, 0);
    int maxDiff = 0;
    dfs(0, n, info, lion, answer, maxDiff);

    if(answer[0] == -1) return { -1 };
    return answer;
}

void dfs(int idx, int n, const vector<int> &apich, vector<int> &lion, vector<int> &answer, int &maxDiff) {
    if(idx == 10) {
        lion[10] = n;
        int lionScore = 0, apichScore = 0;
        
        for(int i = 0; i < 11; ++i) {
            if(lion[i] > apich[i]) lionScore += 10 - i;
            else if(apich[i] != 0) apichScore += 10 - i;
        }
        
        int diff = lionScore - apichScore;
        
        if(diff > maxDiff) {
            maxDiff = diff;
            answer = lion;
        } else if(diff == maxDiff && diff != 0) {
            for(int i = 10; i >= 0; --i) {
                // 낮은 점수를 더 많이 맞춘경우
                if(lion[i] > answer[i]) {
                    answer = lion;
                    break;
                } else if(lion[i] < answer[i]) {
                    break;
                }
            }
        }
        return;
    }

    // 라이언이 이긴 경우
    if(n >= apich[idx] + 1) {
        lion[idx] = apich[idx] + 1;
        dfs(idx + 1, n - (apich[idx] + 1), apich, lion, answer, maxDiff);
        lion[idx] = 0;
    }

    // 라이언이 진 경우
    dfs(idx + 1, n, apich, lion, answer, maxDiff);
}
