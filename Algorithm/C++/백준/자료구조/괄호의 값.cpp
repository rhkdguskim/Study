#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    string operation;
    cin >> operation;

    stack<char> stk;
    int result = 0;
    int temp = 1;

    for (int i = 0; i < operation.size(); ++i) {
        char op = operation[i];
        if (op == '(') {
            stk.push(op);
            temp *= 2;
        } else if (op == '[') {
            stk.push(op);
            temp *= 3;
        } else {
            if (stk.empty() || (op == ')' && stk.top() != '(') || (op == ']' && stk.top() != '[')) {
                cout << 0;
                return 0;
            }
            if (op == ')') {
                if (operation[i - 1] == '(') {
                    result += temp;
                }
                temp /= 2;
            } else if (op == ']') {
                if (operation[i - 1] == '[') {
                    result += temp;
                }
                temp /= 3;
            }
            stk.pop();
        }
    }

    if (!stk.empty()) {
        cout << 0;
    } else {
        cout << result;
    }

    return 0;
}
