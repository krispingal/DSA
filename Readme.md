Data structures and algorithms
==============================
![build passing](https://github.com/krispingal/DSA/actions/workflows/python-build.yml/badge.svg?event=push)

This repo hosts a collection of data structures and algorithms implemented 
to help me build a mental model on how these work under the hood.

## Usage
Clone the git package, install all the dependencies by running the below:
```
pip install .
# to install test dependencies
pip install .[test]
# to install test dependencies in zsh run
pip install -e '.[test]'
```

to run all the test cases run `python -m pytest`.

## Data structures
1. Binary tree
2. Disjoint Sets Union
3. Doubly linked list
2. Heap (Max heap)
1. Linked list
2. Priority Queue (Max priority queue)
1. Queue
1. Stack (implemented using arrays and linked list)
1. Segment tree
1. Trie (implemented using arrays and linked list)

## Algorithms
1. Binary search
1. Kadane's algorithm to find maximum sub array sum
1. Prime sieve - sieve of eratosthenes
1. Dijkstra's algorithm - single source shortest path problem (Using priority queue)
1. Floyd-Warshall - all pairs shortest path
1. Pow - Fast exponentiation

### Sort
1. Bubble sort
2. Merge sort
3. Quick sort (3 variants - Lomuto, Hoare, and Randomized)
4. Insertion sort
5. Heap sort
6. Bucket sort

## Rate limit algorithms
1. Token bucket
1. Fixed window
1. Sliding window log

## Sort performance test results
**Bubble sort** completion time for array size: 10_000 1.19851s

**Insertion sort** completion time for array size: 10_000 0.02462s

**Heap sort** completion time for array size: 10_000 0.04350s

**Merge sort** completion time for array size: **10_000 0.01272s**

**Quick sort** QuicksortAlgorithm.RANDOMIZED partition algo completion time for array size: 10_000 0.01039s

Quicksort Lomuto and Hoare partition code fails due to Recursion error hitting, for this size of the array.
