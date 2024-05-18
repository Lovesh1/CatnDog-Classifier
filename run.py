import tensorflow as tf
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    print(gpus)
else: print('nothing')