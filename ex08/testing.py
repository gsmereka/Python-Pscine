from time import sleep
from tqdm import tqdm
from loading import ft_tqdm

print("Testing ft_tqdm:")
for elem in ft_tqdm(range(333)):
    sleep(0.005)

print("\nTesting tqdm:")
for elem in tqdm(range(333)):
    sleep(0.005)
