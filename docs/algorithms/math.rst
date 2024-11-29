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

- :func:`nth_fibonacci_recursive <dsa.algorithms.math.fibonacci.nth_fibonacci_recursive>`
- :func:`nth_fibonacci_iterative <dsa.algorithms.math.fibonacci.nth_fibonacci_iterative>`

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


API Reference
^^^^^^^^^^^^^

For detailed implementation and parameters, see the API reference for:

- :func:`fast_exponentiation <dsa.algorithms.math.pow.fast_exponentiation>`

----------------

Prime Sieve
-----------
The **Sieve of Eratosthenes** is a classical algorithm for finding all prime numbers up to a 
given number :math:`n`. It is simple yet efficient, leveraging the principle of marking 
non-prime numbers (multiples of primes) in a boolean array. The algorithm runs with a time 
complexity of :math:`O(n \log \log n)`, making it well-suited for moderate-sized values of :math:`n`.

Problem Statement
^^^^^^^^^^^^^^^^^
Given an integer :math:`n \geq 2`, determine all prime numbers less than or equal to :math:`n`.

Key Concepts
^^^^^^^^^^^^
- **Primes**: Numbers greater than 1 that are divisible only by 1 and themselves.
- **Marking Multiples**: Starting from the first prime number :math:`p = 2`, mark all multiples of :math:`p = 2` as non-prime. Repeat this process for the next unmarked number in the list.

Algorithm
^^^^^^^^^
1. Create a boolean array of size :math:`n - 1`, initialized to ``True`` (representing potential primes).
2. Starting from 2, iterate through the array:
   - If a number is still marked as ``True``, it is a prime number.
   - Mark all multiples of this prime as ``False`` (non-prime).
3. Collect all indices still marked as ``True`` — these are the prime numbers.

Implementation
^^^^^^^^^^^^^^
Here’s the Python implementation of the Sieve of Eratosthenes:

.. code-block:: python

    def eratosthenes_sieve(n: int) -> list[int]:
        """
        Computes all prime numbers up to a given limit using the Sieve of Eratosthenes.

        Args:
            n (int): The upper limit (inclusive) for prime number calculation. Must be >= 2.

        Returns:
            list[int]: A list of primes from 2 to `n`.

        Raises:
            ValueError: If `n` is less than 2.
        """
        if n < 2:
            raise ValueError("The sieve requires n >= 2.")
        
        A = [1] * (n - 1)  # Sieve array for numbers 2 to n
        res = []
        for i in range(2, n + 1):
            if A[i - 2]:
                res.append(i)
                for j in range(i * i, n + 1, i):
                    A[j - 2] = 0
        return res

Example Usage
^^^^^^^^^^^^^
To find all prime numbers up to 10:

.. code-block:: python

    >>> primes = eratosthenes_sieve(10)
    >>> print(primes)
    [2, 3, 5, 7]



Real-World Applications
^^^^^^^^^^^^^^^^^^^^^^^
1. **Cryptography**: Prime numbers are integral to encryption algorithms like RSA.
2. **Number Theory**: Used in mathematical proofs and research.
3. **Random Number Generation**: Finding prime numbers to create secure seeds.


Notes on Performance
^^^^^^^^^^^^^^^^^^^^
- **Time Complexity**: :math:`O(n \log \log n)`
- **Space Complexity**: :math:`O(n)` for the sieve array.

Caveats
^^^^^^^
- The memory usage grows linearly with :math:`n`, making this approach less feasible for very large upper limits.

References
^^^^^^^^^^
- `Sieve of Eratosthenes on Wikipedia <https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes>`_
- `Sieve of Eratosthenes on YouTube - Khan Academy <https://www.youtube.com/watch?v=klcIklsWzrY>`_

API Reference
^^^^^^^^^^^^^

For detailed implementation and parameters, see the API reference for:

- :func:`eratosthenes_sieve <dsa.algorithms.prime_sieve.eratosthenes_sieve>`

-----------------------


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
