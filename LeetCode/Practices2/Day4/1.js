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
 var oddEvenList = function(head) {
    const dummyOdd = new ListNode();
    const dummyEven = new ListNode();
    let odd = dummyOdd;
    let even = dummyEven;
    let index = 1;
    while (head !== null) {
        if (index % 2 === 0) {
            even.next = head;
            even = even.next;
        }
        else {
            odd.next = head;
            odd = odd.next;
        }
        head = head.next;
        index += 1;
    }
    odd.next = dummyEven.next;
    even.next = null;
    return dummyOdd.next;
};