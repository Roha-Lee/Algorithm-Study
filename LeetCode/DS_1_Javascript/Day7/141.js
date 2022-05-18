/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
 var hasCycle = function(head) {
    let slow = head;
    let fast = head;
    while(fast) {
        slow = slow.next;
        fast = fast.next;
        if(fast) fast = fast.next;
        if(slow === fast && fast !== null) return true;
    }
    return false;
};