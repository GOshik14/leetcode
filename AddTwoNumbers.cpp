// 2. Add Two Numbers
// You are given two non-empty linked lists representing two non-negative integers.
// The digits are stored in reverse order, and each of their nodes contains a single digit.
// Add the two numbers and return the sum as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.


#include <iostream>

 //Definition for singly-linked list.
 struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };

class Solution {
public:
    static ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
    {
        ListNode* sum = new(ListNode);
        int overflow_previous = 0;

        ListNode* curr_sum = nullptr;
        ListNode* curr_node_p1 =  l1;
        ListNode* curr_node_p2 =  l2;
        while(curr_node_p1 != nullptr && curr_node_p2 != nullptr)
        {
            int tmp_sum = curr_node_p1->val + curr_node_p2->val + overflow_previous;
            //ListNode tmp_next(tmp_sum%10);
            if(curr_sum == nullptr) //first node
            {
                curr_sum = sum;
                curr_sum->val = (tmp_sum > 9 ? tmp_sum%10 : tmp_sum);
                overflow_previous = tmp_sum/10;
            } 
            else
            {
                ListNode* tmp_next = new(ListNode);
                tmp_next->val = (tmp_sum > 9 ? tmp_sum%10 : tmp_sum);
                curr_sum->next = tmp_next;

                overflow_previous = tmp_sum/10;
                curr_sum = tmp_next;  
            }

            curr_node_p1 = curr_node_p1->next;
            curr_node_p2 = curr_node_p2->next;
        }

        while(curr_node_p1 != nullptr)
        {
            ListNode* tmp_next = new(ListNode);
            int tmp_sum = curr_node_p1->val + overflow_previous;
            tmp_next->val = (tmp_sum > 9 ? tmp_sum%10 : tmp_sum);
            curr_sum->next = tmp_next;
            curr_sum = tmp_next;
            curr_node_p1 = curr_node_p1->next;

            overflow_previous = tmp_sum/10;

        }

        while(curr_node_p2 != nullptr)
        {
            ListNode* tmp_next = new(ListNode);
            int tmp_sum = curr_node_p2->val + overflow_previous;
            tmp_next->val = (tmp_sum > 9 ? tmp_sum%10 : tmp_sum);
            curr_sum->next = tmp_next;
            curr_sum = tmp_next;
            curr_node_p2 = curr_node_p2->next;

            overflow_previous = tmp_sum/10;
        }

        if(overflow_previous)
        {
            ListNode* tmp_next = new(ListNode);
            tmp_next->val = 1;
            curr_sum->next = tmp_next;
        }


        return sum;
    }

    static void PrintList(const ListNode* FirstNode)
    {
        const ListNode* currentNode = FirstNode;
        while(currentNode != nullptr)
        {
            std::cout << currentNode->val << '\t';
            currentNode = currentNode->next;
        }
        std::cout << std::endl;
    }

};


int main()
{
    // ListNode MinusThree(9);
    // ListNode MinusTwo(9, &MinusThree);
    // ListNode MinusOne(9, &MinusTwo);
    // ListNode ZeroNode(9, &MinusOne);
    ListNode FirstNode(9);
    ListNode SecondNode(4, &FirstNode);
    ListNode ThirdNode(2, &SecondNode);

    
    ListNode ZeroNode1(9);
    ListNode FirstNode1(4, &ZeroNode1);
    ListNode SecondNode1(6, &FirstNode1);
    ListNode ThirdNode1(5, &SecondNode1);

    Solution::PrintList(Solution::addTwoNumbers(&ThirdNode, &ThirdNode1));

    int a;
    std::cin >> a;


    return 0;
}
