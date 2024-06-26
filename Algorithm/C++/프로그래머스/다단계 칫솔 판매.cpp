// https://school.programmers.co.kr/learn/courses/30/lessons/77486
#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

void go(map<string, int> &key, map<string, string> &graph, string current, int cost)
{  
    // Base Case
    if(cost == 0 || current == "-") return;

    // Logic
    int next_cost = cost / 10;
    int my_cost = cost - next_cost;

    key[current] += my_cost;

    // Next
    go(key, graph, graph[current], next_cost);
}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    map<string, string> graph;
    map<string, int> key;
    size_t n = enroll.size();

    for(int i{0}; i < n; i ++)
    {
        graph[enroll[i]] = referral[i];
        key[enroll[i]] = 0;
    }

    vector<int> answer;
    answer.resize(n, 0);

    size_t m = seller.size();
    
    for(int i{0}; i < m; i ++) 
    {
        go(key, graph, seller[i], amount[i]*100);
    }

    for(int i{0}; i < n; i ++) 
    {
        answer[i] = key[enroll[i]];
    }

    return answer;
}