# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order,
# and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_list = None
        previous_node = None
        overflow = 0
        while l1 is not None and l2 is not None:
            tmp_sum = l1.val + l2.val + overflow
            overflow = tmp_sum // 10
            if sum_list is None:
                sum_list = ListNode(tmp_sum if tmp_sum < 10 else tmp_sum % 10)
                previous_node = sum_list
            else:
                previous_node.next = ListNode(tmp_sum if tmp_sum < 10 else tmp_sum % 10)
                previous_node = previous_node.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            tmp_sum = l1.val + overflow
            overflow = tmp_sum // 10
            if sum_list is None:
                sum_list = ListNode(tmp_sum if tmp_sum < 10 else tmp_sum % 10)
                previous_node = sum_list
            else:
                previous_node.next = ListNode(tmp_sum if tmp_sum < 10 else tmp_sum % 10)
                previous_node = previous_node.next
            l1 = l1.next

        while l2 is not None:
            tmp_sum = l2.val + overflow
            overflow = tmp_sum // 10
            if sum_list is None:
                sum_list = ListNode(tmp_sum if tmp_sum < 10 else tmp_sum % 10)
                previous_node = sum_list
            else:
                previous_node.next = ListNode(tmp_sum if tmp_sum < 10 else tmp_sum % 10)
                previous_node = previous_node.next
            l2 = l2.next

        if overflow:
            current_node = ListNode(overflow)
            previous_node.next = current_node

        return sum_list

    @staticmethod
    def print_list(l: Optional[ListNode]) -> None:
        while l is not None:
            print(l.val)
            l = l.next


# NodeNull = ListNode() # U have to write after name of class () when call __init__ method!!!!!!!!!!!!

# NodeThree = ListNode()
# NodeThree1 = ListNode()

NodeMinusThree= ListNode(9)
NodeMinusTwo = ListNode(9, NodeMinusThree)
NodeMinusOne = ListNode(9, NodeMinusTwo)
NodeZero = ListNode(9, NodeMinusOne)
NodeOne = ListNode(9, NodeZero)
NodeTwo = ListNode(9, NodeOne)
NodeThree = ListNode(9, NodeTwo)

NodeZero1 = ListNode(9)
NodeOne1 = ListNode(9, NodeZero1)
NodeTwo1 = ListNode(9, NodeOne1)
NodeThree1 = ListNode(9, NodeTwo1)

# #Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Solution.print_list(NodeThree)
# print()
# Solution.print_list(NodeThree1)
# print()
Solution.print_list(Solution.add_two_numbers(None, NodeThree, NodeThree1))
