# 🖼️ Image Pixel Manipulator (NumPy)

Treats an image as a 3D NumPy array (**height × width × RGB**) and creates, crops, flips, recolors and filters synthetic images using **only NumPy**. Matplotlib is used just to display results.

![Overview](outputs/overview.png)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/image-pixel-manipulator/blob/main/image_pixel_manipulator.ipynb)

## Features
- **Create** images with `np.zeros`, `np.ones`, `np.full`, `np.random`, plus gradients and checkerboards
- **Draw** colour blocks, stripes and circles using 3D slicing and boolean masks
- **Crop, flip** (negative-step slicing), **rotate** and **extract R/G/B channels**
- **Brightness control** via `float32` casting + `np.clip` (avoids `uint8` overflow)
- **Boolean masking** to isolate bright pixels
- **Filters:** grayscale, invert, threshold, 3×3 box blur (no per-pixel loops)
- **Memory comparison** of `uint8` vs `float32` vs `float64` using `nbytes`
- Overflow bug demo, view-vs-copy demo and `assert` tests

## Project structure
```
image-pixel-manipulator/
├── README.md
├── image_pixel_manipulator.ipynb   # step-by-step notebook with explanations
├── pixel_toolkit.py                # reusable NumPy functions
├── requirements.txt
└── outputs/
    └── overview.png
```

## How to run
**Option 1 (easiest):** click the *Open in Colab* badge and choose *Runtime → Run all*.

**Option 2 (locally):**
```bash
git clone https://github.com/YOUR_USERNAME/image-pixel-manipulator.git
cd image-pixel-manipulator
pip install -r requirements.txt
jupyter notebook image_pixel_manipulator.ipynb
```

## Quick example
```python
from pixel_toolkit import *

img = gradient(200, 200)
img = draw_circle(img, 100, 100, 40, (255, 255, 255))
bright = adjust_brightness(img, 1.5)     # safe: float32 -> clip -> uint8
mirror = flip(img, "horizontal")         # img[:, ::-1]
```

## What I learned
- An image is a `(h, w, 3)` array and slicing `img[r1:r2, c1:c2, ch]` selects any region or channel.
- `uint8` overflows silently (`200 + 100 = 44`), so calculate in `float32`, clip, then cast back.
- `[::-1]` flips an image by reading rows/columns backwards.
- Boolean masks select pixels by condition.
- `float64` uses 8× the memory of `uint8` for an identical-looking image.
- Slices are views, so use `.copy()` when you need independence.

## Resume line
Developed an image manipulation toolkit using 3D NumPy array slicing, dtype casting (uint8/float32) and boolean masks for cropping, flipping, channel extraction and brightness control.

## Author
**YOUR NAME** · [LinkedIn](https://linkedin.com/in/YOUR_PROFILE)
