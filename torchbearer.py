"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Deepanshu Joshi
Student ID:   827985022

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    return(
        "The reason that a single shortest-path run from S is not sufficient is due to the fact that this will only give you the shortest path from the entrance to other nodes. This isn't all that the problem is asking however we also need to find what order the relic chambers need to be visited which a single shortest-path run from S will not be able to suffice. The structural decision that remains after the iner-locational travel costs are known is what order to visit the relic chambers in. Since relic order needs to be determined and this can make different total fuel costs we need a search over order to find a efficient visit order instead of a single computation giving shortest path from A - B."
    )

# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    # Combining spawn node with relic node but getting rid of duplicates
    return list(dict.fromkeys([spawn] + relics))


def run_dijkstra(graph, source):
    # Storing nodes in graph
    nodes = set(graph.keys())

    # Adding neighbor nodes that might not show up
    for node in graph:
        for neighbor, cost in graph[node]:
            node.add(neighbor)

    # Put all distances to default value of infinity
    distances = {}
    for node in nodes:
        distances[node] = float("inf")

    # All distanses other than source unknown
    distances[source] = 0

    # Priority queue to store distance per node
    distpq = []

    heapq.heappush(distpq, (0, source))

    while distpq:
        # Node with smallest distance so far
        curr_dist, curr_node = heapq.heappop(distpq)
        # Making sure to skip and queue entries that are outdated
        if curr_dist != distances[curr_node]:
            continue
        # Explore nodes connected to the current node
        for neighbor, cost in graph.get(curr_node, []):
            # Find the distance
            new_dist = curr_dist + cost
            # Check if new distance is shorter
            if new_dist < distances[neighbor]:
                # Set new distance as shortest distance
                distances[neighbor] = new_dist
                heapq.heappush(distpq, (new_dist, neighbor))
    return distances


def precompute_distances(graph, spawn, relics, exit_node):
    # Get source nodes
    source_nodes = select_sources(spawn, relics, exit_node)
    dist_table = {}
    # Running dijkstra
    for source in source_nodes:
        dist_table[source] = run_dijkstra(graph, source)
    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    return(
        "Current distance is for sure the shortest distance to the node meaning that their values are set in stone, Current distance is the shortest known distance using a path that goes through nodes who are already finalized. All nodes are undiscovered at this point meaning that their distances are set to infiity and only the starting point is known which is given to have a distance of 0 meaning that there is no incorrect distances. Since the algorithm will pick the node with the shortest distance and all edge weights are nonnegative meaning distance cannot possibly get shorter more efficient paths cannot be found to the node. By the end all nodes which are reachable will have the shortest distances mapped out and all nodes unreachable will have a distance of infinity. If the distances are off then there is a high chance that the algorithm might choose a route that isn't as optimal as it could be which leads to burning more fuel than needed."
    )


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    return(
        "S connects to A with cost 1 and B with cost 2, A connects to B with cost 10 and T with cost 1, B connects to A with cost 1 and T with 1, Important to note there is no way to access anything from T. Greedy will pick S -> A -> B -> T. This results in a cost of 12 since there is no way for T to access B going T -> B. Optimal will pick S -> B -> A -> T. Because it is able to see the cost of 10 ahead it makes a more optimal choice having a cost of 4. While choosing the closest relic seems like a good idea it can lead to a path that is worse overall since it does not account for future costs and only looks at the next relic cost. The algorithm has to look at different visiting orders for relics to determine the order that uses the least total fuel "
    )


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
