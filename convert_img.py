import cv2
import numpy as np


def get_img(img_path, x, y):
    if isinstance(img_path, str):
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (x, y))
        # convert img to numpy matrix
        img = np.array(img)
        return img
    else:
        raise TypeError("img_path must be a string")


def kernel_filter_k(img, k):
    # define output matrix
    output = np.zeros((len(img) - k + 1, len(img[0]) - k + 1))

    y = 0
    while y < len(img) - k + 1:
        x = 0
        while x < len(img[0]) - k + 1:
            for i in range(k):
                for j in range(k):
                    # row + column if it's even * 1 else * 0
                    if (i + j) % 2 == 0:
                        output[y][x] += img[i + y][j + x]
            x += 1
        y += 1
    return output


def max_pooling(filtered_img, pool_size):
    # define output matrix
    output = np.zeros((len(filtered_img) // pool_size, len(filtered_img[0]) // pool_size))

    y = 0
    while y < len(filtered_img) - pool_size + 1:
        x = 0
        while x < len(filtered_img[0]) - pool_size + 1:
            pool = filtered_img[y:y + pool_size, x:x + pool_size]
            output[y // pool_size][x // pool_size] = np.max(pool)
            x += pool_size
        y += pool_size
    return output


def average_pooling(filtered_img, pool_size):
    # define output matrix
    output = np.zeros((len(filtered_img) // pool_size, len(filtered_img[0]) // pool_size))

    y = 0
    while y < len(filtered_img) - pool_size + 1:
        x = 0
        while x < len(filtered_img[0]) - pool_size + 1:
            pool = filtered_img[y:y + pool_size, x:x + pool_size]
            output[y // pool_size][x // pool_size] = np.mean(pool)
            x += pool_size
        y += pool_size
    return output


def convert_img(pooling):
    # convert pooling to flat array
    flat_pooling = np.array([])
    for row in pooling:
        flat_pooling = np.concatenate((flat_pooling, row))
    # apply softmax
    softmax_output = np.exp(flat_pooling) / np.sum(np.exp(flat_pooling))
    return softmax_output
