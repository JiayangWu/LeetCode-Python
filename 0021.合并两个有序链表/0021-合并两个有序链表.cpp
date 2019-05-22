/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode temp_head(0);
        ListNode* pre = &temp_head;
        while(l1 && l2){
            if (l1->val<= l2->val){
                pre->next = l1;
                l1 = l1->next;
            }
            else{
                pre->next = l2;
                l2 = l2->next;
            }
            pre = pre->next;
        }
        if(l1) pre->next = l1;
        if(l2) pre->next = l2;
        return temp_head.next;
        
    }
};