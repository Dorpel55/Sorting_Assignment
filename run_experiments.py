import random
import time
import statistics
import matplotlib.pyplot as plt
import argparse
import sys


#Part A - We choose the Bubble, Merge and Insertion sorts.
def bubble_sort(arr):
    len_arr = len(arr)
    for i in range(0, len_arr-1):
        for j in range(0, len_arr-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j] 
                arr[j] = arr[j+1]
                arr[j+1] = temp
                
    return arr


def merge_sort(arr):
    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    mid = len_arr // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge_func(left, right)


def merge_func(left, right):
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def insertion_sort(arr):
    len_arr = len(arr)
    for i in range(1, len_arr):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1
    return arr


#Part C-
def nearly_sorted_array(n, noise_percent):
    arr = list(range(n))
    num_swaps = int(n * noise_percent/100)

    for _ in range(num_swaps):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]

    return arr


#part B -
#creating a random array of the chosen size.
def random_array(n):
    return [random.randint(0, 100000) for _ in range(n)]  # creates random array


#Calling the sorting function with the specific array and measuring the running time.
def measure_time(algo, arr):
    start = time.perf_counter()
    algo(arr.copy())
    end = time.perf_counter()
    total = end - start  # checks time difference
    return total


#Ploting the results.
def plot_func(sizes, bubble, merge, insertion, bubble_c, merge_c, insertion_c):
    avg_b, std_b = bubble
    avg_i, std_i = insertion
    avg_m, std_m = merge

    avg_b_c, std_b_c = bubble_c
    avg_i_c, std_i_c = insertion_c
    avg_m_c, std_m_c = merge_c

    # ===== Part B: Random Arrays =====
    plt.figure()

    plt.plot(sizes, avg_b, label="Bubble")
    plt.plot(sizes, avg_i, label="Insertion")
    plt.plot(sizes, avg_m, label="Merge")

    plt.fill_between(sizes,
                     [a - s for a, s in zip(avg_b, std_b)],
                     [a + s for a, s in zip(avg_b, std_b)],
                     alpha=0.2)

    plt.fill_between(sizes,
                     [a - s for a, s in zip(avg_i, std_i)],
                     [a + s for a, s in zip(avg_i, std_i)],
                     alpha=0.2)

    plt.fill_between(sizes,
                     [a - s for a, s in zip(avg_m, std_m)],
                     [a + s for a, s in zip(avg_m, std_m)],
                     alpha=0.2)

    plt.xlabel("Array size (n)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime Comparison with Std Deviation")
    plt.legend()
    plt.grid()
    plt.savefig("result1.png")
    plt.close()

    # ===== Part C: Nearly Sorted =====
    plt.figure()

    plt.plot(sizes, avg_b_c, label="Bubble (Nearly Sorted)")
    plt.plot(sizes, avg_i_c, label="Insertion (Nearly Sorted)")
    plt.plot(sizes, avg_m_c, label="Merge (Nearly Sorted)")

    plt.fill_between(sizes,
                     [a - s for a, s in zip(avg_b_c, std_b_c)],
                     [a + s for a, s in zip(avg_b_c, std_b_c)],
                     alpha=0.2)

    plt.fill_between(sizes,
                     [a - s for a, s in zip(avg_i_c, std_i_c)],
                     [a + s for a, s in zip(avg_i_c, std_i_c)],
                     alpha=0.2)

    plt.fill_between(sizes,
                     [a - s for a, s in zip(avg_m_c, std_m_c)],
                     [a + s for a, s in zip(avg_m_c, std_m_c)],
                     alpha=0.2)

    plt.xlabel("Array size (n)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Nearly Sorted Arrays")
    plt.legend()
    plt.grid()

    plt.savefig("result2.png")
    plt.close()


def experiment(sizes, times, noise):
    #Parameters for each sorting method. The ones with the _c are for Part C
    avg_times_b = []
    deviations_b = []
    avg_times_i = []
    deviations_i = []
    avg_times_m = []
    deviations_m = []
    avg_times_b_c = []
    deviations_b_c = []
    avg_times_i_c = []
    deviations_i_c = []
    avg_times_m_c = []
    deviations_m_c = []

    #1) Creating an array for each size.
    #2) Measuring the running time for each method per array.
    #3) Calculating the average time and deviation of the running times per size.
    #4) Sending the results to the plotting function.
    for size in sizes:
        time_insertion = []
        time_bubble = []
        time_merge = []
        time_insertion_c = []
        time_bubble_c = []
        time_merge_c = []

        for i in range(times):
            specific_arr = random_array(size)
            array_c = nearly_sorted_array(size, noise)

            #Insertion Check
            t = measure_time(insertion_sort, specific_arr)
            time_insertion.append(t)
            t = measure_time(insertion_sort, array_c)
            time_insertion_c.append(t)

            # Bubble Check
            t = measure_time(bubble_sort, specific_arr)
            time_bubble.append(t)
            t = measure_time(bubble_sort, array_c)
            time_bubble_c.append(t)

            # Merge Check
            t = measure_time(merge_sort, specific_arr)
            time_merge.append(t)
            t = measure_time(merge_sort, array_c)
            time_merge_c.append(t)

        avg_b = sum(time_bubble) / len(time_bubble)
        avg_i = sum(time_insertion) / len(time_insertion)
        avg_m = sum(time_merge) / len(time_merge)
        avg_b_c = sum(time_bubble_c) / len(time_bubble_c)
        avg_i_c = sum(time_insertion_c) / len(time_insertion_c)
        avg_m_c = sum(time_merge_c) / len(time_merge_c)

        deviation_b = statistics.stdev(time_bubble)
        deviation_i = statistics.stdev(time_insertion)
        deviation_m = statistics.stdev(time_merge)
        deviation_b_c = statistics.stdev(time_bubble_c)
        deviation_i_c = statistics.stdev(time_insertion_c)
        deviation_m_c = statistics.stdev(time_merge_c)

        avg_times_b.append(avg_b)
        deviations_b.append(deviation_b)
        avg_times_i.append(avg_i)
        deviations_i.append(deviation_i)
        avg_times_m.append(avg_m)
        deviations_m.append(deviation_m)

        avg_times_b_c.append(avg_b_c)
        deviations_b_c.append(deviation_b_c)
        avg_times_i_c.append(avg_i_c)
        deviations_i_c.append(deviation_i_c)
        avg_times_m_c.append(avg_m_c)
        deviations_m_c.append(deviation_m_c)

    bubble = avg_times_b, deviations_b
    insertion = avg_times_i, deviations_i
    merge = avg_times_m, deviations_m

    bubble_c = avg_times_b_c, deviations_b_c
    insertion_c = avg_times_i_c, deviations_i_c
    merge_c = avg_times_m_c, deviations_m_c

    #Finally plotting the results.
    plot_func(sizes, bubble, merge, insertion, bubble_c, merge_c, insertion_c)


def parse_user_input():
    parser = argparse.ArgumentParser(description="Sorting Algorithms Experiment")

    # Algorithms selection
    parser.add_argument('-a', '--algorithms', nargs=3, type=int, required=True,
                        help="Choose exactly 3 algorithms from: 1-Bubble, 2-Selection, 3-Insertion, 4-Merge, 5-Quick")

    # Sizes
    parser.add_argument('-s', '--sizes', nargs='+', type=int, required=True,
                        help="Array sizes (e.g., 100 500 1000)")

    # Noise level
    parser.add_argument('-e', '--noise', type=int, required=True,
                        help="1- Nearly sorted with 5% noise, 2- Nearly sorted with 20% noise")

    # Repetitions (optional but recommended)
    parser.add_argument('-r', '--repeats', type=int, required=True,
                        help="Number of repetitions")

    args = parser.parse_args()

    # ===== Validation =====

    valid_algorithms = {1, 2, 3, 4, 5}

    # Check algorithms are valid
    if not all(a in valid_algorithms for a in args.algorithms):
        print("Error: Invalid algorithm ID. Use only 1–5.")
        sys.exit(1)

    if not all(a in [1, 3, 4] for a in args.algorithms):
        print("Error: Sorry we choose to work with the Bubble, Insertion and Merge sorts ")

    # Check uniqueness
    if len(set(args.algorithms)) != 3:
        print("Error: You must choose exactly 3 DIFFERENT algorithms.")
        sys.exit(1)

    # Check sizes
    if any(s <= 0 for s in args.sizes):
        print("Error: Sizes must be positive integers.")
        sys.exit(1)

    # Check noise
    if args.noise == 1:
        noise_level = 5
    elif args.noise == 2:
        noise_level = 20
    else:
        print("Error: Experiment type must be 1 (5% noise) or 2 (20% noise).")
        sys.exit(1)

    return list(args.sizes), int(args.noise), int(args.repeats)


def main():
    sizes, noise, repeats = parse_user_input()
    experiment(sizes, repeats, noise)


main()