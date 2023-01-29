/**
 * @param {number} capacity
 */
var LFUCache = function(capacity) {
    this.capacity = capacity;
    this.currLength = 0;
    this.useCounter = new Map();
    this.table = new Map();
    this.cache = new Map();
};

/** 
 * @param {number} key
 * @return {number}
 */
LFUCache.prototype.get = function(key) {
    if (this.cache.has(key)) {
        this.useCounter.set(key, this.useCounter.get(key) + 1);
        this.updateTable(key, this.useCounter.get(key));
        return this.cache.get(key);
    }
    return -1;
};

/** 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
LFUCache.prototype.put = function(key, value) {
    if (this.capacity === 0) {
        return;
    }
    if (this.cache.has(key)) {
        this.cache.set(key, value);
        this.useCounter.set(key, this.useCounter.get(key) + 1);
        this.updateTable(key, this.useCounter.get(key));
        return;
    }
    if (this.currLength >= this.capacity) {
        this.eject();
    }
    this.currLength += 1;
    this.cache.set(key, value);
    this.useCounter.set(key, 1);
    this.updateTable(key, this.useCounter.get(key));
};

LFUCache.prototype.updateTable = function(key, count) {
    if (this.table.has(count)) {
        this.table.get(count).push(key);
    } else {
        this.table.set(count, [key]);
    }
    if (this.table.has(count-1)) {
        this.table.set(count-1, this.table.get(count-1).filter(item => item !== key));
        if (this.table.get(count-1).length === 0) {
            this.table.delete(count-1);
        }
    }
};

LFUCache.prototype.eject = function() {
    const maxCount = Math.min(...this.table.keys())
    const popItem = this.table.get(maxCount).shift();
    if (this.table.get(maxCount).length === 0) {
        this.table.delete(maxCount);
    }
    this.cache.delete(popItem);
    this.currLength -= 1;
};

/** 
 * Your LFUCache object will be instantiated and called as such:
 * var obj = new LFUCache(capacity)
 * var param_1 = obj.get(key)
 * obj.put(key,value)
 */
