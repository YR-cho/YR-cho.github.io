## Ligand data to vector


```python
import sys
import os
import numpy as np
import pandas as pd
import rdkit
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem
from sklearn.preprocessing import scale
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
# 실루엣 분석 metric 값을 구하기 위한 API 추가
from sklearn.metrics import silhouette_samples, silhouette_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb
from io import StringIO
%matplotlib inline

```


```python
pd.set_option('display.max_seq_items', None) ### 모든 데이터를 디스플레이하는 옵션
```


```python
path = "./Lignad_DL" 
file_list = os.listdir(path) 
```


```python
# 파일로드
df = pd.read_csv('./Lignad_DL/O43614.csv')
df_drop = df.drop_duplicates(['SMILES'])  ### 중복 제거
```


```python
for i in file_list:
    df=pd.read_csv("./Lignad_DL/"+i)
    df_drop = df.drop_duplicates(['SMILES']) 
    print(i[:-4],":",df.shape[0],"-",df_drop.shape[0],"=",df.shape[0]-df_drop.shape[0])
```

    O43613 : 9 - 8 = 1
    O43614 : 6 - 3 = 3
    P00268 : 6 - 6 = 0
    P02699 : 6 - 6 = 0
    P07550 : 25 - 11 = 14
    P07700 : 21 - 12 = 9
    P08172 : 5 - 3 = 2
    P21554 : 4 - 4 = 0
    P29274 : 29 - 13 = 16
    P41595 : 7 - 6 = 1
    Q99835 : 8 - 7 = 1
    

### 중복 제거 후 추출


```python
# 파일로드
df = pd.read_csv('./Lignad_DL/P29274.csv')
df = df.drop_duplicates(['SMILES'])  ### 중복 제거
fps = []
for i, smiles in enumerate(df["SMILES"]):
    mol = Chem.MolFromSmiles(smiles)
    arr = np.zeros((1,))
    
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2048)
    DataStructs.ConvertToNumpyArray(fp, arr)
    fps.append(arr)
    
df["fp"] = fps
```


```python
### 저장
df.to_csv('./P29274_Drop.csv', index = False)
np.save("./P29274_Drop.npy", fps)  ## finger print 형태가 넘파이 형태로 데이터를 제작할 필요가 있다.
```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```

### 각 자료를 로드함


```python
data_numpy = np.load('./LC/O43614_Drop.npy') 
PDB_name = pd.read_csv('./LC/O43614_Drop.csv')
PDB_ID=PDB_name["Title"]
PDB_fp=PDB_name["fp"]
```


```python
feature_names = []
for i in range(2048):
    feature_names.append(i)
```


```python
ligand_DF = pd.DataFrame(data=data_numpy, columns=feature_names)  ## numpy형태 DF형태로 변환
```


```python
### PCA analysis

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca_transformed = pca.fit_transform(ligand_DF)

ligand_DF['pca_x'] = pca_transformed[:,0]
ligand_DF['pca_y'] = pca_transformed[:,1]
```


```python
ligand_DF
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>2040</th>
      <th>2041</th>
      <th>2042</th>
      <th>2043</th>
      <th>2044</th>
      <th>2045</th>
      <th>2046</th>
      <th>2047</th>
      <th>pca_x</th>
      <th>pca_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.430968</td>
      <td>-0.172901</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-4.386288</td>
      <td>-6.314395</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>-4.044679</td>
      <td>6.487296</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 2050 columns</p>
</div>




```python
ligand_DF_PCA = ligand_DF[['pca_x','pca_y']]

import sklearn.cluster as cluster
K =range(1,3)
wss = []
for k in K:
    kmeans = cluster.KMeans(n_clusters=k, init="k-means++")
    kmeans = kmeans.fit(ligand_DF_PCA)
    wss_iter = kmeans.inertia_
    wss.append(wss_iter)


mycenters = pd.DataFrame({'Clusters' : K, 'WSS' : wss})
mycenters

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Clusters</th>
      <th>WSS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>188.666667</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>82.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
import seaborn as sns
sns.lineplot(x = 'Clusters', y = 'WSS', data = mycenters, marker='o')
```




    <matplotlib.axes._subplots.AxesSubplot at 0x2460dd3ca90>




    
![png](output_22_1.png)
    



```python
### Cluster analysis
kmeans = KMeans(n_clusters=2, init='k-means++', max_iter=300,random_state=0).fit(ligand_DF)
ligand_DF['cluster'] = kmeans.labels_

dfK1 = pd.DataFrame(PDB_name["Title"].tolist())  ## 해당 결과를 list 형태로 만들고 데이터 프레임으로 변환
dfK2 = pd.DataFrame(kmeans.labels_.tolist())   ## 해당 결과를 list 형태로 만들고 데이터 프레임으로 변환

result = pd.concat([dfK1,dfK2],axis=1)
result.columns = ['PDBID',"Group"]
```


```python
result.to_csv("Cluster_O43614.csv", mode='w')
```


```python

```


```python

```
