import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("../assets/nature.jpg")
img = np.array(img)

img_sorted_0 = np.sort(img, axis=0)
img_sorted_1 = np.sort(img, axis=1)
img_sorted_2 = np.sort(img, axis=2)

plt.figure(1)
# plt.tight_layout()
plt.subplot(221)
plt.title("Original")
plt.imshow(img)
plt.axis("off")

plt.subplot(222)
plt.title("Axis = 0")
plt.imshow(img_sorted_0)
plt.axis("off")

plt.subplot(223)
plt.title("Axis = 1")
plt.imshow(img_sorted_1)
plt.axis("off")

plt.subplot(224)
plt.title("Axis = 2")
plt.imshow(img_sorted_2)
plt.axis("off")
plt.show()