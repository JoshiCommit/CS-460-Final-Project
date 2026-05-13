# The Torchbearer

**Student Name:** Deepanshu Joshi
**Student ID:** 827985022
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  - The reason that a single shortest-path run from S is not sufficient is due to the fact that this will only give you the shortest path from the enterance to S. 
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
| Enterance node | This is the starting point for the route so we need Dijkstra to get the cheapest cost from enterance to each relic |
| Relic Chamber node | After reaching a relic Dijkstra is needed to travel to the next relic |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | |
| What the keys represent | |
| What the values represent | |
| Lookup time complexity | |
| Why O(1) lookup is possible | |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _your answer_
- **Cost per run:** _your answer_
- **Total complexity:** _your answer_
- **Justification (one line):** _your answer_

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  - Current distance is for sure the shortest distance to the node meaning that their values are set in stone

- **For nodes not yet finalized (not in S):**
  - Current distance is the shortest known distance using a path that goes through nodes who are already finalized

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

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

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

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

- _Your references here._
