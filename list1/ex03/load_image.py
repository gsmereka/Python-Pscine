from PIL import Image
from numpy import asarray
import numpy as np


def load_image(path: str) -> np.ndarray:
    """
    Loads an image from the specified path, prints its format and shape,
     and returns its pixel content as a NumPy array in RGB format.

    Args:
        path (str): The file path to the image.

    Returns:
        np.ndarray: The pixel data of the image in RGB format.
    """
    try:
        img = Image.open(path)

        if img.format not in ["JPEG", "JPG"]:
            raise ValueError("Only JPG and JPEG formats are supported.")

        img = img.convert("RGB")
        img_array = asarray(img)

        return img_array

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except ValueError as ve:
        raise ValueError(f"Error processing image: {ve}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")
