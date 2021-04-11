/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    var fakeNode =  new ListNode(-1)  //creating a fake node so that we do no have to write conditions for checking if list is empty or not, and in the end return the node after the fakenode
    var last = fakeNode
    while(l1 != null && l2 != null){
        if(l1.val < l2.val){
            last.next = l1
            last = l1
            l1 = l1.next
        }
        else{
            last.next = l2
            last = l2
            l2 = l2.next
        }
    }
        if(l1!=null){
            last.next = l1
        }
        if(l2!=null){
            last.next = l2
        }
    return fakeNode.next
};