/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 int j=0,v=0;
void inorder(struct TreeNode *root,int *a,int *i){
    if(root!=NULL){
        inorder(root->left,a,i);
         a[(*i)]=root->val;
        (*i)++;
         inorder(root->right,a,i);
    }
}
int kthSmallest(struct TreeNode* root, int k) {
    int i=0,*a;
    a=(int *)malloc(sizeof(int)*10000);
    inorder(root,a,&i);
    return a[k-1];
}