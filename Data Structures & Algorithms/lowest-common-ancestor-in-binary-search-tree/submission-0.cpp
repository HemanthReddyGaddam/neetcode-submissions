/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {

        if(p->val>q->val){
            return lowestCommonAncestor(root,q,p);
        }

        int sm = p->val;
        int hi = q->val;

        if (sm <= root->val && root->val <= hi){
            return root;
        }

        if(root->val>sm){
            return lowestCommonAncestor(root->left,q,p);
        }
        if(root->val<hi){
            return lowestCommonAncestor(root->right,q,p);
        }

        return nullptr;
        
        
    }
};
