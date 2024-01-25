from collections import deque
def makeGraph(rectangle):
    x, y = 0, 0
    graph = []
    leftX, leftY, rightX, rightY = 60, 60, 0, 0
    for a, b, c, d in rectangle:
        leftX = min(a, leftX)
        leftY = min(b, leftY)
        rightX = max(c, rightX)
        rightY = max(d, rightY)
    # print(leftX, leftY, rightX, rightY, "leftX, leftY, rightX, rightY")
    x = rightX - leftX
    y = rightY - leftY
    
    graph = [[0] * (x+1) for _ in range(y+1)]
    
#   직사각형 하나씩 만들어서 1 값 넣어주기
    for a, b, c, d in rectangle:
        for i in range(d-b+1):
            for j in range(c-a+1):
                graph[i+leftY-b][j+leftX-a] = 1
    
    return graph

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
#     모든 경우의 수를 지닌 2차원 배열 초기화
    field = [[-1] * 102 for i in range(102)]
    
#     (1) 직사각형 만든다 테두리부분만 1로 
    for r in rectangle:
        # 모든 좌표값 2배 -> ㄷ 자 일때 ㅁ으로 보여질 수 있어서
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 현재 직사각형의 테두리일 때.
                # for문이 현재의 직사각형 내부에서 도니까
                elif field[i][j] != 0:
                    field[i][j] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[1] * 102 for i in range(102)] # 아직 방문하지 않은 곳은 1로 표시
    visited[characterX * 2][characterY * 2] = 0 # 시작 지점은 0으로 초기화
    
    while q:
        x, y = q.popleft()
        # 도착한 곳이 아이템이 있는 장소라면 현재의 최단거리(나누기 2)를 answer로 하고 while문을 빠져나옴
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
            # break는 가까운 반복문을 하나만 ㅃㅏ져나온다.
        # 아니라면 상하좌우를 탐색
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            # 현재 좌표가 테두리이고 아직 방문하지 않은 곳이라면 q에 추가 후 visited를 최단거리로 갱신
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
            
    #   먼저 2차원으로 큰 직사각형 만들기
    # graph = makeGraph(rectangle)

    
    
    return answer