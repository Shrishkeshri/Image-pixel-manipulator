# 🖼️ Image Pixel Manipulator (NumPy)

Treats an image as a 3D NumPy array (**height × width × RGB**) and creates, crops, flips, recolors and filters synthetic images using **only NumPy**. Matplotlib is used just to display results.

![Overview](outputs/overview.png)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shrishkeshri/image-pixel-manipulator/blob/main/image_pixel_manipulator.ipynb)

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
git clone https://github.com/Shrishkeshri/image-pixel-manipulator.git
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

## Author
**SHRISH KESHRI** · [LinkedIn](https://linkedin.com/in/YOUR_PROFILE)
