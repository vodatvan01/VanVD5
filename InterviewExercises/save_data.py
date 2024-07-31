import tensorflow as tf
import numpy as np

# Tải dữ liệu MNIST
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Lưu dữ liệu vào tệp .npz
np.savez('mnist.npz', x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)
print("Đã lưu dữ liệu MNIST vào tệp mnist.npz")