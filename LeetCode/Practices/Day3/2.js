/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
 var reverseList = function(head) {
    if (head === null) return head;
    return reverse(head, head.next);
};

var reverse = function(prev, curr) {
    if (curr === null) return prev;
    const node = reverse(curr, curr.next);    
    if (curr.next === null) {
        curr.next = prev;
        prev.next = null; 
    }
    return node;
}