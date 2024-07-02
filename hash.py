import cv2
import hashlib
import numpy as np


def histogram_hash(image_path):
    img = cv2.imread(image_path)
    hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    hash_object = hashlib.sha256(hist)
    return hash_object.hexdigest()


"""
hash_value = histogram_hash(
    "/Users/kshitij/Personal/Projects/water_marking_system_buildspace_s5/10_food_classes_all_data/test/pizza/11297.jpg"
)
print("Hash produced is: ", hash_value)
"""
