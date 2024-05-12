# https://school.programmers.co.kr/learn/courses/30/lessons/68936
def solution(arr):
    move = [(0, 0), (0, 1), (1, 0), (1, 1)]
    def answer(i, j, size):
        if size == 2:
            v = arr[i][j]
            if arr[i+1][j] == v and arr[i][j+1] == v and arr[i+1][j+1] == v:
                if v == 0:
                    return [1, 0]
                else:
                    return [0, 1]
            else:
                black, white = 0, 0
                for c in range(4):
                    ny, nx = i + move[c][0], j + move[c][1]
                    if arr[ny][nx]:
                        white += 1
                    else:
                        black += 1
                return [black, white]
        
        new_size = size // 2
        result = [0, 0]
        for m in range(4):
            ny, nx = i + move[m][0]*new_size, j + move[m][1]*new_size
            temp = answer(ny, nx, new_size)
            result[0] += temp[0]
            result[1] += temp[1]
        
        if result[0] == 4 and result[1] == 0:
            return [1, 0]
        elif result[1] == 4 and result[0] == 0:
            return [0, 1]
        else:
            return result
    
    return answer(0, 0, len(arr))

