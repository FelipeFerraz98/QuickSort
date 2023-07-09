# QuickSortAlgorithm

This is a Python academic project that aims to sort three .txt files that have numbers out of order using a quicksort algorithm. Sorting will be performed in two ways for each file, once sequentially and once in parallel and asynchronously.

The program has two main features:

1. Sequential Algorithm: It is a .py file which contains a function of the same name that performs the ordering through the quicksort algorithm, the ordering will be carried out sequentially.

2. Parallel Algorithm: It is a .py file which contains a function of the same name that performs the ordering through the quicksort algorithm, the ordering will be carried out in a parallel and asynchronous way using the "concurrent.futures" library.

## Requirements

* Python 3.x
* futures 3.0.5

## How to use
1. Download or clone the program repository.

2. Make sure you have Python 3.x and futures 3.0.5 installed on your system.

3. Run the main.py file in QuickSortProgram folder using the following command:

       python main.py


## Files

* main.py: Contains the main function of the program, where the user will start the program and count the execution time of each algorithm in each file for sorting.
* parallel_algorithm.py: Contains the quicksort algorithm to order the lists of numbers provided in "Files" in a parallel and asynchronous way.
* sequential_algorithm.py: Contains the quicksort algorithm to order the lists of numbers provided in "Files" sequentially.
* interactions.py: Contains functions to count movements and comparisons performed in the quicksort algorithm for sorting.
* Files folder: Folder containing three .txt files containing out-of-order numbers for the quicksort algorithm to sort.
* Requirements.txt: It is a file that contains the requirements to use in the pip installation

## Contribution
Contributions are welcome! If you encounter an issue, have a suggestion, or want to improve the code, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.