import time # Library to record the time it takes the program to run every sort algorithm
import parallel_algorithm as ap # Import module "parallel_algorithm" and apply the nickname "ap"
import sequential_algorithm as sq # Import module "sequential_algorithm" and apply nickname "sq"
from interactions import results, clear # Import "results and clean" from the interacoes module to obtain algorithm comparisons and movements

# Defining the paths of the input files containing the numbers to be sorted
thousand_numbers = r'./Files/1000RandomNumbers.txt'
ten_thousand_numbers = r'./Files/10000RandomNumbers.txt'
hundred_thousand_numbers = r'./Files/100000RandomNumbers.txt'

# Opening and reading the contents of the file "1000NumerosAleatorios.txt"
with open(thousand_numbers, "r") as file:
     thousand_numbers = file.readlines()

# Opening and reading the contents of the file "10000NumerosAleatorios.txt"
with open(ten_thousand_numbers, "r") as file:
     ten_thousand_numbers = file.readlines()

# Opening and reading the contents of the file "100000NumerosAleatorios.txt"
with open(hundred_thousand_numbers, "r") as file:
     hundred_thousand_numbers = file.readlines()


def parallel(numbers):
    # Registering the initial time of the execution of the algorithm
    start = time.time()

    # Calling the "quick_sort" function of the "parallel_algorithm" module to sort the list of numbers
    ap.quick_sort(numbers) # ap is the nickname of the "parallel_algorithm" module

    # Registering the final time of the execution of the algorithm
    end = time.time()

    # Calculating the total running time
    total_time = end - start

    # Printing the sort total_time of the Parallel QuickSort algorithm
    print(f"Parallel QuickSort sort time =", total_time)


def sequential(list):
    # Registering the initial time of the execution of the algorithm
    start = time.time()

    # Calling the "quick_sort" function of the "sequential_algorithm" module to sort the list of numbers
    sq.quick_sort(list) # sq is the nickname of the module "sequential_algorithm"

    # Registering the final time of the execution of the algorithm
    end = time.time()

    # Calculating the total running time
    total_time = end - start

    # Printing the sort total_time of the Sequential QuickSort algorithm
    print(f"Sequential QuickSort sort time =", time)


def execution(list):
    # Running the Sequential and Parallel QuickSort algorithm on the list of numbers
    print("\n", "-=" * 5, "SEQUENTIAL", "=-" * 5)
    sequential(list)
    print("\n", "-=" * 5, "PARALLEL", "=-" * 5)
    parallel(list)

    # Get the results of comparisons and moves
    print("\n", "-=" * 5, "COMPARISONS/MOVES", "=-" * 5)
    compare, move = results()
    print(f"This run had {compare} comparisons")
    print(f"This execution had {move} moves")
    clear() # Clear the values of comparisons and movements for the next execution


# Performing ordering of numbers in different input sizes
print("-=" * 15, "THOUSAND NUMBERS", "=-" * 15)
execution(thousand_numbers)
print("\n", "-=" * 15, "TEN THOUSAND NUMBERS", "=-" * 15)
execution(ten_thousand_numbers)
print("\n", "-=" * 15, "ONE HUNDRED THOUSAND NUMBERS", "=-" * 15)
execution(hundred_thousand_numbers)