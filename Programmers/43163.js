function calcDiff(str1, str2) {
    return str1.split('').filter((letter, index) => {
        return letter !== str2[index];
    }).length;
}

function makeGraph(words) {
    const graph = {};
    words.forEach(word => {graph[word] = []})
    for(let i = 0; i < words.length - 1; i++) {
        for (let j = i+1; j < words.length; j++) {
            if (calcDiff(words[i], words[j]) === 1) {
                graph[words[i]].push(words[j]);
                graph[words[j]].push(words[i]);
            }
        }
    }
    return graph;
}

function solution(begin, target, words) {
    const graph = makeGraph(words);
    const visited = {};
    let q = words.filter(word => {
        visited[word] = false;
        return calcDiff(word, begin) === 1;  
    });
    
    q.forEach(word => {
        visited[word] = true;
    });
    
    let count = 0;
    while (q.length > 0) {
        count += 1;
        let nextQ = new Set();
        for(let i = 0; i < q.length; i++) {
            const curr = q[i];
            if(curr === target) {
                return count;
            }
                
            for(let neighbor of graph[curr]) {
                if(visited[neighbor]){
                   continue; 
                }
                visited[neighbor] = true;
                nextQ.add(neighbor);
            }        
        }
        q = [...nextQ];
    }
    return 0;
}