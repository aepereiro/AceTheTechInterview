# Organizing Containers of Balls

## Problem Statement

David has several containers, each filled with different types of balls. The goal is to sort the balls in such a way that each container holds balls of only one type, and no two balls of the same type are located in different containers. However, David can only perform swap operations between different containers to achieve this.

### Task

Determine whether it is possible for David to organize the balls according to the rules using a given initial setup. For each query which represents an initial setup, return "Possible" if the balls can be organized as described, otherwise return "Impossible".

## Function Description

Complete the function `organizingContainers` which has the following parameters:

- `int container[n][m]`: A two-dimensional array of integers representing the number of balls of each color in each container.

The function should return either "Possible" or "Impossible".

## Input Format

- The first line contains an integer `q`, the number of queries.
- The first line of each query contains an integer `n`, the number of containers (and also the number of different ball types).
- Each of the next `n` lines contains `n` space-separated integers describing the rows of the matrix.

## Constraints

- Each container and each type is numbered from 1 to `n`.
- All input times are valid.

## Output Format

For each query, print "Possible" on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print "Impossible".

## Sample Input

    ```
    2
    2
    1 1
    1 1
    2
    0 2
    1 1
    ```

## Sample Output

    ```
    Possible
    Impossible
    ```

## Explanation

In the first query, the setup already meets the conditions. In the second query, no matter how many times balls are swapped between the two containers, one container will always contain different types of balls.

## How to Run

You can run the function with a set of queries and observe the output:

    ```
    queries = [
        [[1, 1], [1, 1]],  # First query
        [[0, 2], [1, 1]]   # Second query
    ]

    results = [organizingContainers(q) for q in queries]
    for result in results:
        print(result)
    ```

## Discussion

The primary challenge is to determine whether each container's total capacity matches exactly with the demand for any single type of ball, considering the constraints and the allowed operations (swaps). This problem is approached by analyzing and matching the total counts per container and per type.
