from tqdm import trange
from time import sleep

for i in trange(100, desc="Progress"):
    sleep(0.001)
