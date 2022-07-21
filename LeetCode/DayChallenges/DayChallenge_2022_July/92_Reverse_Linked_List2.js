/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
 var reverseBetween = function(head, left, right) {
    if (left === right) return head;
    
    const dummy = new ListNode(0, head);
    let curr = dummy;
    
    for (let i = 0; i < left - 1; i += 1) {
        curr = curr.next;
    }
    let [beforeStart, endNode] = [curr, curr.next];
    let temp;
    for (let i = 0; i < right - left; i += 1) {
        temp = beforeStart.next;
        beforeStart.next = endNode.next;
        endNode.next = endNode.next.next;
        beforeStart.next.next = temp;
    }
    return dummy.next;
};