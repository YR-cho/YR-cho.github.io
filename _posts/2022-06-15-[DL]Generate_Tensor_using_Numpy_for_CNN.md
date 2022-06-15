```python
import numpy as np  
import os
import glob
from glob import glob
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import datasets, layers, models

from matplotlib import pyplot as plt
```

### Numpy로 input 데이터 만들기


```python
a = np.random.rand(67500).reshape(150,150,3)
b = np.random.rand(67500).reshape(150,150,3)
c = np.random.rand(67500).reshape(150,150,3)
d = np.random.rand(67500).reshape(150,150,3)
e = np.random.rand(67500).reshape(150,150,3)
f = np.random.rand(67500).reshape(150,150,3)
g = np.random.rand(67500).reshape(150,150,3)
sample = np.stack((a,b,c,d,e,f,g))
```


```python
sample.shape
```




    (7, 150, 150, 3)




```python
label = np.random.randint(2, size=7) ### label을 vector로 만듬
label.shape
```




    (7,)


b4000 = np.random.rand(270000000).reshape(4000,150,150,3)
b4000.shape
label = np.random.randint(2, size=4000)
label.shape

```python

```

### CNN Tensorflow


```python
from sklearn.model_selection import train_test_split
x = sample 
y = label
```


```python
X_train, X_test, y_train, y_test = train_test_split(x, 
                                                    y, 
                                                    test_size=0.3, 
                                                    random_state=1004)
```


```python
print(X_train.shape, X_test.shape)
```

    (4, 150, 150, 3) (3, 150, 150, 3)
    


```python
### 데이터 행렬의 크기와 형태에 따라서 결정된다.
data_height = 150
data_width = 150
channel_n = 3
```


```python

```


```python
  # CNN model network
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(data_height, data_width, channel_n)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()
```

    Model: "sequential_1"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    conv2d (Conv2D)              (None, 148, 148, 32)      896       
    _________________________________________________________________
    max_pooling2d (MaxPooling2D) (None, 74, 74, 32)        0         
    _________________________________________________________________
    conv2d_1 (Conv2D)            (None, 72, 72, 64)        18496     
    _________________________________________________________________
    max_pooling2d_1 (MaxPooling2 (None, 36, 36, 64)        0         
    _________________________________________________________________
    conv2d_2 (Conv2D)            (None, 34, 34, 128)       73856     
    _________________________________________________________________
    flatten (Flatten)            (None, 147968)            0         
    _________________________________________________________________
    dense (Dense)                (None, 64)                9470016   
    _________________________________________________________________
    dense_1 (Dense)              (None, 1)                 65        
    =================================================================
    Total params: 9,563,329
    Trainable params: 9,563,329
    Non-trainable params: 0
    _________________________________________________________________
    


```python
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
```


```python
history = model.fit(X_train, y_train, validation_data=(X_test,y_test),
                                                       batch_size=128,
                                                       epochs=5)
```

    Epoch 1/5
    1/1 [==============================] - 1s 628ms/step - loss: 0.6709 - accuracy: 0.7500 - val_loss: 16.0880 - val_accuracy: 0.3333
    Epoch 2/5
    1/1 [==============================] - 0s 97ms/step - loss: 5.8712 - accuracy: 0.7500 - val_loss: 5.2581 - val_accuracy: 0.3333
    Epoch 3/5
    1/1 [==============================] - 0s 98ms/step - loss: 1.7051 - accuracy: 0.7500 - val_loss: 0.6372 - val_accuracy: 0.6667
    Epoch 4/5
    1/1 [==============================] - 0s 99ms/step - loss: 0.8419 - accuracy: 0.2500 - val_loss: 0.7032 - val_accuracy: 0.3333
    Epoch 5/5
    1/1 [==============================] - 0s 102ms/step - loss: 0.6213 - accuracy: 1.0000 - val_loss: 0.9894 - val_accuracy: 0.3333
    


```python
# model chart
plt.figure(figsize=(12,4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend(['train', 'validation'])

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train', 'validation'])
```




    <matplotlib.legend.Legend at 0x11fcdfebda0>




    
![png](output_16_1.png)
    



```python

```
