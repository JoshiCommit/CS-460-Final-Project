# Development Log – The Torchbearer

**Student Name:** Deepanshu Joshi
**Student ID:** 827985022

---

## Entry 1 – [5/12]: Initial Plan

I plan on first going through the README.md file and completing it completely. I think this will give me a better base than doing the README.md and torchbearer.py files at the same time since I will be able to see the whole overview of the program and understand the process well. I expect the hardest part of the program to be just making sure that the route is as optimal as possible. I think there might be a point where my algorithm is able to find the optimal route but it will not classify the route as the most optimal. I will test using the provided test cases

---

## Entry 2 – [5/13]: [Short description]

Working on the coding for Dijkstra's algorithm and I forgot about the neighbors the first time I implemented. After some digging around I realized that i was not actually getting all the needed nodes and was able to fix the problem. Fixed by just accounting for the neighbor nodes and adding them intot he set.

---

## Entry 3 – [Date]: [Short description]

Worked on backtrack for a period and it didn't go the best for a while. Relics were staying visted even though they weren't which was causing incorrect results.Also added pruning logic becuase I realized the second I find out a route is more expensive than the last I can end execution there instead of looking at the whole route.

---

## Entry 4 – [5/14]: Post-Implementation Reflection

After completing the assignment I can say with full confidence that _explore was the hardest. If I had more time to work on this assignment I would make the searches a little more optimal than the currently are. I think the biggest problem I faced was doing a lot of the assignment at once and then taking a big break until right before it was due.

---

## Final Entry – [5/14]: Time Estimate
## PART TIME ESTIMATES ARE JUST FOR THE README THE CODE IS ALL WITHIN IMPLEMENTATION

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 20 Minutes |
| Part 2: Precomputation Design | 1 Hour |
| Part 3: Algorithm Correctness | 30 Minutes |
| Part 4: Search Design | 45 Minutes |
| Part 5: State and Search Space | 30 Minutes |
| Part 6: Pruning | 1 Hour |
| Part 7: Implementation | 6 Hours |
| README and DEVLOG writing | 4 Hours |
| **Total** | About 14 Hours|
