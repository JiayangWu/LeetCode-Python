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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        ListNode* ptr = head->next;
        ListNode* pre = head;
        while(1){
            // cout<<ptr->val<<" "<<pre->val<<endl;
            while (pre->val == ptr->val){
                // cout<<"1"<<endl;
                ptr = ptr->next;  
                if (!ptr) break;
            }
            pre->next = ptr;
            pre = pre->next;
            if (!ptr) break;

        }
        return head;
        
    }
};