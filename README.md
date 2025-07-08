# Tower-of-Hanoi

Introduction

The parts we’ll divide and the topics we’ll discuss in this report are as follows, firstly introduction starts with giving a brief outline of the topics that’ll be covered in each part, secondly after the outline is done, we now focus on the problem at hand in order to have a better understanding of the topic and what is asked of us with a slight history of the given problem. Once we finish the introduction, we move onto what is asked of us regarding this problem. Which are the implementations of recursive and iterative algorithms to solve this problem. Starting with the recursive algorithm, we first talk about what a recursive algorithm is, when can it be used, how it can be implemented and ultimately how can we use it to solve a Tower of Hanoi problem. We also give our recursive algorithm in this part. Next, we move onto the iterative algorithm, like the previous algorithm we start by talking about what an iterative algorithm is, when can it be used, how it can be implemented and yet again our goal which is to implement it for a Tower of Hanoi problem. Once we’ve created these algorithms that can effectively solve a Tower of Hanoi problem both recursively and iteratively now, we move onto making it accessible to general users. Which is done by creating a GUI is done and tested with its source code and proof given in this report, we move on to the next part which is a performance evaluation. This is where we check and compare their performance in terms of time complexity and efficiency. In the last part we write our conclusion and give our concluding remarks.

The Tower of Hanoi is a classic problem for computer science and mathematics. It has been called many names from the problem of Benares Temple or Tower of Brahma, but its most popular name is as we know it The Tower of Hanoi. The problem consists of 3 rods where disks can be stacked on top of each other and various number of disks where none are the same size. The puzzle always starts the same way, disks being stacked on top of each other in decreasing size, so the biggest disk is the one on the bottom while the smallest is the one top. The goal is to move this entire stack into another rod however there are rules that you need to follow. These rules are as given below:

1.	Only one disk may be moved at a time.

2.	Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.

3.	No disk may be placed on top of a disk that is smaller than it.
 
The problem was first invented and used by a French mathematician, Edouard Lucas, in the year 1883 and since its first invention it has become a fundamental concept in algorithm design and complexity analysis [1]. With such a fundamental concept as this one it wasn’t surprising to see that it was now a topic to myths and legends. Legends of ancient temples. These stories only helped more people to recognize the problem which ultimately made it more popular than ever. However, with all the myths and legends aside the importance of the Tower of Hanoi lies in its ability to demonstrate the principles of algorithmic design and efficiency in different approaches.
 
Definitions and Implementations of Recursive and Iterative Algorithms
 
·	Recursive Algorithm

A recursive algorithm can be defined as a method for problem solving where it is needed to divide the problem into smaller sub-problems to help solve them. So, a recursive algorithm can be defined as an algorithm that calls to itself with subsets of the original problem that are getting gradually smaller until it reaches a base case. A base case is where the problem is simple enough to be solved directly. In this case the recursive solution to the Tower of Hanoi problem follows the same divide-and-conquer strategy. It breaks the problem down into smaller subproblems until a base case is reached. The recursive algorithm involves three main steps: moving n-1 disks from the source peg to the auxiliary peg, moving the nth disk from the source peg to the destination peg, and finally, moving the n-1 disks from the auxiliary peg to the destination peg.

·	Iterative Algorithm

An iterative algorithm unlike the recursive one uses a different approach, avoiding the use of recursion. It can be defined as a method for problem solving where a loop must be employed in order to solve the problem. So, it can be said that an iterative algorithm is an algorithm that repeatedly applies a series of steps with the use of repetitive constructs like loops to reach a conclusion for a problem. In this case the iterative solution to The Tower of Hanoi problem follows the same strategy. It employs a loop to simulate the recursive steps iteratively. The key is to emulate the recursive calls using a stack or an explicit data structure to keep track of the state.

User Interface Design and Functionality

We have the algorithms to solve the problem however it is not enough. We need a place where we can use these algorithms and make them usable by anyone who wants to use it. This is achieved by making an easy to use and access interface that users can use and understand without having a software engineering background. Both algorithms are combined inside this GUI.
 
Performance Analysis and Comparison
 
A performance analysis involves measuring execution time for varying values of n. To do this analysis we have to look at the time and space complexity of recursive and iterative algorithms. For the recursive algorithm, the time complexity is T(n) = O(2n). For a single increase in problem size, the time required is double the previous one. The space complexity is O(n) for the recursive algorithm. The time complexity of the iterative algorithm is O(2n). When we look at the time complexities, we can see that the time complexities are the same because the basic idea and logic are the same. On the other hand, the space complexity of the iterative algorithm is O(2n). This is due to the stack size. The same number of steps are required to solve this problem with both algorithms. The minimum number of moves required to solve the Tower of Hanoi problem with n disks is 2n - 1.

When we use recursive algorithm, the space complexity of the Tower of Hanoi problem is O(n); where n is the number of disks. Therefore, it is more advantageous in terms of performance to use a recursive algorithm to solve the problem instead of an iterative algorithm that takes up O(2^n) space.
