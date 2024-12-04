import numpy as np
from PIL import Image
import os

os.makedirs("folder", exist_ok=True)

def save_image(array: np.ndarray, filename: str) -> None:
    """
    Salva um array como uma imagem na pasta "folder".
    """
    image = Image.fromarray(array.astype("uint8"))
    image.save(os.path.join("folder", filename))
    print(f"Imagem salva como folder/{filename}")

def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverte as cores de uma imagem (255 - valor do pixel).
    """
    inverted = 255 - array
    save_image(inverted, "inverted.png")
    return inverted

def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Filtra apenas o canal vermelho, zerando os outros canais.
    """
    red = array.copy()
    red[..., 1] = 0  # Zera o canal verde
    red[..., 2] = 0  # Zera o canal azul
    save_image(red, "red.png")
    return red

def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Filtra apenas o canal verde, zerando os outros canais.
    """
    green = array.copy()
    green[..., 0] = 0  # Zera o canal vermelho
    green[..., 2] = 0  # Zera o canal azul
    save_image(green, "green.png")
    return green

def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Filtra apenas o canal azul, zerando os outros canais.
    """
    blue = array.copy()
    blue[..., 0] = 0  # Zera o canal vermelho
    blue[..., 1] = 0  # Zera o canal verde
    save_image(blue, "blue.png")
    return blue

def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converte a imagem para tons de cinza, calculando a média dos canais.
    """
    grey = array.mean(axis=2, dtype=int)  # Calcula a média de cada pixel
    grey_image = np.stack((grey, grey, grey), axis=-1)  # Replica o valor nos 3 canais
    save_image(grey_image, "grey.png")
    return grey_image
