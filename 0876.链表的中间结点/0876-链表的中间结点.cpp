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
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        if ((head == NULL) || (head->next == NULL)) return head;
        while(1){
            if (fast == NULL || fast->next == NULL)
                break;
            fast = fast->next->next;
            slow = slow->next;
            // cout<<slow->val<<" "<<fast->val<<endl;
        }
        return slow;
    }
};