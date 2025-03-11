import tensorflow as tf

# Create two random matrices
a = tf.random.uniform([1000, 1000])
b = tf.random.uniform([1000, 1000])

# Multiply the two matrices
c = tf.matmul(a, b)

# Run the operation and print the result
print(c)
