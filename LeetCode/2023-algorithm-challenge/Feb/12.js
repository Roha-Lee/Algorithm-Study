/**
 * @param {number[][]} roads
 * @param {number} seats
 * @return {number}
 */
var minimumFuelCost = function(roads, seats) {
    let totalCost = 0;    
    const { graph, visited } = new Graph(roads);
    visited[0] = true;
    const dfs = (curr) => {
        let count = 1;
        for (let next of (graph[curr] || []) ) {
            if (!visited[next]) {
                visited[next] = true;
                count += dfs(next);
                visited[next] = false;
            }
        }
        if (curr !== 0) {
            totalCost += Math.ceil(count / seats);
        }
        return count;
    } 
    dfs(0);
    return totalCost;
};

class Graph {
    constructor(roads) {
        this.graph = {};
        this.visited = {};
        for (let [src, dst] of roads) {
            this.graph[src] = this.graph[src] || [];
            this.graph[dst] = this.graph[dst] || [];
            this.graph[src].push(dst);
            this.graph[dst].push(src);
            this.visited[src] = false;
            this.visited[dst] = false;
        }

        return {
            graph: this.graph,
            visited: this.visited,
        };
    }
}
