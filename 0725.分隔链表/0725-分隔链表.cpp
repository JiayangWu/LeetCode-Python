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
    ListNode* partition(ListNode* head, int x) {
        ListNode less_head(0);
        ListNode more_head(1);
        ListNode* less_ptr = &less_head;
        ListNode* more_ptr = &more_head;
        while(head){
            if (head->val >= x){
                more_ptr->next = head;
                more_ptr = more_ptr->next;
            }
            else{
                less_ptr->next = head;
                less_ptr = less_ptr->next;
            }
            head = head->next;
        }
        less_ptr->next = more_head.next;
        more_ptr->next = NULL;
        return less_head.next;
        
    }
};