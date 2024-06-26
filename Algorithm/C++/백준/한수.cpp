// https://www.acmicpc.net/problem/1316
#include <iostream>
#include <string>
using namespace std;

bool check(string num)
{
    bool ret = true;

    // 만약 3자리보다 작다면 무조건 한수이다.
    if(3 > num.size())
        return ret;

    int num1 = stoi(num.substr(0, 1));
    int num2 = stoi(num.substr(1, 1));
    int num3 = stoi(num.substr(2, 1));

    if(num1 - num2 != num2 - num3)
        ret = false;
    
    return ret;
}

int main()
{
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
    int n;
    int cnt = 0;

    cin >> n;

    for(int i{1}; i <= n; i++)
    {
        if(check(to_string(i)))
            cnt += 1;
    }

    cout << cnt;
}