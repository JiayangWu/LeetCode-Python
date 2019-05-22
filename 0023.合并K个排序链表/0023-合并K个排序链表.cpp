/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
bool cmp(const ListNode* a, const ListNode* b){
    return a->val < b->val;
}
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        std::vector<ListNode *> value;
        for(int i = 0; i< lists.size(); ++i){
            ListNode* head = lists[i];
            while(head){
                value.push_back(head);
                head = head->next;
            }
        }
        
        std::sort(value.begin(),value.end(), cmp);
        if (value.size() == 0)
            return NULL;
        
        for(int i = 1; i<value.size(); ++i){
            value[i-1]->next = value[i];
        }
        value[value.size()-1]->next = NULL;
        return value[0];
        
    }
};