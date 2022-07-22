/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} x
 * @return {ListNode}
 */
 var partition = function(head, x) {
    const less = new ListNode();
    const more = new ListNode();
    let currLess = less;
    let currMore = more;
    while(head) {
        if (head.val >= x) {
            currMore.next = head;
            currMore = currMore.next;
        }
        else {
            currLess.next = head;
            currLess = currLess.next;
        }
        head = head.next;
    }
    currLess.next = more.next;
    currMore.next = null;
    return less.next;
};