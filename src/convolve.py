import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image

img = Image.open("../assets/nature2.jpg")
img = np.array(img) / 255
print (img.shape)

width = img.shape[0]
filter_size = 2
stride = 1
padding = 0

final_dim = int((width - filter_size + 2*padding) / (stride + 1))
print (final_dim)

final_img = np.zeros((final_dim, final_dim))
print (final_img.shape)

kernel = np.random.uniform(0, 1, size=(filter_size, filter_size))

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

for i in range(0, len(img), filter_size):
    collection = img[i:i+filter_size, i:i+filter_size]
    bias = np.random.uniform(0, 1)
    z = sigmoid(np.sum(np.dot(kernel, collection)) + bias)
    
    