function solution(maps) {
    let answer = 0;
    const nextStep = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    let queue = [[1, 1]];
    let nextQueue = []
    const rows = maps.length;
    const cols = maps[0].length;
    let x, y, nx, ny;
    
    maps[0][0] = 0;
    while(queue.length !== 0){
        answer += 1;
        while(queue.length !== 0){
            [x, y] = queue.pop();
            for([dx, dy] of nextStep){
                nx = x + dx;
                ny = y + dy;
                if(0 < nx && nx <= cols && 0 < ny && ny <= rows){
                    if(maps[ny-1][nx-1] === 0){
                        continue;
                    }
                    if(nx === cols && ny === rows){
                        return answer + 1;
                    }
                    maps[ny-1][nx-1] = 0;
                    nextQueue.push([nx, ny]);
                }        
            }
        }
        queue = nextQueue;
        nextQueue = [];
    }
    return -1;
}