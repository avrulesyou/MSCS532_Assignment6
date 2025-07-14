import time
import matplotlib.pyplot as plt
import pandas as pd
from collections import deque

# --- Part 1: Data Structure Implementations ---

# 1.1 Arrays and Matrices (using Python lists)
class Matrix:
    """A simple Matrix implementation using nested lists."""
    def __init__(self, rows, cols, default_value=0):
        if rows <= 0 or cols <= 0:
            raise ValueError("Matrix dimensions must be positive.")
        self._data = [[default_value for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols
        print(f"Initialized a {rows}x{cols} matrix.")

    def get(self, row, col):
        """Access an element."""
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Matrix index out of range.")
        return self._data[row][col]

    def set(self, row, col, value):
        """Set an element's value."""
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            raise IndexError("Matrix index out of range.")
        self._data[row][col] = value

    def __str__(self):
        """String representation for printing."""
        return "\n".join([" ".join(map(str, row)) for row in self._data])

# 1.2 Stacks (using Python list)
class ArrayStack:
    """A stack implementation using a Python list (dynamic array)."""
    def __init__(self):
        self._items = []
        print("Initialized ArrayStack.")

    def push(self, item):
        """Add item to top of stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return item from top of stack."""
        if not self.is_empty():
            return self._items.pop()
        raise IndexError("pop from an empty stack")

    def peek(self):
        """Return top item without removing it."""
        if not self.is_empty():
            return self._items[-1]
        raise IndexError("peek from an empty stack")

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self._items)

# 1.3 Queues (using Python list - inefficient for dequeues)
class ArrayQueue:
    """A queue implementation using a Python list."""
    def __init__(self):
        self._items = []
        print("Initialized ArrayQueue.")

    def enqueue(self, item):
        """Add item to the back of the queue."""
        self._items.append(item)

    def dequeue(self):
        """Remove and return item from the front of the queue."""
        if not self.is_empty():
            return self._items.pop(0) # Inefficient operation: O(n)
        raise IndexError("dequeue from an empty queue")

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self._items)

# 1.4 Linked Lists
class Node:
    """A node for a singly linked list."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """A singly linked list implementation."""
    def __init__(self):
        self.head = None
        print("Initialized SinglyLinkedList.")

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        """Delete a node with the given data key."""
        current = self.head
        # If head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        # Search for the key to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        # If key was not present in linked list
        if current is None:
            return
        # Unlink the node from linked list
        prev.next = current.next
        current = None

    def traverse(self):
        """Print all elements of the linked list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" -> ".join(nodes))

# 1.5 Rooted Trees (using Linked List nodes)
class TreeNode(Node): # Inherits from Node
    """A node for a tree structure."""
    def __init__(self, data=None):
        super().__init__(data)
        self.children = [] # List of child TreeNode objects

    def add_child(self, child_node):
        """Add a child to this node."""
        self.children.append(child_node)

def print_tree(node, level=0):
    """Print the tree structure recursively."""
    if node:
        print(' ' * level * 4 + '|-- ' + str(node.data))
        for child in node.children:
            print_tree(child, level + 1)

# --- Part 2: Demonstrations ---
def run_demonstrations():
    print("### 1. Data Structure Demonstrations ###\n")

    # Matrix
    print("--- Matrix Demo ---")
    m = Matrix(3, 4)
    m.set(1, 2, 5)
    print(m)
    print(f"Value at (1, 2): {m.get(1, 2)}\n")

    # Stack
    print("--- Stack Demo ---")
    s = ArrayStack()
    s.push(10)
    s.push(20)
    print(f"Stack size: {s.size()}")
    print(f"Peek: {s.peek()}")
    print(f"Pop: {s.pop()}")
    print(f"Is empty: {s.is_empty()}\n")

    # Queue
    print("--- Queue Demo ---")
    q = ArrayQueue()
    q.enqueue('A')
    q.enqueue('B')
    print(f"Queue size: {q.size()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Is empty: {q.is_empty()}\n")

    # Linked List
    print("--- Linked List Demo ---")
    ll = SinglyLinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_beginning(0)
    ll.traverse()
    ll.delete_node(2)
    print("After deleting 2:")
    ll.traverse()
    print("")

    # Rooted Tree
    print("--- Rooted Tree Demo ---")
    root = TreeNode("CEO")
    cto = TreeNode("CTO")
    cfo = TreeNode("CFO")
    root.add_child(cto)
    root.add_child(cfo)
    cto.add_child(TreeNode("Lead Engineer"))
    cto.add_child(TreeNode("Data Scientist"))
    cfo.add_child(TreeNode("Accountant"))
    print_tree(root)
    print("-" * 40 + "\n")

# --- Part 3: Performance Analysis ---
def run_performance_analysis():
    """Benchmarks key operations and returns a pandas DataFrame."""
    print("### 2. Running Performance Analysis ###\n")
    input_sizes = [1000, 2500, 5000, 10000, 20000]
    results = []

    for size in input_sizes:
        print(f"Benchmarking with size: {size}...")
        # --- List (Array) Operations ---
        # Append (Insertion at end)
        lst = []
        start_time = time.perf_counter()
        for i in range(size):
            lst.append(i)
        list_append_time = time.perf_counter() - start_time

        # Insertion at beginning
        lst = []
        start_time = time.perf_counter()
        for i in range(size):
            lst.insert(0, i)
        list_insert_front_time = time.perf_counter() - start_time

        # --- Linked List Operations ---
        ll = SinglyLinkedList()
        # Insertion at end
        start_time = time.perf_counter()
        for i in range(size):
            ll.insert_at_end(i)
        ll_insert_end_time = time.perf_counter() - start_time

        # Insertion at beginning
        ll = SinglyLinkedList()
        start_time = time.perf_counter()
        for i in range(size):
            ll.insert_at_beginning(i)
        ll_insert_front_time = time.perf_counter() - start_time
        
        # --- Queue Operations ---
        # ArrayQueue (list.pop(0))
        aq = ArrayQueue()
        for i in range(size):
            aq.enqueue(i)
        start_time = time.perf_counter()
        for _ in range(size):
            aq.dequeue()
        array_queue_dequeue_time = time.perf_counter() - start_time
        
        # Deque (collections.deque)
        dq = deque()
        for i in range(size):
            dq.append(i)
        start_time = time.perf_counter()
        for _ in range(size):
            dq.popleft()
        deque_dequeue_time = time.perf_counter() - start_time


        results.append({
            "Input Size": size,
            "List Append (End)": list_append_time,
            "LL Insert (End)": ll_insert_end_time,
            "List Insert (Front)": list_insert_front_time,
            "LL Insert (Front)": ll_insert_front_time,
            "ArrayQueue Dequeue": array_queue_dequeue_time,
            "Deque Dequeue": deque_dequeue_time
        })

    return pd.DataFrame(results)

# --- Main execution block ---
if __name__ == '__main__':
    run_demonstrations()
    
    # Run analysis and get DataFrame
    perf_df = run_performance_analysis()

    # Display Performance Table
    print("\n### 3. Performance Analysis Table ###")
    print(perf_df.to_string(index=False))

    # Plotting Results
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    fig.suptitle('Data Structure Performance Comparison', fontsize=16, fontweight='bold')

    # Plot 1: Insertion at End
    axes[0].plot(perf_df["Input Size"], perf_df["List Append (End)"], marker='o', label="List Append (End)")
    axes[0].plot(perf_df["Input Size"], perf_df["LL Insert (End)"], marker='x', label="Linked List Insert (End)")
    axes[0].set_title("Insertion at End")
    axes[0].set_xlabel("Input Size")
    axes[0].set_ylabel("Time (seconds)")
    axes[0].legend()

    # Plot 2: Insertion at Beginning
    axes[1].plot(perf_df["Input Size"], perf_df["List Insert (Front)"], marker='o', label="List Insert (Front)")
    axes[1].plot(perf_df["Input Size"], perf_df["LL Insert (Front)"], marker='x', label="Linked List Insert (Front)")
    axes[1].set_title("Insertion at Beginning")
    axes[1].set_xlabel("Input Size")
    axes[1].set_ylabel("Time (seconds)")
    axes[1].legend()
    
    # Plot 3: Queue Dequeue Performance
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    ax2.plot(perf_df["Input Size"], perf_df["ArrayQueue Dequeue"], marker='s', label="ArrayQueue (list.pop(0))")
    ax2.plot(perf_df["Input Size"], perf_df["Deque Dequeue"], marker='d', label="collections.deque")
    ax2.set_title("Queue Dequeue Performance")
    ax2.set_xlabel("Input Size")
    ax2.set_ylabel("Time (seconds)")
    ax2.legend()


    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
