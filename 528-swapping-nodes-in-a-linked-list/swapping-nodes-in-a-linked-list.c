/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 typedef struct ListNode* node;
struct ListNode* swapNodes(struct ListNode* head, int k) {
       node temp=head;
       int i=0,u,v;
       while(temp!=NULL ){
        temp=temp->next;
        i++;
       }
       temp=head;
       int a[i];
       for(int j=0;j<i;j++){
            a[j]=temp->val;
            temp=temp->next;
       }
       u=a[k-1];
       a[k-1]=a[i-k];
       a[i-k]=u;
       temp=head;
       for(int j=0;j<i;j++){
              temp->val=a[j];
              temp=temp->next;
       }
      return head;


}