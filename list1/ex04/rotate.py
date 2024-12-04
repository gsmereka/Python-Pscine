import numpy as np
import matplotlib.pyplot as plt
from load_image import load_image

def transpose_image(image):
    """
    Manually transpose an image (flip rows and columns).
    Handles 3D arrays (color images) correctly.
    """
    rows, cols, channels = image.shape
    transposed_image = np.zeros((cols, rows, channels), dtype=image.dtype)
    
    for i in range(rows):
        for j in range(cols):
            for c in range(channels):
                transposed_image[j, i, c] = image[i, j, c]
    
    return transposed_image

def main():
    img = load_image("animal.jpeg")

    center_x = int(img.shape[1] / 2)
    center_y = int(img.shape[0] / 2)
    zoom_size = 200
    square_img = img[(center_y - zoom_size):(center_y + zoom_size),
                            (center_x - zoom_size):(center_x + zoom_size)]

    
    # Display the original image shape and data
    print(f"The shape of image is: {square_img.shape}")
    print(square_img)
    
    # Transpose the image manually
    transposed_img = transpose_image(square_img)
    
    # Display the new shape and data after transpose
    print(f"New shape after Transpose: {transposed_img.shape}")
    print(transposed_img)
    
    # Display the transposed image
    plt.imshow(transposed_img)
    plt.savefig("output.png")

if __name__ == "__main__":
    main()
