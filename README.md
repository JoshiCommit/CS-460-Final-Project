# The Torchbearer

**Student Name:** Deepanshu Joshi
**Student ID:** 827985022
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  - The reason that a single shortest-path run from S is not sufficient is due to the fact that this will only give you the shortest path from the entrance to S. 
  - This isn't all that the problem is asking however we also need to find what order the relic chambers need to be visited which a single shortest-path run from S will not be able to suffice.

- **What decision remains after all inter-location costs are known:**
  - The structural decision that remains after the iner-locational travel costs are known is what order to visit the relic chambers in.

- **Why this requires a search over orders (one sentence):**
  - Since relic order needs to be determined and this can make different total fuel costs we need a search over order to find a efficient visit order instead of a single computation givign shortest path from A - B.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| Entrance node | This is the starting point for the route so we need Dijkstra to get the cheapest cost from entrance to each relic and exit |
| Relic Chamber node | After reaching a relic Dijkstra is needed to travel to the next relic |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | Dictionary of dictionaries|
| What the keys represent | Keys represent the source node and the destination node|
| What the values represent | Minimum fuel cost from source node to the specific node |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Hashing allows for O(1) averages |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** 
  - k + 1
  - k is the number of relics
  - Running from S once and from each relic once
- **Cost per run:**
  - ASSIGNMENT.md states "Single shortest-path run costs O(m log n)."
  - Keeping in mind Let n = |V|, m = |E|, k = |M|
- **Total complexity:** 
  - O(k + 1) * O(m log n)
  - O((k + 1) m log n)
- **Justification (one line):**
  - We know that Dijkstra has to run once from the source till a relic and then from each relic, with each run costing O(m log n)

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  - Current distance is for sure the shortest distance to the node meaning that their values are set in stone

- **For nodes not yet finalized (not in S):**
  - Current distance is the shortest known distance using a path that goes through nodes who are already finalized

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  - All nodes are undiscovered at this point meaning that their distances are set to infiity and only the starting point is known which is given to have a distance of 0 meaning that there is no incorrect distances.

- **Maintenance : why finalizing the min-dist node is always correct:**
  - Since the algorithm will pick the node with the shortest distance and all edge weights are nonnegative meaning distance cannot possibly get shorter more efficient paths cannot be found to the node.

- **Termination : what the invariant guarantees when the algorithm ends:**
  - By the end all nodes which are reachable will have the shortest distances mapped out and all nodes unreachable will have a distance of infinity

### Part 3c: Why This Matters for the Route Planner
 - If the distances are off then there is a high chance that the algorithm might choose a route that isn't as optimal as it could be which leads to burning more fuel than needed.

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** 
  - Greedy just picks the closest relic not looking at the possibility of the future and looking at how it might be more efficient to pick another relic in the long run
- **Counter-example setup:** 
  - S connects to A with cost 1 and B with cost 2
  - A connects to B with cost 10 and T with cost 1
  - B connects to A with cost 1 and T with 1
  - Important to note there is no way to access anything from T
- **What greedy picks:** 
  -  Greedy will pick S -> A -> B -> T
  - This results in a cost of 12 since there is no way for T to access B going T -> B
- **What optimal picks:** 
  - Optimal will pick S -> B -> A -> T
  - Because it is able to see the cost of 10 ahead it makes a more optimal choice having a cost of 4
- **Why greedy loses:** 
  - While choosing the closest relic seems like a good idea it can lead to a path that is worse overall since it does not account for future costs and only looks at the next relic cost

### What the Algorithm Must Explore

- The algorithm has to look at different visiting orders for relics to determine the order that uses the least total fuel

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | curr_loc | node | Node where torchbearer is currently |
| Relics already collected | relics_col | set | Storing which relics have already been collected |
| Fuel cost so far | fuel_curr | float | Total fuel cost so far |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | set |
| Operation: check if relic already collected | Time complexity: O(1)|
| Operation: mark a relic as collected | Time complexity: O(1)|
| Operation: unmark a relic (backtrack) | Time complexity: O(1)|
| Why this structure fits | Set allows you to easily check if a relic has already been collected or not, also has the add and remove operations needed for backtracking|

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** 
  - k!
- **Why:** 
  - Algorithm has to rearch through every single combination of reaching the relics

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- Lecture Notes used for basically the whole assignment
- ChatGPT used to find out how to use GitHub
- Abdul Bari Dijkstra Algorithm video https://www.youtube.com/watch?v=XB4MIexjvY0&t=981s&pp=ygUVZGlqa3N0cmEgYWxnb3JpdG1hc8Sx used to gain an understanding of Dijkstra's algorithm for Part 2 onwards verified with Geeks for Geeks and Lecture Notes
- Geeks for Geeks Dijkstra's Algorithm article https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/ used to gain an understanding of Dijkstra's algorithm for Part 2 onwards verified with Abdul Bari's YouTube video.
