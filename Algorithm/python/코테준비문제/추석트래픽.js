// 2016-09-15 03:10:33.020 0.011s
// -> 2016-09-15 03:10:33.010 ~ 2016-09-15 03:10:33.020
// 소수점 셋재 짜리 까지

// 합 배열 문제로 해결
// 시간복잡도 O(1000 * 1000)

// ms로 가중치 기준을 잡는다.
// 가중치
// 1시간 : 360000, 분 : 6000, 1초 : 1000

lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
    ]

function solution(lines) {
    startTime = Array() // 시작시간
    endTime = Array(); // 종료시간
    traffics = Array(lines.length).fill(1); // 최대 트래픽을 저장할 배열

    lines.map(element => { // O(N)

        // 가중치를 계산한다.
        element = element.split(" ")
        const time = element[1].split(":")

        const hour = Number(time[0]) * 1000 * 60 * 60
        const min = Number(time[1]) * 1000 * 60
        const temp = time[2].split(".")

        const sec = Number(temp[0]) * 1000
        const msec = Number(temp[1])

        const duration = Number(element[2].replace("s", "")) * 1000

        const sumTime = hour + min + sec + msec
        startTime.push(sumTime - duration + 1)
        endTime.push(sumTime + 1000) // 1초간의 간격 가중치 추가
    });

    for(let i =0; i < lines.length; i++) { // O(N^2)
        for(let j =i-1; j >= 0; j-- ) {
            if ( endTime[j] > startTime[i] ) { // 겹치는 구간이 생긴다면
                traffics[j] += 1 // 합배열에 가중치를 더한다.
            }
        }
    }
    console.log(startTime) // StartTime
    console.log(endTime) // EndTime
    const answer = traffics.reduce((max, current) => { // O(N)
        return Math.max(max, current)
    })
    return answer
}

console.log(solution(lines))
