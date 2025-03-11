===========
Linked List
===========

Introduction
=============
A Linked List is a dynamic data structure consisting of nodes, where each node contains a value and a reference (or pointer) to the next node in the sequence. Unlike arrays, linked list elements are not stored in contiguous memory locations. This structural distinction makes linked lists flexible but introduces certain trade-offs compared to arrays.

Advantages Over Arrays
----------------------
1. **Dynamic Memory Allocation**:
    - Arrays require their size to be defined at compile time to allocate a contiguous block of memory. Resizing an array is computationally expensive as it involves creating a larger array and copying existing elements.
    - Linked lists, on the other hand, allocate memory for each node dynamically at runtime, providing flexibility in memory management and supporting dynamic resizing.

2. **Efficient Insertions and Deletions**:
    - Inserting or removing elements at the head of a linked list is an :math:`O(1)` operation, which is significantly more efficient than arrays in scenarios where frequent head insertions or deletions are required.

3. **No Fixed Size Requirement**:
    - Linked lists grow and shrink dynamically, node by node, eliminating the need for predefined 
    size requirements.

Disadvantages Compared to Arrays
--------------------------------
1. **Access Time**:
    - Accessing an element by index in a linked list requires traversing the list from the head, 
    resulting in an :math:`O(n)` time complexity. In contrast, arrays offer constant-time (:math:`O(1)`) 
    access since elements are stored contiguously in memory.

2. **Memory Overhead**:
    - Each node in a linked list contains a pointer in addition to the data value, increasing memory usage compared to arrays.

3. **Performance During Full Scans**:
    - When traversing the entire list, arrays can be more efficient due to CPU caching. The contiguous memory layout of arrays allows them to benefit from reduced memory access overhead, as all elements are likely to reside on the same memory page.

Applications
------------
Linked lists are a foundational data structure used to implement more complex data types like stacks, queues, 
and graphs. For instance, in stacks, the push and pop operations (inserting and removing elements at the beginning) are efficiently supported by the :math:`O(1)` insertion and deletion operations of linked lists.

Core Concepts
=============

Nodes in a Linked List
----------------------
The basic building block of a linked list is the node. Each node consists of:

- A **value**: The data stored in the node.
- A **reference** (or pointer) to the next node in the sequence.

Below is the implementation of the ``ListNode`` class, which represents a single node in the linked list:

.. code-block:: python

    class ListNode(Generic[T]):
    """Represents a node in a linked list."""
    def __init__(self, val: T, next: Optional["ListNode"] = None) -> None:
        """Initializes a node with a value and a reference to the next node."""
        self.val = val
        self.next = next

The Linked List Structure
-------------------------
A linked list is essentially a sequence of nodes, with the *head* node serving as the entry point. 
The linked list maintains a reference to the head node, and all other nodes are accessed by traversing the list sequentially from this head.

The following ``LinkedList`` class implements a basic linked list:

.. code-block:: python

    class LinkedList(Generic[T]):
    """Represents a singly linked list."""
    
    def __init__(self) -> None:
        """Initializes an empty linked list."""
        self.head = None

---------------------------

API Overview
============
This section provides a high-level summary of the operations supported by the ``LinkedList`` class. 
For detailed method signatures, arguments, and examples, refer to the full API Reference at the end of 
this document.

- **Construction**:
    * ``__init__``: Initialize an empty linked list.

- **Modification**:
    * ``prepend``: Insert a value at the beginning of the list (:math:`O(1)`).
    * ``append``: Add a value to the end of the list (:math:`O(n)`).
    * ``insert_at_position``: Insert a value at a specific position (:math:`O(n)`).
    * ``delete_by_value``: Remove the first occurrence of a value (:math:`O(n)`).
    * ``delete_at_position``: Remove a value at a specific position (:math:`O(n)`).
    * ``reverse``: Reverse the entire list (:math:`O(n)`).

- Access and Search:
    * ``search``: Find the index of the first occurrence of a value (:math:`O(n)`).
    * ``get_node_at``: Retrieve the node at a specific index (:math:`O(n)`).

You can find the entire API for linked lists in the :class:`API reference section <dsa.datastructures.linked_list.LinkedList>`.

Implementation Details
======================

A linked list is implemented using two primary components: nodes and the list structure that organizes them. Here's an overview of the patterns and considerations involved in the implementation:

1. Traversing the List
----------------------

Traversing a linked list involves starting at the head node and moving through each node's next pointer until the desired node is found or the end of the list is reached.

- **Key Pattern**:

.. code-block:: python

    cur = self.head
    while cur:
        # Perform operations with cur
        cur = cur.next

- Used in:
    * Searching for a value (``search`` method).
    * Finding the last node for appending (``append`` method).
    * Reversing the list (``reverse`` method).

---------------------------

2. Handling Edge Cases
----------------------

Edge cases must be considered to ensure robust implementation. These include:

- **Empty List**:
    * Methods like ``delete_at_position`` or ``reverse`` should handle scenarios where self.head is None.

- **Single Node List**:
    * Operations like ``delete_at_position`` and ``reverse`` need to account for the case where there is only one node, ensuring pointers are correctly updated.

- **Invalid Indices**:
    * Index-based operations (insert_at_position, get_node_at, delete_at_position) must handle:
    * Negative indices.
    * Indices larger than the current length of the list.

- **Value Not Found**:
    * Methods like ``delete_by_value`` and ``search`` must handle cases where the target value is not present in the list.

-----------------------

3. Maintaining Pointers
-----------------------

In Python, objects are referenced by pointers. In a linked list, the ``next`` attribute of a node stores the reference to the subsequent node. Here's how pointers are used:

- **Inserting a Node**:
    * To insert a node at a given position:
            1. Traverse to the preceding node.
            2. Update its next pointer to the new node.
            3. Point the new node’s next to the succeeding node.

- **Deleting a Node**:
    * To delete a node:
            Traverse to the preceding node.
            Update its next pointer to skip the node being deleted.

4. Iterative Patterns
---------------------

- **Head Manipulation**:
    * Most operations start by modifying ``self.head``, such as ``prepend`` or ``delete_at_position``.

- **Temporary Variables**:
    * Temporary variables are used to avoid losing references during operations, such as:

.. code-block:: python

    temp = cur.next
    cur.next = None  # Remove connection
    cur = temp       # Proceed to next node

---------------

Code Walkthrough
==================

This section introduces the implementation of the linked list, breaking it into logical components to make the code accessible and easy to understand. The walkthrough provides detailed commentary on the following:

1. **Core Classes and Attributes**:
   - ``ListNode``: Represents a single node in the linked list.
   - ``LinkedList``: Encapsulates the linked list and its operations.

2. **Methods**:
    - Node Manipulation:
        * ``prepend``, ``append``, and ``insert_at_position``.
    - Deletion:
        * ``delete_by_value`` and ``delete_at_position``.
    - Search:
        * ``search`` and ``get_node_at``.
    - Utility
        * ``reverse`` and ``__str__``.

---------------

Core Classes and Attributes
---------------------------
``ListNode``
This class defines the basic unit of a linked list—a node.

- **Attributes**:
  - ``val``: Stores the value of the node.
  - ``next``: Points to the next node in the list (or ``None`` if it's the last node).

.. code-block:: python

    class ListNode(Generic[T]):
        def __init__(self, val: T, next: Optional["ListNode"] = None) -> None:
            self.val = val
            self.next = next


``LinkedList``
This class manages the linked list and provides methods for manipulating it.

- **Attributes**:
    * ``head``: Points to the first node of the linked list. If the list is empty, `head` is `None`.

.. code-block:: python

    class LinkedList(Generic[T]):
        def __init__(self) -> None:
            self.head = None

----------

Key Methods
----------------
Here’s an overview of the most important methods, organized by functionality:


Node Manipulation
^^^^^^^^^^^^^^^^^

1. ``prepend``: Adds a node to the beginning of the list.
    - **Logic**: Creates a new node and sets its ``next`` pointer to the current head. Updates the head to the new node.
    - **Time Complexity**: :math:`O(1)`.

.. code-block::python

    def prepend(self, val: T) -> None:
        new_node = ListNode(val, self.head)
        self.head = new_node


2. ``append``: Adds a node to the end of the list.
    - **Logic**: Traverses the list to find the last node and updates its ``next`` pointer.
    - **Time Complexity**: :math:`O(n)`.

.. code-block:: python

    def append(self, val: T) -> None:
        if not self.head:
            self.head = ListNode(val, None)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val, None)


3. ``insert_at_position``: Inserts a node at a specific index.
    - **Logic**: Traverses to the specified position, updates pointers to insert the node.
    - **Edge Cases**:
        * Invalid position (``position < 0`` or beyond the list length).
        * Insert at the head (``position == 0``).

.. code-block:: python

    def insert_at_position(self, position: int, val: T) -> bool:
        if position < 0:
            return False
        if position == 0:
            new_node = ListNode(val, self.head)
            self.head = new_node
            return True
        cur = self.head
        index = 0
        while cur and index < position - 1:
            cur = cur.next
            index += 1
        if cur:
            new_node = ListNode(val, cur.next)
            cur.next = new_node
            return True
        return False


---------

Deletion
^^^^^^^^
1. ``delete_by_value``: Removes the first node containing the specified value.
    - **Logic**: Traverses the list, skipping the node to be deleted by updating pointers.
    - **Edge Case**: Deleting the head.

.. code-block:: python

    def delete_by_value(self, key: T) -> bool:
        if self.head and self.head.val == key:
            self.head = self.head.next
            return True
        cur, prev = self.head, None
        while cur:
            if cur.val == key:
                if prev:
                    prev.next = cur.next
                return True
            prev, cur = cur, cur.next
        return False


2. ``delete_at_position``: Removes the node at a given position.
    - **Logic**: Similar to ``delete_by_value`` but uses an index for traversal.
    - **Edge Cases**:
        * Invalid position.
        * Deleting the head.

--------------

Search
^^^^^^

1. ``search``: Finds the index of the first node containing a specific value.
    - **Logic**: Traverses the list while comparing values.
    - **Time Complexity**: :math:`O(n)`.

.. code-block:: python

    def search(self, key: T) -> int:
        cur = self.head
        index = 0
        while cur:
            if cur.val == key:
                return index
            cur = cur.next
            index += 1
        return -1


2. ``get_node_at`` Retrieves the node at a specific index.
    - **Logic**: Similar to ``search``, but returns the node itself.

------------

Utility
^^^^^^^

1. ``reverse`` Reverses the linked list.
    - **Logic**: Iteratively reverses pointers.
    - **Time Complexity**: :math:`O(n)`.

.. code-block:: python

    def reverse(self) -> None:
        cur, prev = self.head, None
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        self.head = prev

2. **`__str__`**: Converts the list to a string representation.

----------


Performance Analysis
====================
Time and Space Complexity of Linked List Operations
---------------------------------------------------

+------------------------------+---------------------+----------------------+------------------------------------------------------------------------+
| **Operation**                | **Time Complexity** | **Space Complexity** | **Description**                                                        |
+==============================+=====================+======================+========================================================================+
| **Access (by index)**        | :math:`O(n)`        | :math:`O(1)`         | Traverses the list sequentially to access an element.                  |
+------------------------------+---------------------+----------------------+------------------------------------------------------------------------+
| **Search**                   | :math:`O(n)`        | :math:`O(1)`         | Linear traversal to find the desired value.                            |
+------------------------------+---------------------+----------------------+------------------------------------------------------------------------+
| **Prepend (Insert at Head)** | :math:`O(1)`        | :math:`O(1)`         | Directly updates the `head` pointer.                                   |
+------------------------------+---------------------+----------------------+------------------------------------------------------------------------+
| **Append (Insert at Tail)**  | :math:`O(n)`        | :math:`O(1)`         | Traverses the list to find the tail and updates the pointer.           |
+------------------------------+---------------------+----------------------+------------------------------------------------------------------------+
| **Insert at Position**       | :math:`O(n)`        | :math:`O(1)`         | Traverses to the position, updates pointers.                           |
+------------------------------+---------------------+----------------------+------------------------------------------------------------------------+
| **Delete by Value**          | :math:`O(n)`        | :math:`O(1)`         | Linear traversal to find the node, then updates pointers.              |
+------------------------------+---------------------+----------------------+------------------------------------------------------------------------+
| **Delete at Position**       | :math:`O(n)`        | :math:`O(1)`         | Similar to `delete_by_value` but uses an index for traversal.          |
+------------------------------+---------------------+----------------------+------------------------------------------------------------------------+  
| **Reverse**                  | :math:`O(n)`        | :math:`O(1)`         | Reverses pointers in a single traversal.                               |
+------------------------------+---------------------+----------------------+------------------------------------------------------------------------+
| **Space per Node**           | —                   | :math:`O(1)`         | Each node requires memory for the value and a pointer to the next node.|
+------------------------------+---------------------+----------------------+------------------------------------------------------------------------+


Comparison with Arrays
----------------------
+------------------------------+----------------------------------------------------+-----------------------------------------------------+
| **Scenario**                 | **Linked List**                                    | **Array**                                           |
+==============================+====================================================+=====================================================+
| **Dynamic Resizing**         | Efficient (no reallocation required).              | Requires creating a new array and copying elements. |
+------------------------------+----------------------------------------------------+-----------------------------------------------------+
| **Random Access**            | Inefficient (:math:`O(n)` traversal).              | Efficient (:math:`O(1)` via indexing).              |
+------------------------------+----------------------------------------------------+-----------------------------------------------------+
| **Insert/Delete at Head**    | Efficient (:math:`O(1)`).                          | Inefficient (:math:`O(n)` for shifting).            |
+------------------------------+----------------------------------------------------+-----------------------------------------------------+
| **Insert/Delete at Tail**    | Inefficient (:math:`O(n)` unless tail is tracked). | Efficient (:math:`O(1)`).                           |
+------------------------------+----------------------------------------------------+-----------------------------------------------------+
| **Memory Usage**             | Higher (extra pointer per node).                   | Lower (contiguous memory storage).                  |
+------------------------------+----------------------------------------------------+-----------------------------------------------------+

----------------------------

Examples and Use Cases
======================

Example 1: Implementing a Stack
-------------------------------
A stack can be easily implemented using a linked list, where the **head** represents the top of the stack. 

- **Push**: Use ``prepend`` to insert an element at the head.
- **Pop**: Remove the head element using a deletion method.

.. code-block:: python

    class Stack(Generic[T]):
        def __init__(self) -> None:
            self.stack = LinkedList[T]()

        def push(self, val: T) -> None:
            self.stack.prepend(val)

        def pop(self) -> Optional[T]:
            if not self.stack.head:
                return None
            val = self.stack.head.val
            self.stack.delete_at_position(0)
            return val


------------

Example 2: Detecting a Cycle in a Linked List
---------------------------------------------

This is a common interview problem where we determine if a linked list contains a cycle using the **Floyd’s Cycle Detection Algorithm** (a two-pointer approach).

.. code-block:: python

    def has_cycle(head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False


Example 3: Reversing a Linked List
----------------------------------
Reversing a linked list in-place is a classic interview question, implemented as the ``reverse`` method in our ``LinkedList`` class.


Example 4: Implementing a Queue
-------------------------------
A queue can be implemented with a linked list by maintaining references to both the **head** and **tail**.

.. code-block:: python

    class Queue(Generic[T]):
        def __init__(self) -> None:
            self.queue = LinkedList[T]()

        def enqueue(self, val: T) -> None:
            self.queue.append(val)

        def dequeue(self) -> Optional[T]:
            if not self.queue.head:
                return None
            val = self.queue.head.val
            self.queue.delete_at_position(0)
            return val

Conclusion
==========
Linked lists are a foundational data structure in computer science, offering dynamic memory management and efficient insertion and deletion operations at the cost of slower element access. They shine in scenarios requiring frequent modifications to the beginning or middle of a collection, such as in stack or queue implementations.

However, the trade-offs linked lists present, such as higher memory usage and :math:`O(n)` access times, make them less suited for use cases requiring frequent random access. When memory overhead or contiguous storage is critical, arrays or other data structures like hash tables may be better choices.

Strengths of Linked Lists
-------------------------
- **Dynamic Size**: No need to predefine the size, unlike arrays.
- **Efficient Modifications**: :math:`O(1)` insertion and deletion at the head.
- **Flexible Memory Usage**: Nodes allocated on the heap eliminate the requirement for contiguous memory.

Limitations of Linked Lists
---------------------------
- **Sequential Access**: Accessing an element by index requires traversal, resulting in :math:`O(n)` complexity.
- **Higher Memory Overhead**: Each node carries an additional pointer, consuming more memory than arrays.
- **Performance Trade-offs**: Traversal and operations like reversing are slower compared to array operations.

Further Exploration
-------------------
For more complex scenarios, variations of the singly linked list can be considered:

- **Doubly Linked List**: Each node contains two pointers—one to the next node and another to the previous node—enabling bidirectional traversal at the cost of increased memory usage.
- **Circular Linked List**: The tail node points back to the head, forming a circular structure. This is particularly useful in applications like round-robin schedulers.


Linked lists remain a cornerstone of data structure education and practical use. Their adaptability and simplicity make them a critical tool for developers, especially in interviews and algorithmic problem-solving. As you gain confidence with linked lists, exploring these variations will further enhance your understanding and broaden your toolkit.
