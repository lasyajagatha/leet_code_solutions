/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeNodes(ListNode head) {
        ArrayList<Integer> l=new ArrayList<>();
       // ListNode k=head;
        int i=0,s=0;
        while(head!=null){
            if(head.val!=0 ){
                s=s+head.val;
            }else{
                if(s!=0){
                l.add(s);
                }
                s=0;
            }
            head=head.next;
        }
        i=0;
        ListNode h = null, tail = null;
        for (int val : l) {
            ListNode nn = new ListNode(val);
            if (h == null) {
                h = nn;
                tail = nn;
            } else {
                tail.next = nn;
                tail = nn; 
            }
        }
        return h;
    }
}