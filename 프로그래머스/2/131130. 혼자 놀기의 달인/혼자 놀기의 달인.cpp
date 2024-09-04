// https://school.programmers.co.kr/learn/courses/30/lessons/131130
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// baseCase : 모두 상자가 열려있다면 게임이 종료된다.
// 1. 임의의 닫혀있는 상자에 접근한다. for loop
// 2. 상자에서 숫자를 꺼내고 숫자라 가르키는 상자로 이동한다.
// 3. 가르키는 상자가 열려있다면 종료 -> 1번으로 이동
    // box를 추가한다. 여기서 추가된 개수를 계산한다.
// 4. 가르키는 상자가 닫혀있다면 연다 -> 2번으로 이동
int dfs(vector<int>& cards, vector<bool>& v, vector<int>& boxs, int cur_card, int cnt, vector<vector<int>>& dp);

int solution(vector<int> cards) {
    int answer = 0;
    vector<int> boxs;
    vector<vector<int>> dp;
    dp.resize(cards.size(), vector<int>(cards.size(), -1));
    vector<bool> v(cards.size(), false);
    for (int i = 0; i < cards.size(); i++) {
        boxs.push_back(1);
        v[i] = true;
        answer = max(answer, dfs(cards, v, boxs, i, 1, dp));
        v[i] = false;
        boxs.pop_back();
    }
    return answer;
}

int dfs(vector<int>& cards, vector<bool>& v, vector<int>& boxs, int cur_card, int cnt, vector<vector<int>> &dp)
{
    int card_size = cards.size();
    // 상자가 모두 열려있는경우
    if (cnt == card_size) {
        // 박스가 하나인경우
        if (1 == boxs.size()) return 0;

        vector<int> temp = boxs;
        sort(temp.begin(), temp.end());

        int ans = 1;
        for (int i = 0; i < 2; i++) {
            ans *= temp.back();  temp.pop_back();
        }

        return ans;
    }

    if (dp[cur_card][cnt - 1] != -1) return dp[cur_card][cnt - 1];

    int max_v = 0;
    auto next = cards[cur_card] - 1;
    if (v[next]) {
        for (int i = 0; i < card_size; i++) {
            if (v[i]) continue;

            v[i] = true;
            boxs.push_back(1);
            dp[cur_card][cnt-1] = dfs(cards, v, boxs, i, cnt + 1, dp);
            max_v = max(max_v, dp[cur_card][cnt - 1]);
            boxs.pop_back();
            v[i] = false;
        }
    }
    else {
        boxs.back() += 1;
        v[next] = true;
        dp[cur_card][cnt - 1] = dfs(cards, v, boxs, next, cnt + 1, dp);
        max_v = max(max_v, dp[cur_card][cnt - 1]);
        v[next] = false;
        boxs.back() -= 1;
    }

    return max_v;

}