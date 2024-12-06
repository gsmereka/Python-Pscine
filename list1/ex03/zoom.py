import numpy as np
import matplotlib.pyplot as plt
from load_image import load_image


def display_image_with_zoom(image):
    """
    Displays a zoomed-in section of an image and saves it as 'output.png'.

    Parameters:
    - image: The input image to be processed (should be a 3-channel image).

    This function extracts a 200x200 pixel section\
     from the center of the image,
     converts it to grayscale, and displays the zoomed image. It also saves the
     zoomed-in image to a file named 'output.png'.
    """
    try:
        if image is None:
            raise ValueError("Image not loaded correctly.")

        print(f"The shape of the image is: {image.shape}")
        print(f"{image}")

        center_x = int(image.shape[1] / 2)
        center_y = int(image.shape[0] / 2)
        zoom_size = 200

        zoomed_img = image[
            (center_y - zoom_size):(center_y + zoom_size),
            (center_x - zoom_size):(center_x + zoom_size)
        ]

        if zoomed_img.shape[-1] != 3:
            raise ValueError("The image needs to be a 3-channel image.")

        zoomed_img = np.mean(
            zoomed_img, axis=-1, keepdims=True).astype(np.uint8)

        print(f"New shape after slicing: {zoomed_img.shape}")
        print(f"{zoomed_img}")

        fig, ax = plt.subplots()
        ax.imshow(zoomed_img, cmap='gray')
        plt.savefig("output.png")
    except Exception as e:
        print(f"Error processing the image: {e}")


def main():
    """
    Main function to load an image and display a zoomed-in section of it.
    """
    image_path = "animal.jpeg"
    image = load_image(image_path)
    display_image_with_zoom(image)


if __name__ == "__main__":
    main()
