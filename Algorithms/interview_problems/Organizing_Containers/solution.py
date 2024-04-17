def organizingContainers(container):
    n = len(container)  # Number of containers and types

    # Calculate the total number of balls in each container
    container_capacities = [sum(container[i]) for i in range(n)]

    # Calculate the total number of each type of balls
    type_demands = [0] * n
    for i in range(n):
        for j in range(n):
            type_demands[j] += container[i][j]

    # Sort both lists to compare them directly
    container_capacities.sort()
    type_demands.sort()

    # Compare if both lists (multisets) are the same
    if container_capacities == type_demands:
        return "Possible"
    else:
        return "Impossible"
    
