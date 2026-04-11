from PIL import Image
import numpy as np
import os


def generate_image(filename, target_kb):
    target_bytes = target_kb * 1024

    # Use PNG for very small sizes
    use_png = target_kb <= 5

    size = 32  # start small

    while True:
        data = np.random.randint(0, 256, (size, size, 3), dtype=np.uint8)
        img = Image.fromarray(data, 'RGB')

        if use_png:
            img.save(filename, format='PNG')
        else:
            img.save(filename, format='JPEG', quality=95)

        current_size = os.path.getsize(filename)

        # stop when close AND safe for TPM
        if current_size >= target_bytes * 0.9 and current_size < 64000:
            print(f"{filename} → {current_size/1024:.2f} KB (target {target_kb} KB)")
            return

        size = int(size * 1.2)


def generate_dataset():
    sizes_kb = [1, 2, 5, 10, 15, 25, 40, 50, 63]

    for size in sizes_kb:
        ext = "png" if size <= 5 else "jpg"
        filename = f"img_{size}kb.{ext}"
        generate_image(filename, size)


def verify():
    print("\nFinal file sizes:\n")
    for f in sorted(os.listdir()):
        if f.endswith((".jpg", ".png")):
            print(f"{f} → {os.path.getsize(f)/1024:.2f} KB")


if __name__ == "__main__":
    generate_dataset()
    verify()