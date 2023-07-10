// https://school.programmers.co.kr/learn/courses/30/lessons/43162
n = 2
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
function solution(n, computers) {
    const arr = new Array(n+1);
    const ParentSet = new Set()
    for (let i = 1; i <= n; i++) {
        arr[i] = i;
    }
    console.log(arr)
    for (i =0; i<computers.length; i++)
    {
        for (j =0; j<computers[i].length; j++)
        {
            if (computers[i][j] == 1)
            {
                union(arr,i+1,j+1)
            }
        }
    }
    for (let i = 1; i <= n; i++) {
        ParentSet.add(getParent(arr, i))
    }
    console.log(ParentSet.size)
    return ParentSet.size;
}

 function getParent(arr, n) {
    if (arr[n] === n) return n;
  
    return (arr[n] = getParent(arr, arr[n]));
  }
  
  function union(arr, a, b) {
    a = getParent(arr, a);
    b = getParent(arr, b);
  
    if (a < b) arr[b] = a;
    else arr[a] = b;
  }
  
solution(n,computers)