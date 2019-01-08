import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
X_train = np.linspace(0.1,0.5,100)
Y_train = 8*X_train+5+np.random.randn(100)*0.123
plt.plot(X_train,Y_train,'go',label='raw data')
print("测试！")
plt.legend()
plt.show()