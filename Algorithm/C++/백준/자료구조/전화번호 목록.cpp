// https://www.acmicpc.net/problem/5052
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
int t, n;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> t;
    for(int i = 0; i < t; i ++) {
        cin >> n;
        vector<string> phonenumbers;
        for(int j = 0; j < n; j ++) {
            string temp;
            cin >> temp;
            phonenumbers.push_back(temp);
        }


        // 문자열 정렬
        sort(phonenumbers.begin(), phonenumbers.end());

        bool flag = true;
        for(int i = 0; i < n-1; i ++) {
            int size = phonenumbers[i].size();
            auto next_phone = phonenumbers[i+1].substr(0, size);
            if(next_phone == phonenumbers[i]) {
                cout << "NO\n";
                flag = false;
                break;
            }
        }
        
        if(flag) cout << "YES\n";

    }
    
    
}