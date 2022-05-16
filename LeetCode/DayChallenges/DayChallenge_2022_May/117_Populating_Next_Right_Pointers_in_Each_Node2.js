/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */
/**
 * @param {Node} root
 * @return {Node}
 */
 var connect = function(root) {
    if(!root) return null;
    let prev = root;
    while(prev) {
        const dummy = new Node(0);
        let curr = dummy;
        while(prev) {
            if(prev.left) {
                curr.next = prev.left;
                curr = curr.next;
            }
            if(prev.right) {
                curr.next = prev.right;
                curr = curr.next;
            }
            prev = prev.next;
        }
        prev = dummy.next;
    }
    return root;
};

