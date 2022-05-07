## Test data를 Train 데이터와 같은 형식으로 만들기


```python
import os
import pandas as pd
```


```python
### dataset
Train_dataset = pd.read_csv("GPCR_Interaction_Matrix_20.csv")
Test_dataset = pd.read_csv("GPCR_Interaction_Matrix_20_TEST_set.csv")
```


```python
df = pd.concat([Train_dataset, Test_dataset], ignore_index=True)
```


```python
df.to_csv("DLdata_GRCP_Interaction_n20_TEST_set.csv", mode='w', index=None)
```
