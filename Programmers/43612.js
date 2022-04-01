class UnionFind {
    constructor(n) {
        this.parent = {};
        for(let i = 1; i <= n; i++) {
            this.parent[i] = i;
        }
        this.groups = n;
    }
    
    union(node1, node2) {
        node1 = this.find(node1);
        node2 = this.find(node2);
    
        if(node1 !== node2) {
            this.parent[node1] = node2;
            this.groups -= 1;
        }
        
    }
    
    find(node) {
        if (this.parent[node] !== node){
            this.parent[node] = this.find(this.parent[node]);
        }
        return this.parent[node] ;
    }
    
    getGroups() {
        return this.groups;
    }
}

function solution(n, computers) {
    const unionFind = new UnionFind(n);
    for(let i = 0; i < n - 1; i += 1) {
        for(let j = i + 1; j < n; j += 1) {
            if(computers[i][j] === 1){
                unionFind.union(i+1, j+1);
            }
        }
    }
    return unionFind.getGroups();
}