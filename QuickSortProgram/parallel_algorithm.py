import concurrent.futures # Import Parallelism library

def quick_sort(number_list):
    # Main function to call the Quick Sort algorithm
    quick_sort_helper(number_list, 0, len(number_list) - 1)

def quick_sort_helper(number_list, first, last):
    # Helper function for Quick Sort that implements recursion and divides the list into smaller partitions

    if first < last:
        # Stopping condition: if the first element is less than the last element

        cutoff_point = quick_sort_algorithm(number_list, first, last)
        # Find the cutoff point (pivot) that divides the list into two partitions

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(quick_sort_helper, (number_list, first, cutoff_point - 1))
            # Execute the quick_sort_helper function asynchronously for the first half of the list to the left of the cutoff point
            
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(quick_sort_helper, (number_list, cutoff_point + 1, last))
            # Execute the quick_sort_helper function asynchronously for the second half of the list to the right of the cutoff point


def quick_sort_algorithm(number_list, first, last):
    # Implementation of the Quick Sort algorithm

    pivot = number_list[first]
    # Select the first element of the list as the pivot

    left_point = first + 1
    right_point = last
    # Set the pointers to traverse the list from left to right and from right to left

    is_complete = False
    # Control variable to check if the partition is complete

    while not is_complete:
        # Loop to perform comparisons and swaps of elements

        while left_point <= right_point and int(number_list[left_point]) <= int(pivot):
            left_point = left_point + 1
            # Move the left pointer forward while the value is less than or equal to the pivot

        while int(number_list[right_point]) >= int(pivot) and right_point >= left_point:
            right_point = right_point - 1
            # Move the right pointer backward while the value is greater than or equal to the pivot

        if right_point < left_point:
            is_complete = True
            # Check if the pointers have crossed, indicating that the partition is complete
        else:
            # Swap the elements to ensure that the smaller ones are on the left and the larger ones are on the right
            auxiliary = number_list[left_point]
            number_list[left_point] = number_list[right_point] 
            number_list[right_point] = auxiliary
            
    # Swap the pivot to its correct position
    auxiliary = number_list[first]
    number_list[first] = number_list[right_point]
    number_list[right_point] = auxiliary

    return right_point
    # Return the index of the pivot, which will be used to divide the list into smaller partitions

        