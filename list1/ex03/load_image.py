from PIL import Image
import numpy as np


def load_image(filepath):
    try:
        image = Image.open(filepath)
        image = np.array(image)
        if image is None:
            raise FileNotFoundError(f"Imagem não encontrada: {filepath}")
        return image
    except FileNotFoundError as e:
        print(f"Erro: {e}")
        return None
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")
        return None
