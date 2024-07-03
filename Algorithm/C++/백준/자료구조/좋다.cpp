// https://www.acmicpc.net/problem/1253
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int N;
    cin >> N;
    vector<long long> nums(N);

    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    sort(nums.begin(), nums.end());
    
    int answer = 0;

    for (int i = 0; i < N; i++) {
        int left = 0, right = N - 1;
        while (left < right) {
            if (left == i) {
                left++;
                continue;
            }
            if (right == i) {
                right--;
                continue;
            }
            if (nums[left] + nums[right] == nums[i]) {
                answer++;
                break;
            } else if (nums[left] + nums[right] < nums[i]) {
                left++;
            } else {
                right--;
            }
        }
    }
    
    cout << answer << '\n';

    return 0;
}
