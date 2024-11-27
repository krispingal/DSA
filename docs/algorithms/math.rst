====
Math
====

This section covers algorithms rooted in mathematical principles, designed to solve problems that rely on numeric computations or properties of numbers. Examples include calculating the factorial of a number, finding the nth prime number, and more.

While the direct applications of these algorithms might not always be obvious, they play a crucial role in powering a wide range of technologies. Many systems rely on math-based algorithms, often operating behind the scenes.


Algorithms
==========

Fibonacci
---------
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It is defined as:

.. math::
    F(n) = F(n-1) + F(n-2), \quad \text{with } F(0) = 0 \text{ and } F(1) = 1

This sequence appears in various domains, including mathematics, computer science, biology, and art. In this section, we provide two implementations for calculating the nth Fibonacci number:

1. A **recursive implementation** using caching to avoid redundant computations.
2. An **iterative implementation** optimized for performance.

Recursive Implementation
^^^^^^^^^^^^^^^^^^^^^^^^

The recursive approach leverages Python's `functools.cache` to store previously computed values, 
reducing the time complexity to :math:`O(n)` while keeping the simplicity of a recursive definition.

.. autofunction:: dsa.algorithms.math.nth_fibonacci_recursive

**Example Usage:**

.. code-block:: python

    from dsa.algorithms.math import nth_fibonacci_recursive

    print(nth_fibonacci_recursive(10))  # Output: 55

**Advantages:**
- Simplicity: The implementation closely follows the mathematical definition of Fibonacci.
- Efficient: The `cache` decorator ensures that previously computed values are reused, significantly improving performance compared to a naive recursive approach.

**Limitations:**
- Memory Usage: Caching can consume more memory, especially for large inputs.
- Recursion Limit: Python's recursion depth limit may cause issues with very large :math:`n`.

------------------------

Iterative Implementation
^^^^^^^^^^^^^^^^^^^^^^^^

The iterative approach uses two variables to keep track of the previous two Fibonacci numbers. 
It avoids recursion entirely, making it both space and time-efficient :math:`O(n)`.

.. autofunction:: dsa.algorithms.math.nth_fibonacci_iterative

**Example Usage:**

.. code-block:: python

    from dsa.algorithms.math import nth_fibonacci_iterative

    print(nth_fibonacci_iterative(10))  # Output: 55

**Advantages:**
- Space Efficiency: The implementation uses constant space :math:`O(1)`.
- No Recursion Limit: Suitable for very large :math:`n`.

**Limitations:**
- Complexity: Slightly harder to understand compared to the recursive approach for beginners.

------------------------------

Comparing Recursive and Iterative Implementations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The table below highlights the differences between the two approaches:

+---------------------+---------------------------+------------------------+
| **Feature**         | **Recursive**             | **Iterative**          |
+=====================+===========================+========================+
| **Time Complexity** | :math:`O(n)` with caching | :math:`O(n)`           |
+---------------------+---------------------------+------------------------+
| **Space Complexity**| :math:`O(n)` (cache)      | :math:`O(1)`           |
+---------------------+---------------------------+------------------------+
| **Ease of Use**     | Intuitive, matches        | Less intuitive, but    |
|                     | mathematical formula      | efficient              |
+---------------------+---------------------------+------------------------+

---------------------------

API Reference
^^^^^^^^^^^^^

For detailed implementation and parameters, see the API reference for:
- :func:`nth_fibonacci_recursive <dsa.algorithms.math.nth_fibonacci_recursive>`
- :func:`nth_fibonacci_iterative <dsa.algorithms.math.nth_fibonacci_iterative>`

Power Function
--------------
Overview
^^^^^^^^

The power function, commonly represented as :math:`a^b`, computes the result of raising a base aa to an exponent :math:`\text{b}`. 
While this is a standard operation in most programming languages, understanding the mechanics behind efficient computation can be valuable. Exponentiation by squaring is one such technique, enabling rapid computation of powers, even for very large exponents.

Why learn this? Many high-level libraries internally use optimized approaches like this, and understanding these methods can help you:

- Improve performance for custom implementations.
- Optimize computations in low-level or resource-constrained systems.
- Solve mathematical problems requiring efficient power calculations.

Recursive Definition of Exponentiation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exponentiation can be defined recursively as:

.. math::
    \begin{equation}
        a^{b} = 
        \begin{cases} 
            1 & \text{if} b = 0 \\
            a \cdot a^{b-1} & \text{if} b > 0
        \end{cases}
    \end{equation}

However, this approach results in :math:`O(\text{b})` time complexity, which is inefficient for large :math:`\text{b}`. 
Exponentiation by squaring, in contrast, reduces the time complexity to :math:`O(\log b)`, making it significantly faster.

Fast Exponentiation: Iterative Approach
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The iterative approach to exponentiation by squaring works by breaking down the problem into smaller sub-problems and leveraging properties of exponents:

.. math::
    \begin{equation}
        a^b = 
        \begin{cases}
            (a^2)^{b/2} & \text{if b is even} \\
            a \cdot (a^2)^{(b-1)/2} & \text{if b is odd}
        \end{cases}
    \end{equation}


Prime Sieve
-----------
The **Sieve of Eratosthenes** is a well-known algorithm for generating all prime numbers up to a given limit. It works by iteratively marking the multiples of each prime number, starting from 2. Prime sieves are foundational in fields like cryptography and number theory.

Real-World Applications
========================

Mathematical algorithms are foundational to many domains, including cryptography, computer graphics, and high-performance systems. Mastering these algorithms provides tools for problem-solving and optimization in diverse areas.

Computer Graphics
-----------------
Modern game engines and animation tools model real-world phenomena such as light reflection and refraction. These simulations rely heavily on mathematical models and computations, enabling realistic rendering in games and movies. Physics engines perform millions of computations per second to achieve this level of detail.

Software Engineering
--------------------
In systems handling high traffic, approximate algorithms like **HyperLogLog** provide efficient ways to estimate metrics, such as the number of unique visitors, without consuming excessive memory or processing power.

In high-performance systems, sampling techniques are used to log events selectively, reducing overhead while retaining sufficient data for analysis.
