function solution(n) {
    const v = [];
    for (let i = 0; i < n; i++) {
        v[i] = new Array(n).fill(false);
    }

    function check(row, col) {
        let left = col - 1;
        let right = col + 1;

        for (let i = row - 1; i >= 0; i--) {
            if (v[i][col]) return false;  // 같은 열 검사
            if (left >= 0 && v[i][left]) return false;  // 왼쪽 대각선 검사
            if (right < n && v[i][right]) return false;  // 오른쪽 대각선 검사
            left--;
            right++;
        }

        return true;
    }

    function backtracking(row) {
        if (row == n) {
            return 1;
        }

        let sum = 0;
        for (let col = 0; col < n; col++) {
            if (check(row, col)) {
                v[row][col] = true;
                sum += backtracking(row + 1);
                v[row][col] = false;
            }
        }

        return sum;
    }

    return backtracking(0);
}
