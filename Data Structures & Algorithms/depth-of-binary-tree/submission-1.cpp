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
    void depth(TreeNode* root,int temp,int &ans){
        if (root==nullptr){
            ans=max(temp,ans);
            return;
        }
        depth(root->left,temp+1,ans);
        depth(root->right,temp+1,ans);
        return;
        
    }
    int maxDepth(TreeNode* root) {
        int ans=0;
        depth(root,0,ans);
        return ans;
        
    }
};
