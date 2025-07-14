# MSCS532 Assignment 6: Medians and Order Statistics & Elementary Data Structures

This repository contains implementations and empirical analysis of selection algorithms and fundamental data structures. The project demonstrates both theoretical concepts and practical implementations with performance comparisons.

## 📋 Overview

This assignment explores two fundamental areas of computer science:

### Part 1: Medians and Order Statistics
Demonstrates and compares two different approaches to finding the k-th smallest element in an array:

1. **Deterministic Selection (Median of Medians)** - O(n) worst-case time complexity
2. **Randomized Selection (Quickselect)** - O(n) expected time complexity

### Part 2: Elementary Data Structures
Implements and analyzes fundamental data structures including:
- **Arrays and Matrices** - 2D array operations and matrix manipulation
- **Stacks** - LIFO (Last In, First Out) data structure
- **Queues** - FIFO (First In, First Out) data structure  
- **Linked Lists** - Node-based dynamic structure with pointers
- **Rooted Trees** - Hierarchical data structure for representing relationships

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd MSCS532_Assignment6
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the analyses**
   ```bash
   # Run Part 1: Medians and Order Statistics
   python part1.py
   
   # Run Part 2: Elementary Data Structures
   python part2.py
   ```

## 📊 Example Output

### Algorithm Correctness Demonstration

```
### Demonstrating Algorithm Correctness ###
Sample Array: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
Finding the k-th smallest element for k = 5

Deterministic (Median of Medians) result: 4
Randomized (Quickselect) result: 4
Verification with sorted(): 4
----------------------------------------
```

### Performance Analysis Results

```
### Performance Analysis Table ###
 Input Size  Deterministic Time (s)  Randomized Time (s)
       1000                0.000000             0.000000
       2500                0.001007             0.001004
       5000                0.003409             0.002354
       7500                0.004987             0.001994
      10000                0.007703             0.002713
      15000                0.010178             0.006256
      20000                0.016454             0.007464
      30000                0.019125             0.006044
      40000                0.045071             0.011428
      50000                0.034432             0.018465
```

The script also generates a performance comparison plot showing execution times vs input sizes.

## 🔧 Implementation Details

### Deterministic Selection (Median of Medians)

- **Time Complexity**: O(n) worst-case
- **Space Complexity**: O(n)
- **Key Features**:
  - Divides input into groups of 5 elements
  - Finds median of medians as pivot
  - Guarantees linear time complexity
  - More complex implementation but predictable performance

### Randomized Selection (Quickselect)

- **Time Complexity**: O(n) expected
- **Space Complexity**: O(n)
- **Key Features**:
  - Uses random pivot selection
  - Simpler implementation
  - Generally faster in practice
  - Performance varies based on pivot choice

## 📈 Performance Analysis

The analysis compares both algorithms across various input sizes:
- **Input Sizes**: 1,000 to 50,000 elements
- **Test Data**: Random integers
- **Target**: Finding the median element (k = n/2)

### Key Observations

1. **Randomized Quickselect** generally performs better for most input sizes
2. **Deterministic Median of Medians** shows more consistent but slower performance
3. Both algorithms demonstrate linear scaling characteristics
4. Performance differences become more pronounced with larger inputs

## 📁 Project Structure

```
MSCS532_Assignment6/
├── part1.py              # Medians and order statistics analysis
├── part2.py              # Elementary data structures implementation
├── requirements.txt       # Python dependencies
├── README.md            # This file
└── venv/                # Virtual environment (not tracked)
```

## 📦 Dependencies

- `matplotlib` - For plotting performance graphs
- `pandas` - For data manipulation and display
- `numpy` - For numerical operations (dependency of matplotlib/pandas)

## 🔮 Part 2: Elementary Data Structures Implementation and Performance Analysis

Part 2 focuses on implementing and analyzing fundamental data structures including arrays, matrices, stacks, queues, linked lists, and rooted trees.

### Running Part 2

```bash
python part2.py
```

### Example Output

#### Data Structure Demonstrations

```
### 1. Data Structure Demonstrations ###

--- Matrix Demo ---
Initialized a 3x4 matrix.
0 0 0 0
0 0 5 0
0 0 0 0
Value at (1, 2): 5

--- Stack Demo ---
Initialized ArrayStack.
Stack size: 2
Peek: 20
Pop: 20
Is empty: False

--- Queue Demo ---
Initialized ArrayQueue.
Queue size: 2
Dequeue: A
Is empty: False

--- Linked List Demo ---
Initialized SinglyLinkedList.
0 -> 1 -> 2
After deleting 2:
0 -> 1

--- Rooted Tree Demo ---
|-- CEO
    |-- CTO
        |-- Lead Engineer
        |-- Data Scientist
    |-- CFO
        |-- Accountant
```

#### Performance Analysis Results

```
### 3. Performance Analysis Table ###
 Input Size  List Append (End)  LL Insert (End)  List Insert (Front)  LL Insert (Front)  ArrayQueue Dequeue  Deque Dequeue
       1000           0.000048         0.010031             0.000295           0.000214            0.000204       0.000054
       2500           0.000101         0.064136             0.001652           0.000564            0.000574       0.000084
       5000           0.000166         0.251590             0.006681           0.001314            0.002073       0.000164
      10000           0.000431         1.006025             0.067715           0.002388            0.008703       0.000334
      20000           0.000867         4.061750             0.105934           0.005763            0.030468       0.000707
```

### Implemented Data Structures

#### 1. **Matrix Class**
- **Implementation**: Nested lists (2D array)
- **Operations**: Get/Set elements with bounds checking
- **Use Case**: Mathematical computations, image processing

#### 2. **ArrayStack**
- **Implementation**: Python list as underlying structure
- **Operations**: Push, Pop, Peek, Size, IsEmpty
- **Time Complexity**: O(1) for all operations
- **Use Case**: Function call stack, undo operations

#### 3. **ArrayQueue**
- **Implementation**: Python list (inefficient for dequeue)
- **Operations**: Enqueue, Dequeue, Size, IsEmpty
- **Time Complexity**: O(1) enqueue, O(n) dequeue
- **Use Case**: Simple queue implementations

#### 4. **SinglyLinkedList**
- **Implementation**: Node-based structure with pointers
- **Operations**: Insert at beginning/end, delete, traverse
- **Time Complexity**: O(1) insert at beginning, O(n) insert at end
- **Use Case**: Dynamic data structures, memory-efficient lists

#### 5. **Rooted Tree**
- **Implementation**: TreeNode class with children list
- **Operations**: Add child, tree traversal
- **Use Case**: Organizational hierarchies, file systems

### Performance Analysis Insights

#### Key Findings:

1. **List vs Linked List Performance**:
   - **List Append (End)**: Fastest operation - O(1) amortized
   - **Linked List Insert (End)**: Slower due to traversal - O(n)
   - **List Insert (Front)**: Expensive - O(n) due to shifting
   - **Linked List Insert (Front)**: Fast - O(1) constant time

2. **Queue Implementations**:
   - **ArrayQueue (list.pop(0))**: Poor performance - O(n) dequeue
   - **collections.deque**: Excellent performance - O(1) operations
   - **Recommendation**: Use `collections.deque` for queue operations

3. **Scalability Patterns**:
   - Linked list operations show linear growth
   - List front insertion shows quadratic growth
   - Deque maintains consistent performance across all sizes

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is part of MSCS532 coursework. Please refer to your course guidelines for usage permissions.

## 👨‍💻 Author

*Abhishek Vishwakarma* - MSCS532 Student

---

**Note**: This analysis demonstrates the practical differences between deterministic and randomized selection algorithms, providing valuable insights into algorithm design and performance characteristics. 
