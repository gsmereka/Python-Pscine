
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
        zoomed_img = image[
            (center_y - zoom_size):(center_y + zoom_size),
            (center_x - zoom_size):(center_x + zoom_size)
        ]
        if zoomed_img.shape[-1] != 3:
            raise ValueError("The image needs to be a 3-channel image.")
        zoomed_img = np.mean(zoomed_img, axis=-1, keepdims=True).astype(np.uint8)
        return zoomed_img
    except Exception as e:
        print(f"Error processing the image: {e}")
        return None


def transpose_image(image):
    """
    Manually transpose an image (flip rows and columns).
    If the image has a single channel, the third dimension is removed
    before transposing.
    """

    rows, cols, extra = image.shape
    transposed_image = np.zeros((cols, rows))

    for i in range(rows):
        for j in range(cols):
            transposed_image[j, i] = image[i, j, 0]
    return transposed_image


def main():
    """
    Main function to load an image and display\
     a transposed and zoomed-in section of it.
    """
    img = load_image("animal.jpeg")
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
