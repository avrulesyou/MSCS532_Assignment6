import random
import time
import matplotlib.pyplot as plt
import pandas as pd
import sys

# Increase recursion limit for Median of Medians on large inputs
sys.setrecursionlimit(2000)

# --- Deterministic Selection (Median of Medians) ---
def median_of_medians(arr, k):
    """
    Finds the k-th smallest element in an array in worst-case linear time.
    arr: list of numbers
    k: the order statistic to find (0-indexed)
    """
    # If list is small, just sort and return
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Step 1: Divide the list into chunks of 5 elements.
    chunks = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    
    # Step 2: Find the median of each chunk.
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]

    # Step 3: Recursively find the median of the medians.
    pivot = median_of_medians(medians, len(medians) // 2)

    # Step 4: Partition the array around the pivot.
    # Elements smaller, equal to, and larger than the pivot.
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    
    # Step 5: Recurse into the appropriate partition.
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + len(pivots):
        # The k-th element is the pivot itself
        return pivot
    else:
        # The k-th element is in the 'high' partition.
        # Adjust k to search in the smaller subarray.
        return median_of_medians(high, k - len(low) - len(pivots))

# --- Randomized Selection (Quickselect) ---
def randomized_quickselect(arr, k):
    """
    Finds the k-th smallest element in an array in expected linear time.
    arr: list of numbers
    k: the order statistic to find (0-indexed)
    """
    if not arr:
        return None

    # Choose a random pivot
    pivot = random.choice(arr)
    
    # Partition the array based on the pivot
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    # Recurse based on the position of k
    if k < len(low):
        return randomized_quickselect(low, k)
    elif k < len(low) + len(pivots):
        return pivot
    else:
        # Adjust k for the recursive call on the 'high' partition
        return randomized_quickselect(high, k - len(low) - len(pivots))

# --- Empirical Analysis ---
def run_analysis():
    """
    Runs the empirical analysis of the two selection algorithms.
    """
    # Increased number of input sizes for more detailed analysis
    input_sizes = [1000, 2500, 5000, 7500, 10000, 15000, 20000, 30000, 40000, 50000]
    results = []

    print("Starting performance analysis...\n")

    for size in input_sizes:
        # Generate a random array of integers
        random_arr = [random.randint(0, size * 10) for _ in range(size)]
        # We will find the median element, so k is size // 2
        k = size // 2

        # --- Time Deterministic Algorithm ---
        start_time_det = time.time()
        median_of_medians(random_arr.copy(), k)
        deterministic_time = time.time() - start_time_det

        # --- Time Randomized Algorithm ---
        start_time_rand = time.time()
        randomized_quickselect(random_arr.copy(), k)
        randomized_time = time.time() - start_time_rand

        results.append({
            "Input Size": size,
            "Deterministic Time (s)": deterministic_time,
            "Randomized Time (s)": randomized_time
        })
        print(f"Completed analysis for input size: {size}")

    return pd.DataFrame(results)

# --- Main execution block ---
if __name__ == '__main__':
    # --- Part 1: Demonstrate Correctness ---
    print("### Demonstrating Algorithm Correctness ###")
    sample_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    k_to_find = 5 # Find the 6th smallest element (0-indexed)
    
    print(f"Sample Array: {sample_array}")
    print(f"Finding the k-th smallest element for k = {k_to_find}\n")

    # Using Median of Medians
    det_result = median_of_medians(sample_array.copy(), k_to_find)
    print(f"Deterministic (Median of Medians) result: {det_result}")

    # Using Randomized Quickselect
    rand_result = randomized_quickselect(sample_array.copy(), k_to_find)
    print(f"Randomized (Quickselect) result: {rand_result}")

    # Verification using Python's sort
    correct_result = sorted(sample_array)[k_to_find]
    print(f"Verification with sorted(): {correct_result}")
    print("-" * 40 + "\n")


    # --- Part 2: Run Performance Analysis ---
    performance_df = run_analysis()

    # --- Display Performance Table ---
    print("\n### Performance Analysis Table ###")
    # Using to_string() for better alignment in console
    print(performance_df.to_string(index=False))

    # --- Plotting Results ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 7))

    ax.plot(performance_df["Input Size"], performance_df["Deterministic Time (s)"], marker='o', linestyle='-', label="Deterministic (Median of Medians)")
    ax.plot(performance_df["Input Size"], performance_df["Randomized Time (s)"], marker='x', linestyle='--', label="Randomized (Quickselect)")

    ax.set_title("Performance of Selection Algorithms", fontsize=16, fontweight='bold')
    ax.set_xlabel("Input Size (n)", fontsize=12)
    ax.set_ylabel("Execution Time (seconds)", fontsize=12)
    ax.legend()
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Improve tick formatting
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
