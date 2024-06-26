// https://school.programmers.co.kr/learn/courses/30/lessons/250135
#include <string>
#include <vector>
#include <iostream>
using namespace std;
// 시 : h = h / 3600 분 : m = m / 60, s = 1
// 1초씩 흘려보내면서 초가 시간과 분을 겹치거나 넘어가는 시점을 카운팅한다.

double filter(double v)
{
    if(v >= 60) {
        return v-60;
    }
}

double cnt_h(double h)
{
    return h + (1 / 3600.0);
}

double cnt_m(double m)
{
    return m + (1 / 60.0);
}

double cnt_s(double s)
{
    return s+1;
}


int solution(int h1, int m1, int s1, int h2, int m2, int s2) {

    int start_time = h1*3600 + m1*60 + s1;
    int end_time = h2*3600 + m2*60 + s2;
    int answer = 0;

    if(h1 >= 12)
    {
        h1 -= 12;
    }

    double prev_h = h1 * 5;
    double prev_m = m1;
    double prev_s = s1;

    bool h_flag = false;
    bool m_flag = false;

    if(prev_h == prev_s || prev_m == prev_s)
    {
        if(prev_h == prev_s) {
            h_flag = true;
        }
        if(prev_m == prev_s) {
            m_flag = true;
        }
        answer += 1;
    }

    for(int i{1}; i <= end_time - start_time; i++)
    {

        int cur_h = cnt_h(prev_h);
        int cur_m = cnt_m(prev_m);
        int cur_s = cnt_s(prev_s);

        bool cnt_flag = false;

        if(cur_s == 60)
        {
            m_flag = false;
            h_flag = false;
        }

        if(cur_h >= prev_s && !h_flag)
        {
            h_flag = true;
            cnt_flag = true;
        }

        if(cur_m >= prev_s && !m_flag)
        {
            m_flag = true;
            cnt_flag = true;
        }

        if(cnt_flag)
        {
            answer += 1;
            cout << cur_h << cur_m << prev_s << endl;
        }
            

        prev_h = filter(cur_h);
        prev_m = filter(cur_m);
        prev_s = filter(cur_s);
    }

    
    return answer;
}