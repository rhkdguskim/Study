#include <iostream>
#include <vector>
#include <tuple>
#include <unordered_set>

namespace std {
    template<> struct hash<tuple<int, int>> {
        size_t operator()(const tuple<int, int>& t) const {
            auto [x, y] = t;
            return hash<int>()(x) ^ hash<int>()(y);
        }
    };
}

using namespace std;
constexpr int EMPTY = 0;
constexpr int HOUSE = 1;
constexpr int CHICKEN = 2;
vector<tuple<int, int>> house;
vector<tuple<int, int>> chicken;
vector<vector<int>> graph;
int n, m;

int get_distance(tuple<int, int> &house, tuple<int ,int> &chicken)
{
    return abs(get<0>(house) - get<0>(chicken)) + abs(get<1>(house) - get<1>(chicken));
}

int combination(unordered_set<tuple<int, int>> &not_chicken, int idx)
{
    if(m >= chicken.size() - not_chicken.size())
    {
        // 치긴거리 구하기.
        int total_distance = 0;
        for(auto h : house)
        {
            int min_distance = 2*n;
            for(auto c : chicken)
            {
                if(not_chicken.find(c) == not_chicken.end())
                {
                    min_distance = min(min_distance, get_distance(h, c));
                }
            }
            total_distance += min_distance;
        }

        // 도시의 치킨거리 리턴
        return total_distance;
    }

    int result = 987654321;

    for(int i = idx; i < chicken.size(); i ++)
    {
        not_chicken.insert(chicken[i]);
        result = min(result, combination(not_chicken, i + 1));
        not_chicken.erase(chicken[i]);
    }

    return result;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n >> m;
    
    int temp;

    for(int i = 0; i < n; i ++)
    {
        for(int j = 0; j < n; j ++)
        {
            cin >> temp;
            if(temp == CHICKEN)
            {
                chicken.push_back({i, j});
            }
            else if(temp == HOUSE)
            {
                house.push_back({i, j});
            }
        }
    }

    unordered_set<tuple<int, int>> not_chicken;

    cout << combination(not_chicken, 0);
}

