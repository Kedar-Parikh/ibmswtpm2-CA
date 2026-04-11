import os
import subprocess
import re


images_dir = "/home/paper/Projects/ibmswtpm2-CA/workspace/sample_images/lessthan64kbimages"   # change if needed


files = [
    f for f in os.listdir(images_dir)
    if f.endswith((".png", ".jpg"))
]


def get_size(filename):
    match = re.search(r"_(\d+)kb", filename)
    return int(match.group(1)) if match else 0


files = sorted(files, key=get_size)

for file in files:
    filepath = os.path.join(images_dir, file)
    size = get_size(file)

    print(f"\n=== Running for {file} ({size} KB) ===")

    
    subprocess.run(["python", "main.py", filepath])

    
    subprocess.run([
        "rm",
        "aes.ctx", "aes.priv", "aes.pub",
        "cipher.bin", "decrypted.txt", "primary.ctx"
    ])