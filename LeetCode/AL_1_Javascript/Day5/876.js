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
 var middleNode = function(head) {
    let slow = head;
    let fast = head;
    while(fast.next) {
        fast = fast.next;
        slow = slow.next;
        if(fast.next) {
            fast = fast.next;
        }
    }
    return slow;
};