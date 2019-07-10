#how to use dqdm
import time
from tqdm import tqdm

text = ""
for char in tqdm(["a", "b", "c", "d"]):
    text = text + char
    time.sleep(0.5)