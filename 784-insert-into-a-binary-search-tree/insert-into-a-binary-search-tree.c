/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 struct TreeNode *create(int v){
    struct TreeNode *n=(struct TreeNode *)malloc(sizeof(struct TreeNode));
    n->val=v;
    n->left=NULL;
    n->right=NULL;
    return n;
 }
struct TreeNode* insertIntoBST(struct TreeNode* root, int val) {
    if(root==NULL){
       struct TreeNode *nn=create(val);
        return nn;
    }
    if(root->val < val){
        root->right=insertIntoBST(root->right,val);
    } else if(root->val > val){
        root->left=insertIntoBST(root->left,val);
    } else{
        return root;
    }
    return root;
}