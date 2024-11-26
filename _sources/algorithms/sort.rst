==================
Sorting Algorithms
==================

Sorting algorithms are used to arrange elements in a specific order, such as ascending or descending. These algorithms work on arrays, lists, and other collections, where elements must be comparable (e.g., implement a ``comparator function``). After sorting, all elements in the collection are in their correct order.

Sorting is a common task in everyday life. Examples include:

1. Organizing bills or currency notes in your wallet.
2. Arranging a deck of cards.
3. Schools or universities managing attendance sheets sorted by name or student ID.

When the size of a collection is small, most sorting algorithms can complete the task in a similar time frame. 
However, as the size of the collection grows (e.g., from 100 to 1,000,000 elements), the performance of these 
algorithms may vary significantly. Understanding their **time complexity**, **space complexity**, and whether 
they are **stable** algorithms is essential for choosing the right algorithm.

Sorting in Python
-----------------

Python provides built-in functionality for sorting lists, making it easy to use. Here are two examples:

Using the ``list.sort`` method, suppose you want to send out a list of invites to your birthday/farewell party:

.. code-block:: python

    >>> invite_list = ['Sam', 'Pippin', 'Aragorn', 'Gimli', 'Legolas', 'Galadriel', 'Faramir', 'Eowyn']
    >>> invite_list.sort()
    >>> print(invite_list)
    ['Aragorn', 'Eowyn', 'Faramir', 'Galadriel', 'Gimli', 'Legolas', 'Pippin', 'Sam']

Using the `sorted` function (returns a new sorted list):

.. code-block:: python

    >>> invite_list = ['Sam', 'Pippin', 'Aragorn', 'Gimli', 'Legolas', 'Galadriel', 'Faramir', 'Eowyn']
    >>> print(sorted(invite_list))
    ['Aragorn', 'Eowyn', 'Faramir', 'Galadriel', 'Gimli', 'Legolas', 'Pippin', 'Sam']

Now lets look into some algorithms and how they can be implemented.

Algorithms
==========

This library includes the following sorting algorithms:

- **Bubble Sort**: A simple algorithm that repeatedly swaps adjacent elements if they are in the wrong order.
- **Bucket Sort**: Divides elements into buckets and sorts each bucket individually (useful for uniformly distributed data).
- **Heap Sort**: A comparison-based algorithm that uses a binary heap data structure.
- **Insertion Sort**: Builds the sorted list one element at a time by inserting elements into their correct position.
- **Merge Sort**: A divide-and-conquer algorithm that splits the collection into smaller parts, sorts them, and merges them back together.
- **Quick Sort**: A highly efficient divide-and-conquer algorithm that partitions the collection around a pivot.
- **Selection Sort**: Repeatedly selects the smallest element and moves it to its correct position.
