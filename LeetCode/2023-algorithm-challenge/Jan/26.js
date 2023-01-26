/**
 * @param {number} n
 * @param {number[][]} flights
 * @param {number} src
 * @param {number} dst
 * @param {number} k
 * @return {number}
 */
var findCheapestPrice = function(n, flights, src, dst, k) {
    const graph = generateGraph(flights);
    let costs = new Array(n).fill(Infinity);
    costs[src] = 0;
    let currQueue = [src];
    let nextQueue = [];
    for (let count = 0; count <= k; count += 1) {
        const newCosts = [...costs];
        while(currQueue.length) {
            const curr = currQueue.shift();
            for (let [to, price] of (graph[curr] || [])) {
                if (newCosts[to] > costs[curr] + price) {
                    newCosts[to] = costs[curr] + price;
                    nextQueue.push(to);
                }
            }
        }
        costs = newCosts;
        currQueue = nextQueue;
        nextQueue = [];
    }
    return costs[dst] === Infinity ? -1 : costs[dst];
};

const generateGraph = (flights) => {
    const graph = {};
    for (let [from, to, price] of flights) {
        graph[from] = graph[from] || [];
        graph[from].push([to, price]);
    }
    return graph;
};
