#include <iostream>
#include <string>
#include <stack>
using namespace std;

// 연산자 우선순위
int getPrecedence(char op) {
    if (op == '(' || op == ')')
        return 0;
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return -1;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    string operation;
    cin >> operation;

    string answer;
    stack<char> op;

    for(int i = 0; i < operation.size(); i ++) {
        char t = operation[i];
        if (t >= 'A' && t <= 'Z') {
            answer.push_back(t); // 알파벳인 경우 바로 출력
        }
        else if (t == '(') {
            op.push(t); // 여는 괄호는 스택에 넣는다
        }
        else if (t == ')') {
            while (!op.empty() && op.top() != '(') {
                answer.push_back(op.top()); // 여는 괄호를 만날 때까지 모든 연산자를 출력
                op.pop();
            }
            op.pop(); // 여는 괄호 제거
        }
        else {
            // 연산자인 경우
            while (!op.empty() && getPrecedence(op.top()) >= getPrecedence(t)) {
                answer.push_back(op.top());
                op.pop();
            }
            op.push(t);
        }
    }

    // 스택에 남은 모든 연산자를 출력
    while (!op.empty()) {
        answer.push_back(op.top());
        op.pop();
    }

    cout << answer << endl;
    return 0;
}
