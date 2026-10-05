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
    public ListNode reverseKGroup(ListNode he, int k) {
         LinkedList<Integer> head=new LinkedList<>();
        LinkedList<Integer> l=new LinkedList<>();
        LinkedList<Integer> s=new LinkedList<>();
        int p=k,i;
        ListNode h=he;
        while(h!=null){
            head.add(h.val);
            h=h.next;
        }
        while(head.size()!=0 && head.size()>=k){
            k=p;
            while(k!=0 && head.size()>=k){
                s.addFirst(head.getFirst());
                k=k-1;
                head.removeFirst();
            }
            while(s.size()!=0){
                l.addLast(s.getFirst());
                s.removeFirst();
            }
        }
        while(head.size()!=0){
            l.add(head.getFirst());
            head.removeFirst();
        }
        ListNode m=null,nn,tem;
        for(i=0;i<l.size();i++){
             nn=new ListNode(l.get(i));
             if(m==null){
                m=nn;
             } else{
                tem=m;
                while(tem.next!=null){
                    tem=tem.next;
                }
                tem.next=nn;
             }
        }
        return m;
    }
}