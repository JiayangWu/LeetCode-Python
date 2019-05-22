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
    ListNode* swapPairs(ListNode* head) {
        if (!head || !head->next)
            return head;
        ListNode n_head(0);
        ListNode* pre = &n_head;
        n_head.next = head;
        ListNode* ptr = head;
        while(ptr && ptr->next){
            pre->next = ptr->next;
            // if (!ptr->next)
            ptr->next = ptr->next->next;
            // else
                // ptr->next = NULL;
            pre->next->next = ptr;
            pre = pre->next->next;
            ptr = ptr->next;
        }
        return n_head.next;
        
    }
};