## 필요 정보만 추출하여 Matrix 만들기


```python
import pandas as pd
```


```python
df=pd.read_csv("2I35.csv")
dfp=pd.read_csv("2I35_prop.csv")
```


```python
df_rmsd = dfp["r_i_glide_rmsd_to_input"]
```


```python
pd.concat([df, df_rmsd], axis=1) # 옆 쪽 방향으로 Matrix를 합친다.
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
      <th>Title</th>
      <th>A0_contact</th>
      <th>A0_backbone</th>
      <th>A0_sidechain</th>
      <th>A0_polar</th>
      <th>A0_hydrophobic</th>
      <th>A0_acceptor</th>
      <th>A0_donor</th>
      <th>A0_aromatic</th>
      <th>A0_charged</th>
      <th>...</th>
      <th>A326_contact</th>
      <th>A326_backbone</th>
      <th>A326_sidechain</th>
      <th>A326_polar</th>
      <th>A326_hydrophobic</th>
      <th>A326_acceptor</th>
      <th>A326_donor</th>
      <th>A326_aromatic</th>
      <th>A326_charged</th>
      <th>r_i_glide_rmsd_to_input</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ligand_2I35</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2.420319</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ligand_2I35</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1.300578</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ligand_2I35</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2.401464</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ligand_2I35</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>...</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>2.036761</td>
    </tr>
  </tbody>
</table>
<p>4 rows × 2945 columns</p>
</div>



## Matrix 자동 제작 스크립트


```python
import os
```


```python
path_csv = "./list/csv" 
csv_list = os.listdir(path_csv) 
path_csv_p = "./list/csv_p" 
csvp_list = os.listdir(path_csv_p) 
```


```python
for i,j in zip(csv_list,csvp_list): # 두 가지 group을 zip으로 반복문을 실행한다.
    print('df=pd.read_csv("./list/csv/'+i+'")')
    print('dfp=pd.read_csv("./list/csv_p/'+j+'")')
    print('df_rmsd = dfp["r_i_glide_rmsd_to_input"]')
    print('df_sum = pd.concat([df, df_rmsd], axis=1)')
    print('Matrix_'+i[0:4],"= df_sum")
```

    df=pd.read_csv("./list/csv/2I35.csv")
    dfp=pd.read_csv("./list/csv_p/2I35_prop.csv")
    df_rmsd = dfp["r_i_glide_rmsd_to_input"]
    df_sum = pd.concat([df, df_rmsd], axis=1)
    Matrix_2I35 = df_sum
    df=pd.read_csv("./list/csv/2RH1.csv")
    dfp=pd.read_csv("./list/csv_p/2RH1_prop.csv")
    df_rmsd = dfp["r_i_glide_rmsd_to_input"]
    df_sum = pd.concat([df, df_rmsd], axis=1)
    Matrix_2RH1 = df_sum
    df=pd.read_csv("./list/csv/2VT4.csv")
    dfp=pd.read_csv("./list/csv_p/2VT4_prop.csv")
    df_rmsd = dfp["r_i_glide_rmsd_to_input"]
    df_sum = pd.concat([df, df_rmsd], axis=1)
    Matrix_2VT4 = df_sum
    


```python
df=pd.read_csv("./list/csv/2I35.csv")
dfp=pd.read_csv("./list/csv_p/2I35_prop.csv")
df_rmsd = dfp["r_i_glide_rmsd_to_input"]
df_sum = pd.concat([df, df_rmsd], axis=1)
Matrix_2I35 = df_sum
df=pd.read_csv("./list/csv/2RH1.csv")
dfp=pd.read_csv("./list/csv_p/2RH1_prop.csv")
df_rmsd = dfp["r_i_glide_rmsd_to_input"]
df_sum = pd.concat([df, df_rmsd], axis=1)
Matrix_2RH1 = df_sum
df=pd.read_csv("./list/csv/2VT4.csv")
dfp=pd.read_csv("./list/csv_p/2VT4_prop.csv")
df_rmsd = dfp["r_i_glide_rmsd_to_input"]
df_sum = pd.concat([df, df_rmsd], axis=1)
Matrix_2VT4 = df_sum
```


```python
'Matrix_'i[0:4].to_csv("Matrix_",i,)
```


```python
print('Matrix_'+i[0:4],"= df_sum")
```


```python
for i,j in zip(csv_list,csvp_list):
    print('Matrix_'+i[0:4]+'.to_csv("Matrix_'+i[0:4]+'.csv", index = False)')
```

    Matrix_2I35.to_csv("Matrix_2I35.csv", index = False)
    Matrix_2RH1.to_csv("Matrix_2RH1.csv", index = False)
    Matrix_2VT4.to_csv("Matrix_2VT4.csv", index = False)
    


```python
Matrix_2I35.to_csv("Matrix_2I35.csv", index = False)
Matrix_2RH1.to_csv("Matrix_2RH1.csv", index = False)
Matrix_2VT4.to_csv("Matrix_2VT4.csv", index = False)
```


```python

```
