function niceCandidate(place, r, c) {
    place[r][c] = 'X';
    const rows = place.length;
    const cols = place[0].length;
    const moves = [[1, 0], [0, 1], [0, -1], [-1, 0]];
    let nextSteps = [[r, c]];
    
    
    for(let iter = 0; iter < 2; iter++){
        let q = [];
        while(nextSteps.length > 0) {
            [r, c] = nextSteps.shift();
            for(let i = 0; i < moves.length; i++) {
                const [dr, dc] = moves[i];
                const nr = r + dr; 
                const nc = c + dc;
                if (0 <= nr && nr < rows && 0 <= nc && nc < cols) {
                    if(place[nr][nc] === 'O') {
                        q.push([nr, nc]);
                        place[nr][nc] = 'X';
                    }
                    else if(place[nr][nc] === 'P') {
                        return false;
                    }
                }
            }    

        }
        nextSteps = q;
    }
    return true;
}

function isNiceDistribution(place) {
    const rows = place.length;
    const cols = place[0].length;

    for(let r = 0; r < rows; r++) {
        for(let c = 0; c < cols; c++) {
            if(place[r][c] === 'P') {
                if (!niceCandidate(place, r, c)) {
                    return false;
                }
            }
        }
    }   
    return true;
}

function solution(places) {
    const answer = [];
    for(let p = 0; p < places.length; p++) {
        let place = [];
        for(let r = 0; r < places[p].length; r++){
            place.push(places[p][r].split(''));
        }
        answer.push(+isNiceDistribution(place));
    }
    return answer;
}