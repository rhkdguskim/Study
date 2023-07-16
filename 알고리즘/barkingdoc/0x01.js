// 문제1
// N 이하의 자연수 중에서 3의 배수이거나 5의 배수인 수를 모두 합한 값을 반환하는 함수 func1(int N)을 작성하여라 N은 10만 이하의 자연수이다.
// 시간복잡도 O(n)
function func1(num) {
    let x = 0;
    for(let i = 0; i<num; i++) {
        if(i % 3 == 0 || i % 5 == 0)
            x += i;
    }

    return x;
}

//console.log(func1(16));

// 문제2
// 주어진 길이 N의 int 배열 arr에서 합이 100인 서로 다른 위치의 두 원소가 존재하면 1을, 존재하지 않으면 0을 반환하는 함수 func2(int arr[], int n)를 작성하여라.
// arr의 각수는 0이상 100이하이고 N은 1000 이하이다.
// 시간복잡도 O(n^2)
function func2(arr, length) {
    for(let i=0; i<length; i++) {
        for(let j=i+1; j<length; j++) {
            if((arr[i] + arr[j]) === 100)
                return 1;
        }
    }
    return 0;
}

// console.log(func2([1,52,48],3));
// console.log(func2([50, 42],2));
// console.log(func2([4,13,63,87],4));

// 문제3
// N이 제곱수이면 1을 반환하고 제곱수가 아니면 0을 반환하는 함수 func3(int N)을 작성하여라. N은 10억 이하의 자연수이다.
// 시간복잡도 O(root N);
function func3(num) {
    const x = 0;
    for(let i=0; i<num; i++) {
        if(i*i >= num) {
            return ((i*i) === num);
        }
    }
}

//console.log(func3(756580036));

// 문제4
// N이하의 수 중에서 가장 큰 2의 거듭제곱수를 반환하는 함수 func4(int N)을 작성하라, N은 10억 이하의 자연수이다.
// 시간복잡도 O(lgN)
function func4(num) {
    for(let i=0; i<=num; i++) {
        const num2 = Math.pow(2,i);
        if(num <= num2) {
            return Math.pow(2,i-1);
        }
    }
}
//console.log(func4(97615282));