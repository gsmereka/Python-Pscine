from typing import List, Union


def give_bmi(height: List[Union[int, float]],
             weight: List[Union[int, float]]) -> List[Union[int, float]]:
    if len(height) != len(weight):
        raise ValueError("The height and weight lists \
        must have the same size.")

    for h in height:
        if not isinstance(h, (int, float)):
            raise TypeError("The height list must contain\
             only integers or floats.")

    for w in weight:
        if not isinstance(w, (int, float)):
            raise TypeError("The weight list must contain\
             only integers or floats.")

    bmi = []
    for h, w in zip(height, weight):
        if h == 0:
            raise ValueError("Height cannot be zero.")

        bmi_value = w / (h ** 2)
        bmi.append(bmi_value)

    return bmi


def apply_limit(bmi: List[Union[int, float]], limit: int) -> List[bool]:
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("The BMI list must contain\
             only integers or floats.")

    if not isinstance(limit, int):
        raise TypeError("The limit must be an integer.")

    result = []
    for b in bmi:
        result.append(b > limit)
    return (result)
