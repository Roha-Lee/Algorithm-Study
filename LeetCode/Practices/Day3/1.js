var mergeTwoLists = function(list1, list2) {
    const dummy = new ListNode();
    let curr = dummy;
    let node1 = list1;
    let node2 = list2;
    while(node1 && node2) {
        if(node1.val < node2.val) {
            curr.next = node1;
            node1 = node1.next;
        }
        else if(node1.val >= node2.val) {
            curr.next = node2;
            node2 = node2.next;
        }
        curr = curr.next;
    }
    if(!node1) curr.next = node2;
    if(!node2) curr.next = node1;
    return dummy.next;
};