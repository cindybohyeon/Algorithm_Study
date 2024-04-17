function solution(maps) {
    if (!maps) {
        return 1
    }
    var answer = 0;
    let mxLen = maps.length
    let myLen = maps[0].length
    
    // 상대 팀을 파괴하는 것 => 상대 팀으로 빨리 도착해야한다.
    let visited = Array(mxLen).fill(0)
    for (let i = 0; i< mxLen; i++) {
        visited[i] = Array(myLen).fill(0)
    }
    // 1인 값만 이동가능한 곳.
    let dx = [1,0,-1,0];
    let dy = [0,1,0,-1];
    
    // queue를 만들어야한다..
    let q = []
    q.push([0, 0])
    visited[0][0] = 1
    while (q.length != 0) {
        var [x, y] = q.shift()
        for (var i = 0; i< 4; i++) {
            let nx = x + dx[i]
            let ny = y + dy[i]
            if (0 <= nx && nx < mxLen && 0 <= ny && ny < myLen) {
                if (visited[nx][ny] == 0 && maps[nx][ny] == 1) {
                    q.push([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                }                
            }

        }
    }
    if (visited[mxLen-1][myLen-1] == 0) {
        answer = -1
    }
    else {
        answer = visited[mxLen-1][myLen-1]
    }
    
    return answer;
}

function solution2(maps) {
    // 1. 남동북서 기준
    const dy = [1,0,-1,0];
    const dx = [0,1,0,-1];
    const row = maps.length;
    const col = maps[0].length;

    // 2.
    const visitCount = [...maps].map((r) => r.map((c) => 1));

    // 3.
    const queue = [[0,0]];  //시작점

    // 4.
    while(queue.length) {
        const [y, x] = queue.shift();

        // 5.
        for(let i = 0; i < 4; i++ ) {
            const ny = y + dy[i];
            const nx = x + dx[i];

            // 6.
            if(ny >= 0 && nx >= 0 && ny < row && nx < col) {
                // 7.
                if(maps[ny][nx] === 1 && visitCount[ny][nx] === 1) {
                    visitCount[ny][nx] = visitCount[y][x] + 1;
                    queue.push([ny,nx]);
                }
            }
        }
    }

    return visitCount[row - 1][col - 1] === 1 ? -1 : visitCount[row - 1][col - 1];    
}