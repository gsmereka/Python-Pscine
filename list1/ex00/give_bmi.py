from typing import List, Union


def give_bmi(height: List[Union[int, float]],
             weight: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Calculate BMI for each individual as weight / (height ** 2).

    Args:
        height (List[Union[int, float]]): List of heights in meters.
        weight (List[Union[int, float]]): List of weights in kilograms.

    Returns:
        List[Union[int, float]]: BMI values for each individual.

    Raises:
        ValueError: If lists have different sizes or height is zero.
        TypeError: If height/weight contains non-numeric values.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same size.")

    for h in height:
        if not isinstance(h, (int, float)):
            raise TypeError("Height must contain only numbers.")

    for w in weight:
        if not isinstance(w, (int, float)):
            raise TypeError("Weight must contain only numbers.")

    bmi = []
    for h, w in zip(height, weight):
        if h == 0:
            raise ValueError("Height cannot be zero.")
        bmi.append(w / (h ** 2))

    return bmi


def apply_limit(bmi: List[Union[int, float]], limit: int) -> List[bool]:
    """
    Check if each BMI exceeds a given limit.

    Args:
        bmi (List[Union[int, float]]): List of BMI values.
        limit (int): Threshold to compare BMI values.

    Returns:
        List[bool]: Boolean list indicating if BMI exceeds the limit.

    Raises:
        TypeError: If BMI contains non-numeric values\
         or limit is not an integer.
    """
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("BMI must contain only numbers.")
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")

    return [b > limit for b in bmi]
