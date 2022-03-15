const keyTable = {
    1: 'L',
    2: '',
    3: 'R',
    4: 'L',
    5: '',
    6: 'R',
    7: 'L',
    8: '',
    9: 'R',
    0: '',
}
const history = {
    'L': [0, 0],
    'R': [0, 2],
}
const coordinateTable = {
    1: [3, 0],
    2: [3, 1],
    3: [3, 2],
    4: [2, 0],
    5: [2, 1],
    6: [2, 2],
    7: [1, 0],
    8: [1, 1],
    9: [1, 2],
    0: [0, 1],
}

function calcNearest(num, defaultDirection) {
    const vector1 = history['L'];
    const vector2 = history['R'];
    const vector3 = coordinateTable[num];
    const dist1 = calcDist(vector1, vector3);
    const dist2 = calcDist(vector2, vector3);
    return dist1 === dist2 ? defaultDirection : dist1 < dist2 ? 'L' : 'R';
}

function calcDist(vector1, vector2) {
    return vector1.reduce((prev, curr, index) => {
        return prev + Math.abs(curr - vector2[index]) 
    }, 0)
}

function solution(numbers, hand) {
    var answer = '';    
    let direction;
    const defaultDirection = hand[0].toUpperCase();
    for(let i = 0; i < numbers.length; i++){
        direction = keyTable[numbers[i]];
        if(direction === '') {
            direction = calcNearest(numbers[i], defaultDirection);
        }
        answer += direction;
        history[direction] = coordinateTable[numbers[i]];   
    }
    return answer;
}