import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list by row indices and returns the result.

    Args:
        family (list): A 2D list where all rows must have the same size.
        start (int): The starting index for slicing (inclusive).
        end (int): The ending index for slicing (exclusive).

    Returns:
        list: A sliced portion of the 2D list.

    Raises:
        TypeError: If the input is not a 2D list.
        ValueError: If rows in the input do not have the same size.
    """
    if not isinstance(family, list):
        raise TypeError("The input must be a list.")
    for row in family:
        if not isinstance(row, list):
            raise TypeError("Each element of the input must be a list.")

    try:
        array = np.array(family)
    except ValueError as e:
        raise ValueError("All rows in the input must \
        have the same size.") from e

    original_shape = array.shape
    print(f"My shape is : {original_shape}")

    truncated_array = array[start:end]
    new_shape = truncated_array.shape
    print(f"My new shape is : {new_shape}")

    result = truncated_array.tolist()
    return result
