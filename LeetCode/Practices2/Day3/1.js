/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
 var isPalindrome = function(head) {
    let isPalindrome = true;
    const check = function(prev, curr) {
        if (prev.next === null) {
            return;
        }
        else {
            check(prev.next, curr.next);    
            if (prev && head && isPalindrome) {
                isPalindrome = head.val === curr.val;   
                prev.next = null;
                head = head.next;
            }
        }
    }
    let dummy = new ListNode(0, head);
    check(dummy, head);
    return isPalindrome;
};