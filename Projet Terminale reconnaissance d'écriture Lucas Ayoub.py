from PIL import Image
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt

(X_train,Y_train), (X_test,Y_test) = mnist.load_data()

print('X_train shape: ',X_train.shape)
print('Y_train shape: ',Y_train.shape)

plt.imshow(X_train[160])
plt.show()
print(Y_train[160])

"""x = np.arange(0, 5, 0.1)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()"""
