/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 */
var Solution = function(head) {
    this.idx = 0;
    this.head = head;
    while (head) {
        this.idx += 1;
        head = head.next;
    }
};

/**
 * @return {number}
 */
Solution.prototype.getRandom = function() {
    let randint = Math.floor(Math.random() * this.idx);
    let node = this.head;
    while (randint > 0) {
        node = node.next;
        randint -= 1;
    }
    return node.val;
};

/** 
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(head)
 * var param_1 = obj.getRandom()
 */
