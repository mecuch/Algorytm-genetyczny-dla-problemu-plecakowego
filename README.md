# Knapsack Problem – Genetic Algorithm (Python)

## 1. Introduction and Architecture

The goal of this project is to implement a **genetic algorithm** for solving the classical **Knapsack Problem**.  
The problem consists in selecting a subset of items with given weights and values such that the total weight does not exceed the knapsack capacity while the total value is maximized.

The solution is implemented in **Python** using an **object-oriented approach**.  
The entire algorithm is encapsulated in a single class that stores both the problem data and the current state of the evolutionary process.

---

## 2. Class Structure

The core of the implementation is the `KnapsackProblemAG` class.  
It contains all data required to run the genetic algorithm as well as methods corresponding to individual evolutionary stages.

### Main class attributes

- `num_of_individ` – population size  
- `num_of_items` – number of available items  
- `weight_items` – list of item weights  
- `value_items` – list of item values  
- `load_capacity` – maximum allowed knapsack capacity  
- `population` – current population (list of individuals)  
- `max_stagnation` – maximum number of generations without improvement  
- `stop_numb`, `stop_stag` – flags defining the stopping criterion  

Each individual is represented as a **binary list**, where:

- `1` → item selected  
- `0` → item not selected  

---

## 3. Solution Representation

Each individual is represented as a binary vector of length equal to the number of items.

Example:


This means that items with indices `0`, `2`, and `4` are selected.

---

## 4. Handling Individuals Exceeding the Weight Limit

The algorithm uses a **penalty-based approach** to handle solutions that violate the weight constraint.

For each individual:

- total weight and total value are calculated,
- if the weight exceeds the allowed capacity, the fitness value is set to `0`,
- otherwise, the fitness value equals the sum of selected item values.

Invalid individuals are not physically removed from the population, but their zero fitness makes them extremely unlikely to be selected for reproduction.

---

## 5. Fitness Function and Selection

### 5.1 Fitness Function

The **fitness function** measures the quality of a solution.

- valid solutions are evaluated by the total value of selected items,
- invalid solutions receive a fitness value of `0`.

The fitness function **does not perform selection** — it only evaluates individuals.

---

### 5.2 Roulette Wheel Selection

The project uses **roulette wheel selection**, where the probability of selecting an individual is proportional to its fitness value.

Selection procedure:

1. Compute the sum of all fitness values.
2. Draw a random number from the interval `[0, sum]`.
3. Accumulate fitness values until the random number is exceeded.
4. Select the corresponding individual.

This method favors better solutions while maintaining population diversity.

---

## 6. Genetic Operators

### 6.1 Crossover

One-point crossover is used with a global crossover probability.

Two parents exchange genetic material at a randomly selected crossover point, producing two offspring.

---

### 6.2 Mutation

Mutation is implemented as a **bit-flip operation**.

Each gene has a fixed probability of being inverted (`0 ↔ 1`), which helps prevent premature convergence and preserves genetic diversity.

---

## 7. Stopping Conditions

Two alternative stopping criteria are implemented.

### 7.1 Fixed Number of Generations

The algorithm terminates after a predefined number of generations.

---

### 7.2 Stagnation-Based Termination

The algorithm stops when no improvement in the best fitness value is observed for a specified number of consecutive generations.

This allows early termination when further evolution becomes ineffective.

---

## 8. Graphical User Interface (GUI)

A graphical user interface implemented using **Tkinter** allows the user to:

- select the stopping criterion,
- enter problem parameters,
- run the genetic algorithm,
- display the final result.

The application window is centered on the screen and includes input validation.

---

## 9. Output

After termination, the algorithm returns:

- the best individual found,
- its fitness value,
- a solution that satisfies the knapsack capacity constraint.

Screenshots presenting example executions are included in the project documentation.

---

## 10. Summary

The implemented genetic algorithm successfully solves the knapsack problem using classical evolutionary mechanisms.  
Penalty-based constraint handling, roulette wheel selection, and flexible stopping criteria provide a robust and extensible solution suitable for educational purposes.
