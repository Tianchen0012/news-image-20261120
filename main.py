"""Sum up 20 November 2026 world news in one image.

Deterministic, no network: copies the bundled image to /output/entry.png,
after verifying it is a valid 1024x1024 PNG under 1 MiB, so a corrupt or
wrong-sized bundle fails loudly instead of submitting a bad entry.
"""
import os
import shutil
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024


def png_size(path):
    """Return (width, height) of a PNG file, verifying its signature."""
    with open(path, "rb") as f:
        header = f.read(33)
    if header[:8] != PNG_SIGNATURE:
        raise ValueError("entry.png is not a PNG file")
    if header[12:16] != b"IHDR":
        raise ValueError("entry.png has no PNG IHDR chunk")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        raise FileNotFoundError("bundled entry.png is missing")
    if os.path.getsize(src) > MAX_BYTES:
        raise ValueError("entry.png is over 1 MiB")
    width, height = png_size(src)
    if (width, height) != (1024, 1024):
        raise ValueError(f"entry.png must be 1024x1024, got {width}x{height}")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        raise ValueError("copied entry.png does not match the bundled file")


if __name__ == "__main__":
    main()
