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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* res = new ListNode(-1);
        ListNode* cur = res;
        int carry = 0;
        while(l1 || l2){
            int t1 = l1? l1->val : 0;
            int t2 = l2? l2->val : 0;
            int sum = t1 + t2 + carry;
            carry = sum / 10;
            cur->next = new ListNode(sum % 10);
            cur = cur->next;
            if (l1) l1 = l1->next;
            if (l2) l2 = l2->next;
        }
        if (carry) cur->next =new ListNode(1);
        return res->next;
        
        
    }
};