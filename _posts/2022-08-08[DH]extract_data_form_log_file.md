```python
import os
```


```python
f=open('Deeplearning_log.txt','r')
output=open('output.txt','w')
```


```python
for line in f:
    if 'loss' in line:
        output.write(line)
output.close()
```


```python
for line in f:
    if 'Training for fold' in line:
        output.write(line)
    if 'loss' in line:
        output.write(line)
output.close()
```


```python

```
