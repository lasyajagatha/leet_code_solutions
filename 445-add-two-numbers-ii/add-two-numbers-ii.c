/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 typedef struct ListNode *n;
 n reverse(n h){
    n p=NULL,r=h,ne=NULL;
    while(r!=NULL){
        ne=r->next;
        r->next=p;
        p=r;
        r=ne;
    }
    return p;
 }
 n create(int v){
    n h=(n)malloc(sizeof(struct ListNode));
    h->next=NULL;
    h->val=v;
    return h;
 }
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int c,a=0;
    n r=NULL;
    n h1=reverse(l1);
    n h2=reverse(l2);
    while(h1!=NULL && h2!=NULL){
         
            c=h1->val+h2->val+a;
            if(c>9){
                a=c/10;
                c=c%10;
            } else{
                a=0;
            }
           
            if(r==NULL){
            r=create(c);
            } else{
                n p=r;
                while(p->next!=NULL){
                    p=p->next;
                }
                p->next=create(c);
            }
        h1=h1->next;
        h2=h2->next;
    }
    while(h1!=NULL){
        c=h1->val+a;
        if(c>9){
            a=c/10;
            c=c%10;
        } else{
            a=0;
        }
        
        if(r==NULL){
        r=create(c);
        } else{
            n p=r;
            while(p->next!=NULL){
                p=p->next;
            }
            p->next=create(c);
        }
        h1=h1->next;
    }
     while( h2!=NULL){
         
            c=h2->val+a;
            if(c>9){
                a=c/10;
                c=c%10;

            } else{
                a=0;
            }
           
            if(r==NULL){
            r=create(c);
            } else{
                n p=r;
                while(p->next!=NULL){
                    p=p->next;
                }
                p->next=create(c);
            }
       
        h2=h2->next;
    }
    if(a==1){
        n q=r;
        while(q->next!=NULL){
            q=q->next;
        }
        q->next=create(1);
    }
    return reverse(r);

}