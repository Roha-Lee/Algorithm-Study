/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
    let curr = head;
    const values = [];
    while (curr) {
        values.push(curr.val);
        curr = curr.next;
    }
    return constructBST(values);
};

const constructBST = (values) => {
    if (values.length === 0) return null;
    const mid = Math.floor(values.length / 2);
    const curr = values[mid];
    const left = constructBST(values.slice(0, mid));
    const right = constructBST(values.slice(mid+1));
    return new TreeNode(curr, left, right);
};
