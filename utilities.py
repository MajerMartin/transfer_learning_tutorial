import cv2
import numpy as np
import matplotlib.pyplot as plt

def keep_ratio(shape, height, width):
    # height <= width
    if shape[0] <= shape[1]:
        ratio = height / shape[0]
        width = shape[1] * ratio
    elif shape[0] >= shape[1]:
        ratio = width / shape[1]
        height = shape[0] * ratio
    else:
        pass

    # opencv dimension format
    dim = np.ceil(width).astype(int), np.ceil(height).astype(int)

    return dim

def crop(img, height, width):
    if (img.shape[0] == height) and (img.shape[1] == width):
        return img
    elif img.shape[0] == height:
        middle = np.ceil(img.shape[1] / 2).astype(int)
        return img[:, (middle - width // 2):(middle + width // 2)]
    else:
        middle = np.ceil(img.shape[0] / 2).astype(int)
        return img[(middle - height // 2):(middle + height // 2), :]

def resize_crop(img, height, width):
    dim = keep_ratio(img.shape, height, width)
    img_resized = cv2.resize(img, dim, interpolation=cv2.INTER_CUBIC)
    img_cropped = crop(img_resized, height, width)

    return img_cropped

def plot_sample(images, columns=6, images_count=18, shuffle=True):
    indexes = np.arange(images.shape[0])
    
    if shuffle:
        np.random.shuffle(indexes)
    
    choice = sorted(indexes[:images_count])
    
    sample = images[choice, ...].astype(np.uint8)
        
    plt.figure(figsize=(20, 10))
    for i, image in enumerate(sample):
        plt.subplot(len(sample) / columns + 1, columns, i + 1)
        plt.imshow(image)
        plt.axis("off")
    plt.show()