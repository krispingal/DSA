import pytest

from src.dsa.datastructures.linked_list import LinkedList

class TestLinkedList:

    @pytest.mark.parametrize("actual, expected, msg", [
        (["A"], ["A"], "List append should work with only 1 element"),
        (["A", "B", "C"], ["A", "B", "C"], "List append should work with multiple strings")
    ])
    def test_append(self, actual, expected, msg):
        linked_list = LinkedList()
        for v in actual:
            linked_list.append(v)
        cur = linked_list.head
        for expected_value in expected:
            assert cur.val == expected_value, msg
            cur = cur.next

    @pytest.mark.parametrize("actual, expected, msg", [
        ([1], [1], "List append should work with only 1 element"),
        ([3, 2, 1], [1, 2, 3], "List append should work with multiple nums")
    ])
    def test_prepend(self, actual, expected, msg):
        linked_list = LinkedList()
        for v in actual:
            linked_list.prepend(v)
        cur = linked_list.head
        for expected_value in expected:
            assert cur.val == expected_value, msg
            cur = cur.next

    def test_insert_at_position(self):
        linked_list = LinkedList()
        assert not linked_list.insert_at_position(-2, 5), "Index cannot be less than 0"
        assert linked_list.insert_at_position(0, -1), "Should allow insertion in an empty array at idx 0"
        assert linked_list.head.val == -1, "Inserted element at 0th position should match the value that was passed."
        for i in range(3):
            linked_list.append(i)
        assert linked_list.insert_at_position(0, -2)
        assert linked_list.head.val == -2, "Insert element at 0th position when list is non-empty should pass."
        assert linked_list.head.next.val == -1, "Previously inserted element should remain there."
        assert linked_list.insert_at_position(1, -3), "Insert should succeed when position is not sentinel"
        assert linked_list.head.next.val == -3, "Previously inserted element should remain there."
        assert linked_list.insert_at_position(6, -4), "Insert should succeed when insert at the end of LL."
        cur = linked_list.head
        for i in range(6): #LL size is 7, needs 6 skips to reach tail
            cur = cur.next
        assert cur.val == -4, "Inserted value at tail end should be at tail"
        assert not linked_list.insert_at_position(8, -5), "LL cannot insert without any preceding elements"



    @pytest.mark.parametrize("actual, del_value, expected, msg", [
        (["A"], "A", [], "List deletion should work with only 1 element"),
        (["A", "B", "C"], "A", ["B", "C"], "List deletion should work when first element is removed"),
        (["A", "B", "C"], "B", ["A", "C"], "List deletion should work when last element is removed"),
        (["A", "B", "C"], "C", ["A", "B"], "List deletion should work when middle element is removed"),
        (["A", "B", "C", "B"], "B", ["A", "C", "B"], "List deletion should delete only the first satisfying element"),

    ])
    def test_delete_by_value_success(self, actual, del_value, expected, msg):
        linked_list = LinkedList()
        for a in actual:
            linked_list.append(a)
        assert linked_list.delete_by_value(del_value)
        cur, i = linked_list.head, 0
        while cur:
            assert cur.val == expected[i], msg
            cur, i = cur.next, i + 1

    @pytest.mark.parametrize("actual, del_value, expected, msg", [
        ([], "A", [], "List deletion should not work with empty list"),
        (["A", "B", "C"], "D", ["A", "B", "C"], "List deletion should fail if element is not present")
    ])
    def test_delete_by_value_failure(self, actual, del_value, expected, msg):
        linked_list = LinkedList()
        for a in actual:
            linked_list.append(a)
        assert not linked_list.delete_by_value(del_value)
        cur, i = linked_list.head, 0
        while cur:
            assert cur.val == expected[i], msg
            cur, i = cur.next, i + 1


    @pytest.mark.parametrize("actual, delete_idx, expected, msg", [
        (["A"], 0, [], "List deletion should work with only 1 element"),
        (["A", "B", "C"], 0, ["B", "C"], "List deletion should work when first element is removed"),
        (["A", "B", "C"], 1, ["A", "C"], "List deletion should work when first element is removed"),
        (["A", "B", "C"], 2, ["A", "B"], "List deletion should work when first element is removed")
    ])
    def test_delete_at_position(self, actual, delete_idx, expected, msg):
        linked_list = LinkedList()
        for a in actual:
            linked_list.append(a)
        assert linked_list.delete_at_position(delete_idx)
        cur, i = linked_list.head, 0
        while cur:
            assert cur.val == expected[i], msg
            cur, i = cur.next, i + 1

    @pytest.mark.parametrize("actual, del_idx, expected, msg", [
        ([], 1, [], "List deletion should not work with empty list"),
        (["A", "B", "C"], -2, ["A", "B", "C"], "List deletion should fail if idx is negative"),
        (["A", "B", "C"], 3, ["A", "B", "C"], "List deletion should fail if idx does not exist")
    ])
    def test_delete_by_position_failure(self, actual, del_idx, expected, msg):
        linked_list = LinkedList()
        for a in actual:
            linked_list.append(a)
        assert not linked_list.delete_at_position(del_idx)
        cur, i = linked_list.head, 0
        while cur:
            assert cur.val == expected[i], msg
            cur, i = cur.next, i + 1

    @pytest.mark.parametrize("elements, key, expected, msg", [
        ([], 1, False, "Should be able to search in a list with only 1 element"),
        ([1], 1, True, "Should be able to search in a list with only 1 element"),
        ([1, 2, 3], 3, True, "Should be able to search in a list with multiple elements"),
        ([1, 2, 3], 0, False, "Should fail if element is not present in LL")
    ])
    def test_search(self, elements, key, expected, msg):
        linked_list = LinkedList()
        for e in elements:
            linked_list.append(e)
        assert linked_list.search(key) == expected, msg

    @pytest.mark.parametrize("elements, expected, msg", [
        ([], "\n", "Display should work when LL is empty"),
        (["A"], "A \n", "Display should work with single element"),
        ([1, 2, 3], "1 2 3 \n", "Display should work with multiple elements")
    ])
    def test_display(self, capfd, elements, expected, msg):
        linked_list = LinkedList()
        for e in elements:
            linked_list.append(e)
        linked_list.display()
        out, err = capfd.readouterr()
        assert out == expected, msg
