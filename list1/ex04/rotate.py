
import numpy as np
import matplotlib.pyplot as plt
from load_image import load_image


def zoom_image(image, zoom_size):
    """
    Apply a zoomed-in section of an image and return it.

    Parameters:
    - image: The input image to be processed (should be a 3-channel image).
    - zoom_size: Size of the zoom window (should be an integer).
    """
    try:
        if image is None:
            raise ValueError("Image not loaded correctly.")
        center_x = int(image.shape[1] / 2)
        center_y = int(image.shape[0] / 2)
        zoom_size = int(zoom_size / 2)
        zoomed_image = image[
            (center_y - zoom_size):(center_y + zoom_size),
            (center_x - zoom_size):(center_x + zoom_size)
        ]
        if zoomed_image.shape[-1] != 3:
            raise ValueError("The image needs to be a 3-channel image.")
        zoomed_image = np.mean(zoomed_image, axis=-1, keepdims=True)
        return zoomed_image
    except Exception as e:
        print(f"Error processing the image: {e}")
        return None

def transpose_image(image):
    """
    Manually transpose an image (flip rows and columns).
    If the image has a single channel, the third dimension is removed
    before transposing.
    """
    if image.ndim == 3 and image.shape[2] == 1:
        image = image[:, :, 0]
    
    rows, cols = image.shape
    transposed_image = np.zeros((cols, rows), dtype=image.dtype)
    
    for i in range(rows):
        for j in range(cols):
            transposed_image[j, i] = image[i, j]
    
    return transposed_image

def main():
    img = load_image("animal.jpeg")
    center_x = int(img.shape[1] / 2)
    center_y = int(img.shape[0] / 2)
    zoom_size = 400
    square_img = zoom_image(img, zoom_size)

    print(f"The shape of image is: {square_img.shape}")
    print(square_img)
    transposed_img = transpose_image(square_img)
    print(f"New shape after Transpose: {transposed_img.shape}")
    print(transposed_img)

    plt.imshow(transposed_img, cmap='gray')
    plt.savefig("output.png")

if __name__ == "__main__":
    main()
