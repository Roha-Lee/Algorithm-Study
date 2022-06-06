/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
 var getIntersectionNode = function(headA, headB) {
    let currA = headA;
    let currB = headB;
    while(currA && currB) {
        if(currA === currB) return currA;
        currA = currA.next;
        currB = currB.next;
    }
    if(currA === null) currA = headB;
    if(currB === null) currB = headA;
    while (currA && currB) {
        if(currA === currB) return currA;
        currA = currA.next;
        currB = currB.next;
    }
    if(currA === null) currA = headB;
    if(currB === null) currB = headA;
    while (currA && currB) {
        if(currA === currB) return currA;
        currA = currA.next;
        currB = currB.next;
    }
};