// https://school.programmers.co.kr/learn/courses/30/lessons/169198?language=cpp

#include <string>
#include <vector>
#include <cmath>
#include <iostream>
using namespace std;

// 1. 당구의 위치, 맞춰야할 공위치의 중간 점을 구한다. ( 가로의 길이를 구한다. )
// 2. 중간점으로부터 (-1 , -1) 혹은 (+1, +1 )을 해가면서 가장 가까운 높이를 구한다.
// 3. 정답 =  ((가로^2 + 높이^2) ^ 0.5 * 2)^2
// 가로의 길이를 알게된다.

int get_width(int src_x, int src_y, int dst_x, int dst_y)
{
    return sqrt(pow(src_x - dst_x, 2) + pow(src_y - dst_y, 2)) / 2;
}

int get_height(int mid_x, int mid_y, int m, int n) 
{
    int top = mid_y;
    int bottom = n - mid_y;
    int left = mid_x;
    int right = m - mid_x;

    return min(min(min(top, bottom), left), right);
}

pair<int, int> get_mid_pos(int src_x, int src_y, int dst_x, int dst_y)
{
    return {(src_x + dst_x)/2, (src_y + dst_y)/2};
}

int get_length(int w, int h)
{
    // ((가로^2 + 높이^2) ^ 0.5 * 2)^2
    return pow(sqrt(pow(w, 2) + pow(h, 2)) * 2, 2);
}

vector<int> solution(int m, int n, int startX, int startY, vector<vector<int>> balls) {
    vector<int> answer;

    for(const auto ball : balls)
    {
        auto dst_x = ball[0];
        auto dst_y = ball[1];

        auto w = get_width(startX, startY, dst_x, dst_y);
        auto mid = get_mid_pos(startX, startY, dst_x, dst_y);
        auto h = get_height(mid.first, mid.second, m, n);
        auto v = get_length(w, h);

        // cout << w << " "<< h <<  " " << v << "\n";
        answer.push_back(v);
    }

    return answer;
}