// https://www.acmicpc.net/problem/1256

#include <iostream>
#include <vector>
#include <string>

// N개의 a와 M개의 z가 이루어져 있다.
// K번째 문자열이 무엇인지 구하시오.
using namespace std;
// aazz 16개의 문자가 존재.
// zz
void dfs(int a_cnt, int z_cnt, string word);
int N, M, K, total;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> N >> M >> K;

    dfs(0, 0, "");
}

void dfs(int a_cnt, int z_cnt, string word)
{
    if(a_cnt == N && z_cnt == M)
    {
        total += 1;
        cout << total << ' ' << word;
        return;
    }

    if(N > a_cnt)
    {
        dfs(a_cnt + 1, z_cnt, word + 'a');
    }

    if(M > z_cnt)
    {
        dfs(a_cnt, z_cnt + 1, word + 'z');
    }

}