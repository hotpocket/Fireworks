class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle(head):
    """
    Finds the middle node of a linked list using the fast and slow pointer method.

    Args:
        head: The head of the linked list.

    Returns:
        The middle node of the linked list, or None if the list is empty.
    """
    if not head:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

middle = find_middle(head)
if middle:
    print(f"Middle node value: {middle.value}") # Output: Middle node value: 3

# Example usage:
# create a linked list: 1 -> 2 -> 3 -> 4
head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

middle2 = find_middle(head2)
if middle2:
    print(f"Middle node value: {middle2.value}") # Output: Middle node value: 3
