// https://school.programmers.co.kr/learn/courses/30/lessons/42895
N = 5
number = 12

function solution(N, number) {
    let dp = new Array(32000+1).fill(9);
    let queue = []
    
    let multi = 1
    let num = N
    let count = 1
    while (32001 > num) {
        queue.push([num, count])
        const str = String(num) + String(N)
        count += 1
        num = Number(str)
    }

    while (32001 > Math.pow(N, multi)) {
        queue.push([Math.pow(N, multi), multi]);
        multi += 1;
    }

    while (queue.length) {
        const [now, value] = queue.shift()
        if (Number.isInteger(now) && now < 320001 && now > 0 && dp[now] > value) { // 작을 경우만 queue에 삽입 
            dp[now] = value
            queue.push([now+1, value+2])
            queue.push([now-1, value+2])
            queue.push([now+N, value+1])
            queue.push([now-N, value+1])
            queue.push([now*N, value+1])
            queue.push([now/N, value+1])
        }
    }
    console.log(dp[number])
    if (dp[number] > 8)
        return -1
    else
        return dp[number]
}
  

solution(N,number)