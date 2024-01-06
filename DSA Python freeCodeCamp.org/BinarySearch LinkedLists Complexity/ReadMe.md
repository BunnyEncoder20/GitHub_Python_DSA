## Problem 

In this notebook, we focus on solving the following problem:
> **QUESTION 1:** Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
<img src="https://i.imgur.com/mazym6s.png" width="480">

This may seem like a simple problem, especially if you're familiar with the concept of _binary search_, but the strategy and technique we learning here will be widely applicable, and we'll soon use it to solve harder problems.

---

## Why You Should Learn Data Structures and Algorithms

Whether you're pursuing a career in software development or data science, it's almost certain that you'll be asked to solve programming problems like *reversing a linked list* or *balancing a binary tree* in a technical interview or coding assessment.

It's well known, however, that you will almost never face these problems in your job as a software developer. So it's reasonable to wonder why such problems are asked in interviews and coding assessments. Solving programming problems demonstrates the following traits:

1. You can **think about a problem systematically** and solve it systematically step-by-step.
2. You can **envision different inputs, outputs, and edge cases** for programs you write.
3. You can **communicate your ideas clearly** to co-workers and incorporate their suggestions.
4. Most importantly, you can **convert your thoughts and ideas into working code** that's also readable.

It's not your knowledge of specific data structures or algorithms that's tested in an interview, but your approach towards the problem. You may fail to solve the problem and still clear the interview or vice versa. In this course, you will learn the skills to both solve problems and clear interviews successfully.

---

## The Method

Upon reading the problem, you may get some ideas on how to solve it and your first instinct might be to start writing code. This is not the optimal strategy and you may end up spending a longer time trying to solve the problem due to coding errors, or may not be able to solve it at all.

Here's a **systematic strategy** we'll apply for solving problems:

1. State the problem clearly. Identify the input & output formats.
2. Come up with some example inputs & outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem. State it in plain English.
4. Implement the solution and test it using example inputs. Fix bugs, if any.
5. Analyze the algorithm's complexity and identify inefficiencies, if any.
6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

_"Applying the right technique"_ is where the knowledge of common data structures and algorithms comes in handy. 

---

## Solution


### 1. State the problem clearly. Identify the input & output formats.

You will often encounter detailed word problems in coding challenges and interviews. The first step is to state the problem clearly and precisely in abstract terms. 

<img src="https://i.imgur.com/mazym6s.png" width="480">

In this case, for instance, we can represent the sequence of cards as a list of numbers. Turning over a specific card is equivalent to accessing the value of the number at the corresponding position the list. 

<img src="https://i.imgur.com/G9fBarb.png" width="600">

The problem can now be stated as follows:

#### Problem

> We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.

#### Input

1. `cards`: A list of numbers sorted in decreasing order. E.g. `[13, 11, 10, 7, 4, 3, 1, 0]`
2. `query`: A number, whose position in the array is to be determined. E.g. `7`

#### Output

3. `position`: The position of `query` in the list `cards`. E.g. `3` in the above case (counting from `0`)



Based on the above, we can now create the signature of our function:
```
def locate_card(cards, query) :
    pass
```
**Tips**:

* Name your function appropriately and think carefully about the signature
* Discuss the problem with the interviewer if you are unsure how to frame it in abstract terms
* Use descriptive variable names, otherwise you may forget what a variable represents

#### We'll represent our test cases as dictionaries to make it easier to test them once we write implement our function. For example, the above test case can be represented as follows:
```
test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}
```
The function can now be tested as follows : 
```
locate_card(**test['input']) == test['output']      // Note the **test['input'] the ** spread the args inside the input key of test dictionary to become the args of the function
```
---
Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible variations we might encounter:

1. The number `query` occurs somewhere in the middle of the list `cards`.
2. `query` is the first element in `cards`.
3. `query` is the last element in `cards`.
4. The list `cards` contains just one element, which is `query`.
5. The list `cards` does not contain number `query`.
6. The list `cards` is empty.
7. The list `cards` contains repeating numbers.
8. The number `query` occurs at more than one position in `cards`.
9. (can you think of any more variations?)

> **Edge Cases**: It's likely that you didn't think of all of the above cases when you read the problem for the first time. Some of these (like the empty array or `query` not occurring in `cards`) are called *edge cases*, as they represent rare or extreme examples. 

While edge cases may not occur frequently, your programs should be able to handle all edge cases, otherwise they may fail in unexpected ways. Let's create some more test cases for the variations listed above. We'll store all our test cases in an list for easier testing.