# Module: MyArrays
def second_largest(array):
    """Returns the second largest element in an array."""
    if len(array) < 2:
        return None  # Not enough elements
    unique_sorted = sorted(set(array), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

def range_diff(array):
    """Returns the difference between the largest and smallest values in an array."""
    return max(array) - min(array)

def median(array):
    """Returns the median of numbers in an array."""
    sorted_array = sorted(array)
    n = len(sorted_array)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_array[mid - 1] + sorted_array[mid]) / 2
    else:
        return sorted_array[mid]

def min_max(array):
    """Returns a two-element array containing the smallest and largest values in an array."""
    return [min(array), max(array)]

def array_to_string(array):
    """Returns array elements as a string, separated by the minus sign."""
    return "-".join(str(x) for x in array)