import pytest
from solution_add_two_numbers import ListNode, Solution


def to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([5], [5], [0, 1]),
    ],
)
def test_add_two_numbers(l1, l2, expected):
    s = Solution()
    l1_node = to_linked_list(l1)
    l2_node = to_linked_list(l2)
    result = s.addTwoNumbers(l1_node, l2_node)
    assert to_list(result) == expected
