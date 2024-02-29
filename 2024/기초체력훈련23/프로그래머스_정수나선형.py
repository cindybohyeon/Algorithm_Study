def solution(n):
    def in_range(x, y):
        if x >= 0 and x < n and y >= 0 and y < n:
            return True
        return False
        
    answer = [[0 for _ in range(n)] for _ in range(n)]
    turn = 0
    cnt = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    idx, idy = 0, 0
    direct = 0
    while(turn < n*n):
        # if turn == 16:
        #     break
        # 아직 들어가지 않은 경우
        if answer[idx][idy] == 0: # 0, 3
            answer[idx][idy] = cnt
            cnt += 1
            # 이동 가야하는 것 => 4가지 방향에서 1개로
            # 이걸 어떻게 판단할 수? => 값이 그래프 벗어났거나, 값이 0이 아닌 경우            
            nextX = idx + dx[direct]
            nextY = idy + dy[direct]
            if in_range(nextX, nextY) == False or answer[nextX][nextY] != 0:
                # 위치 변경
                if direct == 3:
                    direct = 0
                else:
                    direct += 1                
            idx += dx[direct]
            idy += dy[direct]
            turn += 1
    return answer