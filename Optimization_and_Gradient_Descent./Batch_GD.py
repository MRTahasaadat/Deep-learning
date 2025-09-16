import tensorflow as tf
import numpy as np

# Data
rng = np.random.default_rng(0)
x = rng.uniform(-2, 2, size = (500,1)).astype(np.float32)
y = (3.0 * x - 2.0 + rng.normal(0, 0.3, size = (500,1))).astype(np.float32)

def train_with_batchsize(batch_size):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(1, input_shape=(1,))
    ])

    model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.05),loss='mse')

    model.fit(x, y, epochs=20, batch_size=batch_size, verbose=0)
    w, b = model.layers[0].get_weights()
    return w[0][0], b[0]

print("Batch Size :", train_with_batchsize(len(x))) 
print("Mini-batch Size (32) :", train_with_batchsize(32))
print("SGD ", train_with_batchsize(1))