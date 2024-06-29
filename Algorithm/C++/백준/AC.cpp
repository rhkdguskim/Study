#include <iostream>
#include <sstream>
#include <string>
#include <deque>

int T;

using namespace std;
int main()
{
    cin >> T;
    for(int i = 0; i < T; i ++)
    {
        string p;
        
        int n;
        cin >> p;
        cin >> n;

        string x;
        cin >> x;

        if (!x.empty()) {
            x.erase(0, 1);
        }
        if (!x.empty()) {
            x.erase(x.size() - 1, 1);
        }

        istringstream stream(x);
        string t;
        deque<int> q;
        while(!x.empty() && getline(stream, t, ','))
        {
            if(!t.empty())
                q.push_back(stoi(t));
        }

        bool reversed = false;
        bool is_error = false;
        for(auto op :p)
        {
            if(op == 'D') {
                if(q.empty()) {
                    cout << "error\n";
                    is_error = true;
                    break;
                }
                
                if(reversed) {
                    q.pop_back();
                }
                else {
                    q.pop_front();
                }
            }
            else {
                reversed = !reversed;
            }
        }
        if(!is_error) {
            cout << "[";
            if(!q.empty()) {
                if(reversed) {
                    auto it = q.rbegin();
                    cout << *it++;

                    while(it != q.rend()) {
                        cout << ',' << *it++;
                    }
                }
                else {
                    auto it = q.begin();
                    cout << *it++;

                    while(it != q.end()) {
                        cout << ',' << *it++;
                    }
                }
            }
            cout << "]\n";
        }
    }
}