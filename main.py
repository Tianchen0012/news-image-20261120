"""Sum up 20 November 2026 world news in one image.

Deterministic, no network: copies the bundled image to /output/entry.png.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    src = os.path.join(HERE, "entry.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)

if __name__ == "__main__":
    main()
