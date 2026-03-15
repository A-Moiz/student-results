# Student Progression Outcome System

## Overview
This project is a Python-based program designed to determine student progression outcomes based on the number of credits achieved in **Pass**, **Defer**, and **Fail** categories.  

The system validates user input, calculates progression outcomes, and visualises the results through **horizontal and vertical histograms**. It also stores outcomes in a text file for later retrieval.

The project demonstrates concepts such as **input validation, conditional logic, loops, data structures, file handling, and data visualisation using text-based histograms**.

---

## Features

### 1. Credit Input & Validation
The program prompts the user to input credits for:

- Pass
- Defer
- Fail

Validation rules include:
- Inputs must be **integers**
- Credits must be within the range **0–120**
- Credits must be entered in increments of **20**
- The **total of all credits must equal 120**

If invalid input is provided, the program prompts the user to re-enter the values.

---

### 2. Progression Outcomes
Based on the credit combination entered, the system determines one of four progression outcomes:

| Outcome | Condition |
|------|------|
| **Progress** | Pass = 120 |
| **Progress (module trailer)** | Pass = 100 with 20 credits defer or fail |
| **Do not progress – module retriever** | Lower pass credits but fail credits below exclusion level |
| **Exclude** | High number of fail credits |

Each result is displayed along with the corresponding credit values.

---

### 3. Data Collection
All outcomes are stored in separate lists:

- `progress_list`
- `trailer_list`
- `retriever_list`
- `exclude_list`

Counters are also maintained to track the total number of each outcome.

---

### 4. Horizontal Histogram
The program generates a **horizontal histogram** displaying the number of outcomes in each category.

Example:

```
Progress   3 : * * *
Trailing   2 : * *
Retriever  4 : * * * *
Excluded   1 : *
```

This provides a simple visual representation of the distribution of results.

---

### 5. Vertical Histogram
A **vertical histogram** is also generated for a different visual representation of the outcomes.

Example:

```
 Progress  Trailing  Retriever  Excluded
     *        *          *         *
     *        *          *          
     *                   *          
```

---

### 6. File Storage
The program stores all progression outcomes in a text file:

```
outcomes.txt
```

Each recorded outcome includes the progression result and the associated credit values.

Example:

```
Progress: 120, 0, 0
Trailer: 100, 20, 0
Retriever: 80, 20, 20
Exclude: 40, 0, 80
```

---

### 7. File Reading
After storing results, the program reads the contents of `outcomes.txt` and prints them to the console.

This demonstrates basic **file writing and file reading operations in Python**.

---

## Technologies Used

- **Python**
- Standard Python libraries:
  - File handling
  - Input validation
  - Data structures (lists)
  - Conditional logic
  - Loops

---

## How to Run the Program

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/your-repository-name.git
```

### 2. Navigate to the project directory
```bash
cd your-repository-name
```

### 3. Run the program
```bash
python progression_outcomes.py
```

---

## Example Workflow

1. User enters credit values
2. Program validates the input
3. Progression outcome is calculated
4. User decides whether to enter another dataset
5. Histograms are generated
6. Results are stored in a text file
7. Stored data is printed from the file

---

## Learning Objectives

This project demonstrates understanding of:

- Python control structures
- Data validation techniques
- Use of lists for storing structured data
- File input/output operations
- Text-based data visualisation
- Modular programming using functions

---

## Author

**Abdul Moiz**  
BSc Computer Science (First-Class)  
University of Westminster
