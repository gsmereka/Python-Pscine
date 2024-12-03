import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
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
