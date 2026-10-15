"""
pixel_toolkit.py
A small image-manipulation toolkit built with ONLY NumPy.

An image is a 3D array of shape (height, width, 3) with dtype uint8:
    axis 0 -> rows (height)
    axis 1 -> columns (width)
    axis 2 -> colour channels: 0 = Red, 1 = Green, 2 = Blue
"""
import numpy as np


# ----------------------------------------------------------------------
# 1. Creating images
# ----------------------------------------------------------------------
def create_image(h=200, w=200, color=(0, 0, 0)):
    """Make a solid-colour image (np.full)."""
    return np.full((h, w, 3), color, dtype=np.uint8)


def noise_image(h=200, w=200, seed=None):
    """Random-pixel image (np.random)."""
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, size=(h, w, 3), dtype=np.uint8)


def gradient(h=200, w=200):
    """Red increases left->right, blue decreases top->bottom."""
    img = np.zeros((h, w, 3), dtype=np.uint8)
    img[:, :, 0] = np.linspace(0, 255, w).astype(np.uint8)
    img[:, :, 2] = np.linspace(255, 0, h).astype(np.uint8)[:, None]
    return img


def checkerboard(size=200, square=25):
    """Black/white checkerboard built with a boolean mask."""
    y, x = np.indices((size, size))
    mask = ((y // square) + (x // square)) % 2 == 0
    img = np.zeros((size, size, 3), dtype=np.uint8)
    img[mask] = 255
    return img


# ----------------------------------------------------------------------
# 2. Drawing with slicing / masks
# ----------------------------------------------------------------------
def draw_rect(img, top, left, height, width, color):
    """Return a copy of img with a filled rectangle (3D slicing)."""
    out = img.copy()
    out[top:top + height, left:left + width] = color
    return out


def draw_stripes(img, start, stop, thickness, gap, color, horizontal=True):
    """Draw repeated stripes between `start` and `stop`."""
    out = img.copy()
    for pos in range(start, stop, thickness + gap):
        if horizontal:
            out[pos:pos + thickness, :] = color
        else:
            out[:, pos:pos + thickness] = color
    return out


def draw_circle(img, cy, cx, r, color):
    """Filled circle using a boolean mask over the whole image."""
    out = img.copy()
    y, x = np.ogrid[:img.shape[0], :img.shape[1]]
    mask = (y - cy) ** 2 + (x - cx) ** 2 <= r ** 2
    out[mask] = color
    return out


# ----------------------------------------------------------------------
# 3. Crop, flip, rotate, channels
# ----------------------------------------------------------------------
def crop(img, top, left, height, width):
    """Crop a rectangle. Returns a COPY so the original stays safe."""
    return img[top:top + height, left:left + width].copy()


def flip(img, direction="horizontal"):
    """Flip using negative-step slicing."""
    if direction == "horizontal":
        return img[:, ::-1]      # reverse the columns (mirror)
    return img[::-1]             # reverse the rows (upside down)


def rotate90(img, k=1):
    """Rotate by k * 90 degrees counter-clockwise."""
    return np.rot90(img, k)


def get_channel(img, c):
    """Keep only one channel (0=R, 1=G, 2=B) and zero out the others."""
    out = np.zeros_like(img)
    out[:, :, c] = img[:, :, c]
    return out


# ----------------------------------------------------------------------
# 4. Brightness, masks and filters
# ----------------------------------------------------------------------
def adjust_brightness(img, factor):
    """factor > 1 brightens, factor < 1 darkens. Safe from uint8 overflow."""
    return np.clip(img.astype(np.float32) * factor, 0, 255).astype(np.uint8)


def bright_mask(img, threshold=150):
    """Boolean mask: True where the pixel's average value > threshold."""
    return img.mean(axis=2) > threshold


def keep_masked(img, mask):
    """Keep pixels where mask is True, make the rest black."""
    out = np.zeros_like(img)
    out[mask] = img[mask]
    return out


def grayscale(img):
    """Weighted average that matches human eye sensitivity."""
    g = (img.astype(np.float32) @ np.array([0.299, 0.587, 0.114])).astype(np.uint8)
    return np.stack([g, g, g], axis=2)


def invert(img):
    """Photographic negative."""
    return 255 - img


def threshold(img, t=128):
    """Pure black-and-white image using a boolean mask."""
    bw = (img.mean(axis=2) > t).astype(np.uint8) * 255
    return np.stack([bw, bw, bw], axis=2)


def box_blur(img):
    """3x3 average blur using shifted slices (no per-pixel loops)."""
    f = np.pad(img.astype(np.float32), ((1, 1), (1, 1), (0, 0)), mode="edge")
    h, w = img.shape[:2]
    total = sum(f[dy:dy + h, dx:dx + w] for dy in range(3) for dx in range(3))
    return (total / 9).astype(np.uint8)


# ----------------------------------------------------------------------
# 5. Memory
# ----------------------------------------------------------------------
def memory_report(img):
    """Print memory used by the same image stored in different dtypes."""
    base = img.astype(np.uint8).nbytes
    for dt in (np.uint8, np.float32, np.float64):
        n = img.astype(dt).nbytes
        print(f"{dt.__name__:8s}: {n:>9,} bytes  ({n // base}x uint8)")
