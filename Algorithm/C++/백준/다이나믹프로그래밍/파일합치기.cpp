#include <iostream>
#include <vector>
#include <string>

using namespace std;
int T, K;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    cin >> T;

    for(int i = 0; i < T; i++)
    {
        cin >> K;
        vector<int> dp(K);
        vector<int> file(K);

        for(int j = 0; j < K; j++) cin >> file[j];

        dp[0] = file[0];
        dp[1] = file[0] + file[1];

        for(int k = 2; k < K; k++)
        {
            dp[k] = max(dp[k-1] + file[k], dp[k-2] + file[k-1] + file[k]);
        }

        cout << dp[K-1];
    }
}