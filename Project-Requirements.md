# CS 3364 Design and Analysis of Algorithms
Project: DUE May 5th, 2024
## Task 1-Packing for the Trip (Knapsack Problem) 50 Points
### Background
Assume we are in the year 3089, intergalactic travel has become a reality. As a travel
planner for ”Galaxy Getaways,” you are tasked with planning a grand tour for a group
of space tourists. Your challenges include for the trip ensuring that tourists get the best
experiences within their luggage constraints.

**Scenario**:
Planet Xanadu offers various unique experiences, each requiring different equipment.
Tourists need to maximize their experiences while adhering to their luggage weight re
strictions.

**Experiences and Equipment**:

| Experience ID | Weight (kg) | Value (Enjoyment Points) |
|:-------------:|:-----------:|:------------------------:|
|       1       |      4      |           500            |
|       2       |      5      |           600            |
|       3       |      6      |           700            |
|       4       |      7      |           800            |
|       5       |      8      |           1000           |

 **Luggage Weight Limit**: W = 20 kg

**Tasks**:
1. **State Definition (10 Points)**: Define the sub-problems in terms of maximizing the total enjoyment points without exceeding the luggage weight limit.
2. **Recurrence Relation (10 Points)**: Develop the recurrence relation for the knap sack problem given the weights and values of the experiences.
3. **Implementation (20 Points)**: Propose a dynamic programming solution to calculate the maximum enjoyment points achievable within the weight constraint.
4. **Analysis (10 Points)**: Detail which experiences were chosen for the optimal solution and provide a rationale for your selections.

**Remember, the primary goal of this task is to demonstrate your understanding of dynamic programming, specifically Knapsack problems. Focus on clarity, logical flow, and thoroughness in your solutions.**

### Analysis and Justificaiton 
* For each problem, provide a step-by-step breakdown of your approach before diving into the solution.
* Clearly explain the state definitions and recurrence relations. Diagrams or tables can be used for illustration.
* After presenting your solution, provide an analysis of the results, including the optimal choices and their justifications. For the bonus section, ensure you provide a clear and logical scenario and a strategy to tackle the combined challenge.

## Task 2: Implementation of Prim’s and Kruskal’s algorithm
To implement Prim’s and Kruskal’s algorithms for finding Minimum Spanning Trees (MSTs) in a given graph, and to analyze and compare the performance of these algorithms under different conditions.
Prerequisites– Basic knowledge of graph theory.– Proficiency in a programming language (e.g., Python, Java, C++).– Understanding of algorithm complexity and performance analysis.
Part 1: Implementation
 1. Implement Prim’s Algorithm as a function prim
 mst(graph).
 2. Implement Kruskal’s Algorithm as a function kruskal
 mst(graph).– Deliverable 1: Submit a well-documented source code package contain
ing two separate files: one for implementing Prim’s algorithm and another
 for Kruskal’s algorithm. Each file should include a clearly defined function,
 prim mst(graph) for Prim’s algorithm and kruskal mst(graph) for Kruskal’s
 algorithm. These functions should take a graph as input and return its mini
mum spanning tree (MST). The code must be well-commented to explain the
 logic, and the graph input can be in the form of an adjacency list or matrix,
 as preferred.
 Part 2: Testing and Validation
 1. Create at least three different graphs to test your algorithms. These should
 include:
 ∗ Asparse graph with 10-15 nodes.
 ∗ Adense graph with 10-15 nodes.
 2
∗ Agraph with varying edge weights, including negative weights, if your
 implementation allows
 2. Record and analyze the output of each algorithm on these graphs.
 ∗ Run both algorithms on each of the graphs.
 ∗ Record the output MSTs and their total weights.– Deliverable 2: Provide a comprehensive testing document that includes de
tailed descriptions and results of at least three different graph test cases used
 to validate both algorithms. These graphs should represent a variety of types,
 including a sparse graph, a dense graph, and a graph with varied edge weights.
 For each test case, the document should clearly present the input graph, the
 MSTs obtained from both Prim’s and Kruskal’s algorithms, and a summary
 of the total weight of each MST. This will demonstrate the correctness and
 functionality of your implementations.
 Part 3: Analysis
 ∗ Analyze the performance of both algorithms on each graph.
 ∗ Discuss the time complexity in the best, average, and worst-case scenarios
 for each algorithm.– Deliverable 3: The third part requires a detailed analytical report. This
 report should include a thorough performance analysis comparing Prim’s and
 Kruskal’s algorithms, focusing on time complexity in various scenarios (e.g.,
 best, average, and worst-case). Additionally, the report should feature a real
world application case study, demonstrating the practical use of MSTs and
 arguing which of the two algorithms would be more suitable for the specific
 scenario. The report should conclude with a comparative discussion of the two
 algorithms, drawing insights from both the theoretical aspects and the testing
 results.
 Part 4: Extra Credit (Optional)
 Implement a graphical user interface (GUI) where users can draw a graph and
 see the MST found by each algorithm.
 1 Evaluation Criteria– Correct implementation of algorithms(20 points).– Accuracy in testing and analysis(50 points).– Clarity and depth of the report (30 points).– Creativity and functionality (Optional: Extra credit (10 points)).
 3
Submission Requirements
 File Format
 • Submit your zip file containing your code as a well-formatted PDF document with
 screenshots and justification if any asked.
 Code Implementation
 • You may use Python, Java, C++, or any other major programming language.
 Clearly mention the language used.
 • Ensure that the code is properly indented and commented for clarity. Include brief
 explanations for major blocks or functions.
 • If external libraries or packages are used, mention them explicitly.
 2 Additional Resources
 Here’s a list of additional tools that can be used for this project:
 • Programming Languages: Python, Java, C++
 • Graph Theory Libraries: NetworkX (Python),JGraphT (Java), Boost Graph Li
brary (C++)
 • Integrated Development Environments (IDEs): PyCharm (for Python), Eclipse or
 IntelliJ IDEA (for Java), Visual Studio (for C++)
 • Graph Visualization Tools: Gephi,Graphviz
 • Algorithm Visualization Tools: Visualgo, AlgoViz