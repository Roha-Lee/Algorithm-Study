/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
 var removeNthFromEnd = function(head, n) {
    const dummy = new ListNode(null, head);
    let fast = dummy;
    let target = dummy.next;
    let prev = dummy;
    for(let i = 0; i < n; i += 1) {
        fast = fast.next;
    }
    while(fast.next) {
        target = target.next;
        prev = prev.next;
        fast = fast.next;
    }
    prev.next = target.next;
    return dummy.next;
};