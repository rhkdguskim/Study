// 5x5 크기의 숫자판이 있다. 각각의 칸에는 숫자(0~9)까지 적혀있다. 이숫자판의 임의의 우치에서 시작해서,
// 인접해 있는 네 방향으로 다섯번 이동하면서, 각칸에 적혀있는 숫자를 차례대로 붙이면 6자리 수가 된다.
// 한번 거쳤던 칸을 다시 거쳐도 되며 0으로 시작하는 000123과 같은 수로 만들 수 있다.
// 숫자판이 주어졌을때, 서로 다른 여섯자리 수들의 개수를 구하는 프로그램을 구하시오.

const rows = 5; // 행의 개수
const cols = 5; // 열의 개수

const array2D = new Array(rows);

for(let i = 0; i< rows; i++) {
    array2D[i] = new Array(cols);
}

array2D[0][0] = 1;
array2D[0][1] = 1;
array2D[0][2] = 1;
array2D[0][3] = 1;
array2D[0][4] = 1;
array2D[1][0] = 1;
array2D[1][1] = 1;
array2D[1][2] = 1;
array2D[1][3] = 1;
array2D[1][4] = 1;
array2D[2][0] = 1;
array2D[2][1] = 1;
array2D[2][2] = 1;
array2D[2][3] = 1;
array2D[2][4] = 1;
array2D[3][0] = 1;
array2D[3][1] = 1;
array2D[3][2] = 1;
array2D[3][3] = 2;
array2D[3][4] = 1;
array2D[4][0] = 1;
array2D[4][1] = 1;
array2D[4][2] = 1;
array2D[4][3] = 1;
array2D[4][4] = 1;

function NumberJump(arr) {
    
}
