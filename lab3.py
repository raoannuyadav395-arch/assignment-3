

import time
import random

# =================================================================
# TASK 1: IMPLEMENTING CORE SORTING ALGORITHMS (FROM SCRATCH)
# =================================================================
# Criteria: Implementation of Insertion, Merge, and Quick Sort [cite: 59, 128]

def insertion_sort(arr):
    """Logic: O(n^2) time, stable, and in-place[cite: 25, 112]."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    """Logic: O(n log n) time, stable, out-of-place[cite: 27, 113]."""
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def quick_sort(arr):
    """Logic: Average O(n log n), in-place partitioning[cite: 28, 114]."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# =================================================================
# TASK 2: PERFORMANCE MEASUREMENT & DATASET GENERATION
# =================================================================
# Criteria: Measure time fairly on different dataset types and sizes [cite: 75, 76]

def get_execution_time(sort_type, data):
    """Timing Utility: Returns execution time in milliseconds[cite: 78, 81]."""
    start = time.perf_counter()
    
    # Create a copy so each algorithm sorts the same original data [cite: 80]
    data_copy = data.copy()
    
    if sort_type == "Quick":
        quick_sort(data_copy)
    elif sort_type == "Merge":
        merge_sort(data_copy)
    else:
        insertion_sort(data_copy)
        
    end = time.perf_counter()
    return (end - start) * 1000 # Convert to ms

# =================================================================
# MAIN RUNNER (OUTPUT WITH TASK LABELS)
# =================================================================

def run_spa():
    print("=== SORTING PERFORMANCE ANALYZER (SPA) ===\n")

    # --- TASK 1: CORRECTNESS CHECK ---
    print("[TASK 1: CORRECTNESS CHECK]")
    test_input = [5, 2, 9, 1, 5, 6]
    expected = [1, 2, 5, 5, 6, 9]
    print(f"Testing with: {test_input}")
    
    # Verifying each algorithm 
    t1 = test_input.copy()
    insertion_sort(t1)
    print(f"Insertion Sort Correct: {t1 == expected}")
    
    t2 = test_input.copy()
    merge_sort(t2)
    print(f"Merge Sort Correct: {t2 == expected}")
    
    t3 = quick_sort(test_input.copy())
    print(f"Quick Sort Correct: {t3 == expected}\n")

    # --- TASK 2: RUNNING EXPERIMENTS ---
    print("[TASK 2: DATASET GENERATION & PERFORMANCE MEASUREMENT]")
    # Sizes: 1000, 5000, 10000 [cite: 86]
    sizes = [1000, 5000, 10000]
    
    header = f"{'Size':<7} | {'Data Type':<15} | {'Insertion (ms)':<15} | {'Merge (ms)':<12} | {'Quick (ms)':<12}"
    print(header)
    print("-" * len(header))

    for n in sizes:
        # Generating Random, Sorted, and Reverse-Sorted datasets [cite: 85, 88, 89]
        random_data = [random.randint(1, 100000) for _ in range(n)]
        sorted_data = sorted(random_data)
        reverse_data = sorted_data[::-1]
        
        scenarios = [("Random", random_data), ("Sorted", sorted_data), ("Reverse", reverse_data)]

        for name, data in scenarios:
            # Task 2 (C): Run experiments and record times [cite: 91, 92]
            t_ins = get_execution_time("Insertion", data)
            t_mer = get_execution_time("Merge", data)
            t_qui = get_execution_time("Quick", data)

            print(f"{n:<7} | {name:<15} | {t_ins:<15.2f} | {t_mer:<12.2f} | {t_qui:<12.2f}")

    print("\n[TASK 3: EXPERIMENTS COMPLETE]")
    print("Please refer to report.pdf for complexity analysis[cite: 97, 118].")

if __name__ == "__main__":
    run_spa()