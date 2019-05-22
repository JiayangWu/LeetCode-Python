/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        std::map<RandomListNode*, int> Node_map;
        std::vector<RandomListNode *> Node_vector;
        RandomListNode* ptr = head;
        int i = 0;
        while(ptr){
            Node_vector.push_back(new RandomListNode (ptr->label));
            Node_map[ptr] = i;
            i ++;
            ptr = ptr->next;
        }
        Node_vector.push_back(0);
        ptr = head;
        i = 0;
        while(ptr){
            Node_vector[i]->next = Node_vector[i+1];
            if(ptr->random){
                Node_vector[i]->random = Node_vector[Node_map[ptr->random]];
            }
            i++;
            ptr = ptr->next;
        }
        return Node_vector[0];
    }
};