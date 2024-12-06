import numpy as np
from PIL import Image
import os


os.makedirs("folder", exist_ok=True)


def save_image(array: np.ndarray, filename: str) -> None:
    """
    Save an array as an image in the "folder".
    """
    image = Image.fromarray(array.astype("uint8"))
    image.save(os.path.join("folder", filename))


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
Inverts the color of the image received.
    """
    inverted = 255 - array
    save_image(inverted, "inverted.png")
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Filter only the red channel, setting other channels to zero.
    """
    red = array * [1, 0, 0]
    save_image(red, "red.png")
    return red

def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Filter only the green channel, setting other channels to zero.
    """
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    save_image(green, "green.png")
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Filter only the blue channel, setting other channels to zero.
    """
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    save_image(blue, "blue.png")
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Convert the image to grayscale by averaging the channels.
    The result will have the same value for each channel [b, b, b] for each pixel.
    """
    grey = array.copy()
    grey[:,:,0] = grey[:,:,2]
    grey[:,:,1] = grey[:,:,2]

    save_image(grey, "grey.png")
    
    return grey