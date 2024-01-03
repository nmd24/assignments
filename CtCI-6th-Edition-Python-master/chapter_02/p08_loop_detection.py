import unittest
from linked_list import LinkedList

def loop_detection(ll):
    fast = slow = ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast

class TestLoopDetection(unittest.TestCase):
    def test_loop_detection(self):
        # Test with an empty list
        empty_list = LinkedList()
        self.assertIsNone(loop_detection(empty_list))

        # Test with a list without a loop
        no_loop_list = LinkedList([1, 2, 3])
        self.assertIsNone(loop_detection(no_loop_list))

        # Test with a list with a loop
        looped_list = LinkedList(["A", "B", "C", "D", "E"])
        loop_start_node = looped_list.head.next.next  # "C"
        looped_list.tail.next = loop_start_node  # Creating a loop
        self.assertEqual(loop_detection(looped_list), loop_start_node)

if __name__ == '__main__':
    unittest.main()
