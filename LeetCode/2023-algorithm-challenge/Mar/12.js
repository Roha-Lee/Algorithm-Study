/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function(lists) {
    if (lists.length === 0) return null;
    const valToIdx = new Map();
    const heap = new MinPriorityQueue();
    let val;
    for (let i = 0; i < lists.length; i += 1) {
        if (lists[i] === null) {
            continue;
        }
        val = lists[i].val;
        if (valToIdx.has(val)) {
            const temp = valToIdx.get(val);
            temp.push(i);
            valToIdx.set(val, temp);
        } else {
            valToIdx.set(val, [i]); 
        }
        heap.enqueue(lists[i].val);
    }
    if (valToIdx.size === 0) return null;
    const head = new ListNode();
    let curr = head;
    let newVal;
    while (heap.front() !== null) {
        val = heap.dequeue().element;
        curr.next = new ListNode(val);
        curr = curr.next;
        idxToUpdate = valToIdx.get(val).pop();
        if (valToIdx.get(val).length === 0) {
            valToIdx.delete(val);
        }
        if (lists[idxToUpdate].next !== null) {
            lists[idxToUpdate] = lists[idxToUpdate].next;
            newVal = lists[idxToUpdate].val
            heap.enqueue(newVal);
            if (valToIdx.has(newVal)) {
                const temp = valToIdx.get(newVal);
                temp.push(idxToUpdate);
                valToIdx.set(newVal, temp);
            } else {
                valToIdx.set(newVal, [idxToUpdate]);
            }
        }
    }
    return head.next;
};
