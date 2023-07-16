// 테이블 해시 함수
let data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]

// 테이블의 튜플을 col번째 컬럼 값을 기준으로 오름차순 정렬 (버블정렬)
function bubbleSort(data, col) {
    const mycol = col - 1;
    for(i = 0; i < data.length; i++) {
        for(j=0; j < data.length - 1 - i; j++) {
            if(data[j][mycol] > data[j + 1][mycol]) {
                [data[j], data[j +1]] = swap(data[j], data[j +1]);
            }
        }
    }
    return data;
}

// 기본키인 첫번째 컬럼 값을 기준으로 내림차순 정렬
function checkSameValue(data, col) {
    const mycol = col - 1;
    for(i = 0; i < data.length; i++) {
        for(j=i+1; j < data.length; j++) {
            if(data[i][mycol] == data[j][mycol]) {
                if(data[i][0] < data[j][0])
                    [data[i], data[j]] = swap(data[i], data[j]);
            }
        }
    }
    return data;
}

// i번째 행위 튜플에대해 컬럼값을 i로 나눈 나머지들의 합
function devidebyi(data) {
    let newarr = []
    for(i = 0; i< data.length; i++) {
        let newdata = 0;
        for(j = 0; j<data[i].length; j++) {
            newdata +=  data[i][j] % (i+1);
        }
        newarr.push(newdata)
    }
    return newarr;
}

// arr sawp
function swap(data1, data2) {
    const temp = data1;
    data1 = data2;
    data2 = temp;
    return [data1, data2]; 
}


function solution(data, col, row_begin, row_end) {
    const newdata = checkSameValue(bubbleSort(data, col), col);
    const newdata2 = devidebyi(newdata);
    const begin = row_begin - 1;
    const end = row_end - 1;
    let result = newdata2[begin]; // 첫데이터는 연산하기위하여 대입
    for(i=begin+1; i <= end; i++) {
        result ^= newdata2[i];
    }
    return result;
}