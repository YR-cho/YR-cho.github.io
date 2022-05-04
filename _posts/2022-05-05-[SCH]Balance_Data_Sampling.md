## 특정 조건을 만족하는 데이터 행을 추출


```python
import os
import pandas as pd
```


```python
df=pd.read_csv("./MATRIX/Matrix_2I35.csv")
```


```python

```


```python
df["r_i_glide_rmsd_to_input"] <= 2.0 ## 해당 컬럼값을 bool type으로 변경가능
```




    0    False
    1     True
    2    False
    3    False
    Name: r_i_glide_rmsd_to_input, dtype: bool




```python
df[df["r_i_glide_rmsd_to_input"] <= 2.0] ## 조건문을 사용하고 bool 전체를 대괄호로 감싼다.
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
  </tbody>
</table>
<p>1 rows × 2945 columns</p>
</div>




```python
df[df["r_i_glide_rmsd_to_input"] > 2.0] ## 조건문을 사용하고 bool 전체를 대괄호로 감싼다.
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
<p>3 rows × 2945 columns</p>
</div>



[참고 홈페이지](https://kimdingko-world.tistory.com/206)

## 해당 Matrix 데이터에서 랜덤하게 sampling하기


```python
df_N = df[df["r_i_glide_rmsd_to_input"] > 2.0]
```


```python
df_N.sample(n=3,replace=False) ### replace를 False로 설정하면 중복데이터는 추출하지 않는다.
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
      <th>s_pdb_PDB_CRYST1_Space_Group</th>
      <th>s_pdb_PDB_DEPOSITION_DATE</th>
      <th>s_pdb_PDB_EXPDTA</th>
      <th>s_pdb_PDB_ID</th>
      <th>s_pdb_PDB_REMARK_350_Biomolecule_1_Transform_1_Chains</th>
      <th>s_pdb_PDB_REMARK_350_Biomolecule_1_Transform_1_Matrix_1</th>
      <th>s_pdb_PDB_TITLE</th>
      <th>s_pdb_PDB_format_version</th>
      <th>s_ppw_het_states</th>
      <th>s_ppw_prepared_with_version</th>
    </tr>
  </thead>
  <tbody>
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
      <td>H 3 2</td>
      <td>17-AUG-06</td>
      <td>X-RAY DIFFRACTION</td>
      <td>2I35</td>
      <td>A</td>
      <td>1.000000 0.000000 0.000000   0.000000;0.000000...</td>
      <td>CRYSTAL STRUCTURE OF RHOMBOHEDRAL CRYSTAL FORM...</td>
      <td>3.3</td>
      <td>eJztms1uGzEMhF/F8DkNlvqj1Fcp+gZBbz0Feffukt79ZK...</td>
      <td>2021-1</td>
    </tr>
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
      <td>H 3 2</td>
      <td>17-AUG-06</td>
      <td>X-RAY DIFFRACTION</td>
      <td>2I35</td>
      <td>A</td>
      <td>1.000000 0.000000 0.000000   0.000000;0.000000...</td>
      <td>CRYSTAL STRUCTURE OF RHOMBOHEDRAL CRYSTAL FORM...</td>
      <td>3.3</td>
      <td>eJztms1uGzEMhF/F8DkNlvqj1Fcp+gZBbz0Feffukt79ZK...</td>
      <td>2021-1</td>
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
      <td>H 3 2</td>
      <td>17-AUG-06</td>
      <td>X-RAY DIFFRACTION</td>
      <td>2I35</td>
      <td>A</td>
      <td>1.000000 0.000000 0.000000   0.000000;0.000000...</td>
      <td>CRYSTAL STRUCTURE OF RHOMBOHEDRAL CRYSTAL FORM...</td>
      <td>3.3</td>
      <td>eJztms1uGzEMhF/F8DkNlvqj1Fcp+gZBbz0Feffukt79ZK...</td>
      <td>2021-1</td>
    </tr>
  </tbody>
</table>
<p>3 rows × 3010 columns</p>
</div>




```python

```

## 많은 파일에 적용


```python
path = "./MATRIX_198" 
file_list = os.listdir(path) # 파일 이름 리스트로 설정
```


```python
for i in file_list:
    print('df=pd.read_csv("./MATRIX_198/'+i+'")')
    print('df["r_i_glide_rmsd_to_input"] <= 2.0')  ## 조건문을 사용하고 bool 전체를 대괄호로 감싼다.
    print('T_'+i[7:11],'= df[df["r_i_glide_rmsd_to_input"] <= 2.0]') ## PDB_N 이름으로 변수명 설정
    print('T_'+i[7:11],'=','T_'+i[7:11]+'.sample(n=10,replace=True)')  ### 추출 또는 생성 Matrix 수를 n 으로 설정할 수 있음 positive같은 데이터 수가 매우 작을뿐만아닌 상호작용이 매우 비슷하기 때문에 중복을 허용하였다.
    print('df["r_i_glide_rmsd_to_input"] > 2.0')  ## 조건문을 사용하고 bool 전체를 대괄호로 감싼다.
    print('N_'+i[7:11],'= df[df["r_i_glide_rmsd_to_input"] > 2.0]') ## PDB_N 이름으로 negative 변수명 설정
    print('N_'+i[7:11],'=','N_'+i[7:11]+'.sample(n=10,replace=True)') ## negative 데이터는 positive에 비해 굉장히 많기 때문에 중복을 허용하지 않아야한다.
```

    df=pd.read_csv("./MATRIX_198/Matrix_2I35.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2I35 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2I35 = T_2I35.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2I35 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2I35 = N_2I35.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_2RH1.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2RH1 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2RH1 = T_2RH1.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2RH1 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2RH1 = N_2RH1.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_2VT4.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2VT4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2VT4 = T_2VT4.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2VT4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2VT4 = N_2VT4.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_2X72.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2X72 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2X72 = T_2X72.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2X72 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2X72 = N_2X72.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_2Y00.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2Y00 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2Y00 = T_2Y00.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2Y00 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2Y00 = N_2Y00.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_2Y01.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2Y01 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2Y01 = T_2Y01.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2Y01 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2Y01 = N_2Y01.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_2Y02.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2Y02 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2Y02 = T_2Y02.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2Y02 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2Y02 = N_2Y02.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_2Y03.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2Y03 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2Y03 = T_2Y03.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2Y03 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2Y03 = N_2Y03.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_2Y04.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2Y04 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2Y04 = T_2Y04.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2Y04 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2Y04 = N_2Y04.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_2YCW.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2YCW = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2YCW = T_2YCW.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2YCW = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2YCW = N_2YCW.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_2YCX.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2YCX = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2YCX = T_2YCX.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2YCX = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2YCX = N_2YCX.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_2YCY.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2YCY = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2YCY = T_2YCY.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2YCY = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2YCY = N_2YCY.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_2YCZ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2YCZ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2YCZ = T_2YCZ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2YCZ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2YCZ = N_2YCZ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_2YDV.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_2YDV = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_2YDV = T_2YDV.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_2YDV = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_2YDV = N_2YDV.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_3D4S.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_3D4S = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_3D4S = T_3D4S.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_3D4S = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_3D4S = N_3D4S.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_3NY8.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_3NY8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_3NY8 = T_3NY8.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_3NY8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_3NY8 = N_3NY8.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_3NY9.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_3NY9 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_3NY9 = T_3NY9.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_3NY9 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_3NY9 = N_3NY9.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_3NYA.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_3NYA = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_3NYA = T_3NYA.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_3NYA = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_3NYA = N_3NYA.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_3OE8.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_3OE8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_3OE8 = T_3OE8.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_3OE8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_3OE8 = N_3OE8.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_3P0G.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_3P0G = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_3P0G = T_3P0G.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_3P0G = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_3P0G = N_3P0G.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_3UON.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_3UON = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_3UON = T_3UON.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_3UON = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_3UON = N_3UON.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_3V2W.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_3V2W = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_3V2W = T_3V2W.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_3V2W = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_3V2W = N_3V2W.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_3V2Y.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_3V2Y = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_3V2Y = T_3V2Y.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_3V2Y = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_3V2Y = N_3V2Y.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_3VGA.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_3VGA = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_3VGA = T_3VGA.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_3VGA = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_3VGA = N_3VGA.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_3VW7.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_3VW7 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_3VW7 = T_3VW7.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_3VW7 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_3VW7 = N_3VW7.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_3ZPQ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_3ZPQ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_3ZPQ = T_3ZPQ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_3ZPQ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_3ZPQ = N_3ZPQ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_3ZPR.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_3ZPR = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_3ZPR = T_3ZPR.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_3ZPR = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_3ZPR = N_3ZPR.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4AMJ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4AMJ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4AMJ = T_4AMJ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4AMJ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4AMJ = N_4AMJ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4BVN.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4BVN = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4BVN = T_4BVN.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4BVN = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4BVN = N_4BVN.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4DAJ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4DAJ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4DAJ = T_4DAJ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4DAJ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4DAJ = N_4DAJ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4EA3.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4EA3 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4EA3 = T_4EA3.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4EA3 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4EA3 = N_4EA3.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4EIY.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4EIY = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4EIY = T_4EIY.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4EIY = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4EIY = N_4EIY.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4EJ4.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4EJ4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4EJ4 = T_4EJ4.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4EJ4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4EJ4 = N_4EJ4.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4GBR.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4GBR = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4GBR = T_4GBR.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4GBR = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4GBR = N_4GBR.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4IAQ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4IAQ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4IAQ = T_4IAQ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4IAQ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4IAQ = N_4IAQ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4IAR.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4IAR = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4IAR = T_4IAR.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4IAR = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4IAR = N_4IAR.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4IB4.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4IB4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4IB4 = T_4IB4.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4IB4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4IB4 = N_4IB4.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4JKV.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4JKV = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4JKV = T_4JKV.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4JKV = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4JKV = N_4JKV.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4K5Y.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4K5Y = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4K5Y = T_4K5Y.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4K5Y = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4K5Y = N_4K5Y.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4LDE.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4LDE = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4LDE = T_4LDE.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4LDE = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4LDE = N_4LDE.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4LDL.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4LDL = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4LDL = T_4LDL.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4LDL = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4LDL = N_4LDL.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4LDO.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4LDO = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4LDO = T_4LDO.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4LDO = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4LDO = N_4LDO.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4MBS.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4MBS = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4MBS = T_4MBS.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4MBS = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4MBS = N_4MBS.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4MQS.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4MQS = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4MQS = T_4MQS.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4MQS = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4MQS = N_4MQS.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4MQT.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4MQT = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4MQT = T_4MQT.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4MQT = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4MQT = N_4MQT.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4N4W.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4N4W = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4N4W = T_4N4W.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4N4W = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4N4W = N_4N4W.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4N6H.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4N6H = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4N6H = T_4N6H.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4N6H = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4N6H = N_4N6H.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4NTJ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4NTJ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4NTJ = T_4NTJ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4NTJ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4NTJ = N_4NTJ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4O9R.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4O9R = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4O9R = T_4O9R.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4O9R = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4O9R = N_4O9R.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4OO9.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4OO9 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4OO9 = T_4OO9.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4OO9 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4OO9 = N_4OO9.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4OR2.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4OR2 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4OR2 = T_4OR2.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4OR2 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4OR2 = N_4OR2.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4PXZ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4PXZ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4PXZ = T_4PXZ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4PXZ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4PXZ = N_4PXZ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4PY0.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4PY0 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4PY0 = T_4PY0.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4PY0 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4PY0 = N_4PY0.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4QIM.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4QIM = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4QIM = T_4QIM.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4QIM = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4QIM = N_4QIM.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4QIN.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4QIN = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4QIN = T_4QIN.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4QIN = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4QIN = N_4QIN.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4S0V.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4S0V = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4S0V = T_4S0V.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4S0V = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4S0V = N_4S0V.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4U14.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4U14 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4U14 = T_4U14.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4U14 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4U14 = N_4U14.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4U16.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4U16 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4U16 = T_4U16.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4U16 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4U16 = N_4U16.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4UG2.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4UG2 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4UG2 = T_4UG2.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4UG2 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4UG2 = N_4UG2.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4UHR.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4UHR = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4UHR = T_4UHR.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4UHR = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4UHR = N_4UHR.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4XNW.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4XNW = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4XNW = T_4XNW.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4XNW = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4XNW = N_4XNW.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4YAY.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4YAY = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4YAY = T_4YAY.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4YAY = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4YAY = N_4YAY.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4Z34.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4Z34 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4Z34 = T_4Z34.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4Z34 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4Z34 = N_4Z34.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4Z36.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4Z36 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4Z36 = T_4Z36.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4Z36 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4Z36 = N_4Z36.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4Z9G.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4Z9G = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4Z9G = T_4Z9G.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4Z9G = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4Z9G = N_4Z9G.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_4ZUD.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_4ZUD = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_4ZUD = T_4ZUD.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_4ZUD = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_4ZUD = N_4ZUD.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5C1M.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5C1M = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5C1M = T_5C1M.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5C1M = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5C1M = N_5C1M.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5CGC.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5CGC = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5CGC = T_5CGC.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5CGC = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5CGC = N_5CGC.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5CGD.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5CGD = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5CGD = T_5CGD.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5CGD = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5CGD = N_5CGD.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5CXV.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5CXV = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5CXV = T_5CXV.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5CXV = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5CXV = N_5CXV.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5D5B.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5D5B = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5D5B = T_5D5B.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5D5B = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5D5B = N_5D5B.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5D6L.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5D6L = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5D6L = T_5D6L.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5D6L = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5D6L = N_5D6L.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5DHG.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5DHG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5DHG = T_5DHG.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5DHG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5DHG = N_5DHG.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5DHH.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5DHH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5DHH = T_5DHH.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5DHH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5DHH = N_5DHH.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5DSG.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5DSG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5DSG = T_5DSG.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5DSG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5DSG = N_5DSG.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5F8U.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5F8U = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5F8U = T_5F8U.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5F8U = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5F8U = N_5F8U.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5G53.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5G53 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5G53 = T_5G53.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5G53 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5G53 = N_5G53.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5IU4.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5IU4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5IU4 = T_5IU4.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5IU4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5IU4 = N_5IU4.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5IU7.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5IU7 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5IU7 = T_5IU7.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5IU7 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5IU7 = N_5IU7.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5IU8.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5IU8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5IU8 = T_5IU8.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5IU8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5IU8 = N_5IU8.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5IUA.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5IUA = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5IUA = T_5IUA.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5IUA = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5IUA = N_5IUA.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5IUB.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5IUB = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5IUB = T_5IUB.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5IUB = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5IUB = N_5IUB.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5JQH.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5JQH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5JQH = T_5JQH.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5JQH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5JQH = N_5JQH.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5K2B.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5K2B = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5K2B = T_5K2B.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5K2B = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5K2B = N_5K2B.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5K2D.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5K2D = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5K2D = T_5K2D.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5K2D = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5K2D = N_5K2D.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5L7I.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5L7I = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5L7I = T_5L7I.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5L7I = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5L7I = N_5L7I.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5LWE.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5LWE = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5LWE = T_5LWE.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5LWE = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5LWE = N_5LWE.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5MZJ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5MZJ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5MZJ = T_5MZJ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5MZJ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5MZJ = N_5MZJ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5N2R.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5N2R = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5N2R = T_5N2R.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5N2R = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5N2R = N_5N2R.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5N2S.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5N2S = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5N2S = T_5N2S.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5N2S = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5N2S = N_5N2S.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5NDD.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5NDD = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5NDD = T_5NDD.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5NDD = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5NDD = N_5NDD.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5NLX.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5NLX = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5NLX = T_5NLX.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5NLX = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5NLX = N_5NLX.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5NM2.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5NM2 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5NM2 = T_5NM2.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5NM2 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5NM2 = N_5NM2.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5NM4.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5NM4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5NM4 = T_5NM4.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5NM4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5NM4 = N_5NM4.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5OLG.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5OLG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5OLG = T_5OLG.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5OLG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5OLG = N_5OLG.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5OLH.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5OLH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5OLH = T_5OLH.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5OLH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5OLH = N_5OLH.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5OLO.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5OLO = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5OLO = T_5OLO.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5OLO = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5OLO = N_5OLO.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5OLV.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5OLV = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5OLV = T_5OLV.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5OLV = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5OLV = N_5OLV.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5OLZ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5OLZ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5OLZ = T_5OLZ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5OLZ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5OLZ = N_5OLZ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5OM1.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5OM1 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5OM1 = T_5OM1.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5OM1 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5OM1 = N_5OM1.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5OM4.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5OM4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5OM4 = T_5OM4.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5OM4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5OM4 = N_5OM4.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5TGZ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5TGZ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5TGZ = T_5TGZ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5TGZ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5TGZ = N_5TGZ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5TUD.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5TUD = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5TUD = T_5TUD.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5TUD = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5TUD = N_5TUD.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5TVN.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5TVN = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5TVN = T_5TVN.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5TVN = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5TVN = N_5TVN.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5UIG.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5UIG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5UIG = T_5UIG.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5UIG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5UIG = N_5UIG.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5UNH.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5UNH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5UNH = T_5UNH.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5UNH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5UNH = N_5UNH.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5UVI.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5UVI = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5UVI = T_5UVI.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5UVI = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5UVI = N_5UVI.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5V54.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5V54 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5V54 = T_5V54.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5V54 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5V54 = N_5V54.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5V56.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5V56 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5V56 = T_5V56.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5V56 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5V56 = N_5V56.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5V57.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5V57 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5V57 = T_5V57.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5V57 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5V57 = N_5V57.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5VRA.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5VRA = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5VRA = T_5VRA.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5VRA = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5VRA = N_5VRA.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5WIU.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5WIU = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5WIU = T_5WIU.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5WIU = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5WIU = N_5WIU.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5WIV.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5WIV = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5WIV = T_5WIV.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5WIV = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5WIV = N_5WIV.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5X7D.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5X7D = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5X7D = T_5X7D.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5X7D = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5X7D = N_5X7D.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5XPR.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5XPR = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5XPR = T_5XPR.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5XPR = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5XPR = N_5XPR.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5XR8.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5XR8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5XR8 = T_5XR8.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5XR8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5XR8 = N_5XR8.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5XRA.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5XRA = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5XRA = T_5XRA.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5XRA = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5XRA = N_5XRA.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5ZBQ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5ZBQ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5ZBQ = T_5ZBQ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5ZBQ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5ZBQ = N_5ZBQ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5ZHP.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5ZHP = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5ZHP = T_5ZHP.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5ZHP = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5ZHP = N_5ZHP.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5ZK3.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5ZK3 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5ZK3 = T_5ZK3.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5ZK3 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5ZK3 = N_5ZK3.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5ZK8.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5ZK8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5ZK8 = T_5ZK8.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5ZK8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5ZK8 = N_5ZK8.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5ZKB.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5ZKB = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5ZKB = T_5ZKB.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5ZKB = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5ZKB = N_5ZKB.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5ZKC.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5ZKC = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5ZKC = T_5ZKC.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5ZKC = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5ZKC = N_5ZKC.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5ZKP.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5ZKP = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5ZKP = T_5ZKP.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5ZKP = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5ZKP = N_5ZKP.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5ZKQ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5ZKQ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5ZKQ = T_5ZKQ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5ZKQ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5ZKQ = N_5ZKQ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_5ZTY.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_5ZTY = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_5ZTY = T_5ZTY.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_5ZTY = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_5ZTY = N_5ZTY.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6A93.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6A93 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6A93 = T_6A93.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6A93 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6A93 = N_6A93.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6A94.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6A94 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6A94 = T_6A94.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6A94 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6A94 = N_6A94.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6AKX.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6AKX = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6AKX = T_6AKX.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6AKX = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6AKX = N_6AKX.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6B73.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6B73 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6B73 = T_6B73.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6B73 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6B73 = N_6B73.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6BQG.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6BQG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6BQG = T_6BQG.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6BQG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6BQG = N_6BQG.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6BQH.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6BQH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6BQH = T_6BQH.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6BQH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6BQH = N_6BQH.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6CM4.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6CM4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6CM4 = T_6CM4.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6CM4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6CM4 = N_6CM4.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6D26.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6D26 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6D26 = T_6D26.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6D26 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6D26 = N_6D26.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6DRX.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6DRX = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6DRX = T_6DRX.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6DRX = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6DRX = N_6DRX.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6DRY.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6DRY = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6DRY = T_6DRY.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6DRY = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6DRY = N_6DRY.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6DRZ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6DRZ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6DRZ = T_6DRZ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6DRZ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6DRZ = N_6DRZ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6DS0.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6DS0 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6DS0 = T_6DS0.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6DS0 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6DS0 = N_6DS0.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6E59.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6E59 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6E59 = T_6E59.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6E59 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6E59 = N_6E59.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6E67.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6E67 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6E67 = T_6E67.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6E67 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6E67 = N_6E67.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6FFH.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6FFH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6FFH = T_6FFH.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6FFH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6FFH = N_6FFH.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6FFI.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6FFI = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6FFI = T_6FFI.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6FFI = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6FFI = N_6FFI.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6FK6.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6FK6 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6FK6 = T_6FK6.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6FK6 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6FK6 = N_6FK6.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6FK7.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6FK7 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6FK7 = T_6FK7.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6FK7 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6FK7 = N_6FK7.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6FK8.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6FK8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6FK8 = T_6FK8.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6FK8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6FK8 = N_6FK8.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6FK9.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6FK9 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6FK9 = T_6FK9.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6FK9 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6FK9 = N_6FK9.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6FKA.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6FKA = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6FKA = T_6FKA.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6FKA = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6FKA = N_6FKA.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6FKB.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6FKB = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6FKB = T_6FKB.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6FKB = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6FKB = N_6FKB.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6FKD.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6FKD = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6FKD = T_6FKD.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6FKD = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6FKD = N_6FKD.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6GDG.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6GDG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6GDG = T_6GDG.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6GDG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6GDG = N_6GDG.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6GPS.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6GPS = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6GPS = T_6GPS.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6GPS = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6GPS = N_6GPS.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6GPX.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6GPX = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6GPX = T_6GPX.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6GPX = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6GPX = N_6GPX.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6GT3.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6GT3 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6GT3 = T_6GT3.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6GT3 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6GT3 = N_6GT3.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6H7J.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6H7J = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6H7J = T_6H7J.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6H7J = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6H7J = N_6H7J.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6H7L.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6H7L = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6H7L = T_6H7L.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6H7L = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6H7L = N_6H7L.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6H7M.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6H7M = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6H7M = T_6H7M.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6H7M = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6H7M = N_6H7M.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6H7N.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6H7N = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6H7N = T_6H7N.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6H7N = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6H7N = N_6H7N.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6H7O.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6H7O = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6H7O = T_6H7O.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6H7O = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6H7O = N_6H7O.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6HLL.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6HLL = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6HLL = T_6HLL.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6HLL = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6HLL = N_6HLL.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6HLO.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6HLO = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6HLO = T_6HLO.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6HLO = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6HLO = N_6HLO.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6HLP.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6HLP = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6HLP = T_6HLP.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6HLP = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6HLP = N_6HLP.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6IBL.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6IBL = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6IBL = T_6IBL.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6IBL = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6IBL = N_6IBL.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6IIU.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6IIU = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6IIU = T_6IIU.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6IIU = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6IIU = N_6IIU.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6IIV.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6IIV = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6IIV = T_6IIV.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6IIV = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6IIV = N_6IIV.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6IQL.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6IQL = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6IQL = T_6IQL.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6IQL = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6IQL = N_6IQL.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6J20.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6J20 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6J20 = T_6J20.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6J20 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6J20 = N_6J20.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6JZH.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6JZH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6JZH = T_6JZH.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6JZH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6JZH = N_6JZH.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6K1Q.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6K1Q = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6K1Q = T_6K1Q.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6K1Q = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6K1Q = N_6K1Q.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6M9T.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6M9T = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6M9T = T_6M9T.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6M9T = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6M9T = N_6M9T.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6ME2.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6ME2 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6ME2 = T_6ME2.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6ME2 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6ME2 = N_6ME2.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6ME3.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6ME3 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6ME3 = T_6ME3.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6ME3 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6ME3 = N_6ME3.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6ME4.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6ME4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6ME4 = T_6ME4.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6ME4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6ME4 = N_6ME4.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6ME5.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6ME5 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6ME5 = T_6ME5.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6ME5 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6ME5 = N_6ME5.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6ME6.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6ME6 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6ME6 = T_6ME6.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6ME6 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6ME6 = N_6ME6.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6ME7.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6ME7 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6ME7 = T_6ME7.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6ME7 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6ME7 = N_6ME7.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6ME8.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6ME8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6ME8 = T_6ME8.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6ME8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6ME8 = N_6ME8.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6ME9.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6ME9 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6ME9 = T_6ME9.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6ME9 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6ME9 = N_6ME9.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6MH8.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6MH8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6MH8 = T_6MH8.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6MH8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6MH8 = N_6MH8.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6MXT.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6MXT = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6MXT = T_6MXT.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6MXT = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6MXT = N_6MXT.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6N48.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6N48 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6N48 = T_6N48.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6N48 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6N48 = N_6N48.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6OL9.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6OL9 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6OL9 = T_6OL9.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6OL9 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6OL9 = N_6OL9.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6PRZ.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6PRZ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6PRZ = T_6PRZ.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6PRZ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6PRZ = N_6PRZ.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6PS0.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6PS0 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6PS0 = T_6PS0.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6PS0 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6PS0 = N_6PS0.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6PS1.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6PS1 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6PS1 = T_6PS1.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6PS1 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6PS1 = N_6PS1.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6PS2.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6PS2 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6PS2 = T_6PS2.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6PS2 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6PS2 = N_6PS2.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6PS3.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6PS3 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6PS3 = T_6PS3.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6PS3 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6PS3 = N_6PS3.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6PS4.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6PS4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6PS4 = T_6PS4.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6PS4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6PS4 = N_6PS4.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6PS5.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6PS5 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6PS5 = T_6PS5.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6PS5 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6PS5 = N_6PS5.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6PS6.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6PS6 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6PS6 = T_6PS6.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6PS6 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6PS6 = N_6PS6.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6PS7.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6PS7 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6PS7 = T_6PS7.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6PS7 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6PS7 = N_6PS7.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6PS8.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6PS8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6PS8 = T_6PS8.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6PS8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6PS8 = N_6PS8.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6QZH.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6QZH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6QZH = T_6QZH.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6QZH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6QZH = N_6QZH.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6RZ4.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6RZ4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6RZ4 = T_6RZ4.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6RZ4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6RZ4 = N_6RZ4.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6TP3.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6TP3 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6TP3 = T_6TP3.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6TP3 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6TP3 = N_6TP3.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6TP4.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6TP4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6TP4 = T_6TP4.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6TP4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6TP4 = N_6TP4.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6TP6.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6TP6 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6TP6 = T_6TP6.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6TP6 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6TP6 = N_6TP6.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6TPG.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6TPG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6TPG = T_6TPG.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6TPG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6TPG = N_6TPG.sample(n=10,replace=True)
    df=pd.read_csv("./MATRIX_198/Matrix_6TPN.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    T_6TPN = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    T_6TPN = T_6TPN.sample(n=10,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    N_6TPN = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    N_6TPN = N_6TPN.sample(n=10,replace=True)
    


```python
df=pd.read_csv("./MATRIX_198/Matrix_2I35.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2I35 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2I35 = T_2I35.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2I35 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2I35 = N_2I35.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_2RH1.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2RH1 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2RH1 = T_2RH1.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2RH1 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2RH1 = N_2RH1.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_2VT4.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2VT4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2VT4 = T_2VT4.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2VT4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2VT4 = N_2VT4.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_2X72.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2X72 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2X72 = T_2X72.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2X72 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2X72 = N_2X72.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_2Y00.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2Y00 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2Y00 = T_2Y00.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2Y00 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2Y00 = N_2Y00.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_2Y01.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2Y01 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2Y01 = T_2Y01.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2Y01 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2Y01 = N_2Y01.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_2Y02.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2Y02 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2Y02 = T_2Y02.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2Y02 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2Y02 = N_2Y02.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_2Y03.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2Y03 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2Y03 = T_2Y03.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2Y03 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2Y03 = N_2Y03.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_2Y04.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2Y04 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2Y04 = T_2Y04.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2Y04 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2Y04 = N_2Y04.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_2YCW.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2YCW = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2YCW = T_2YCW.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2YCW = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2YCW = N_2YCW.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_2YCX.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2YCX = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2YCX = T_2YCX.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2YCX = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2YCX = N_2YCX.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_2YCY.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2YCY = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2YCY = T_2YCY.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2YCY = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2YCY = N_2YCY.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_2YCZ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2YCZ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2YCZ = T_2YCZ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2YCZ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2YCZ = N_2YCZ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_2YDV.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_2YDV = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_2YDV = T_2YDV.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_2YDV = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_2YDV = N_2YDV.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_3D4S.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_3D4S = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_3D4S = T_3D4S.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_3D4S = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_3D4S = N_3D4S.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_3NY8.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_3NY8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_3NY8 = T_3NY8.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_3NY8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_3NY8 = N_3NY8.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_3NY9.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_3NY9 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_3NY9 = T_3NY9.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_3NY9 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_3NY9 = N_3NY9.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_3NYA.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_3NYA = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_3NYA = T_3NYA.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_3NYA = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_3NYA = N_3NYA.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_3OE8.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_3OE8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_3OE8 = T_3OE8.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_3OE8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_3OE8 = N_3OE8.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_3P0G.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_3P0G = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_3P0G = T_3P0G.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_3P0G = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_3P0G = N_3P0G.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_3UON.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_3UON = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_3UON = T_3UON.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_3UON = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_3UON = N_3UON.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_3V2W.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_3V2W = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_3V2W = T_3V2W.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_3V2W = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_3V2W = N_3V2W.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_3V2Y.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_3V2Y = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_3V2Y = T_3V2Y.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_3V2Y = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_3V2Y = N_3V2Y.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_3VGA.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_3VGA = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_3VGA = T_3VGA.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_3VGA = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_3VGA = N_3VGA.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_3VW7.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_3VW7 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_3VW7 = T_3VW7.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_3VW7 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_3VW7 = N_3VW7.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_3ZPQ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_3ZPQ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_3ZPQ = T_3ZPQ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_3ZPQ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_3ZPQ = N_3ZPQ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_3ZPR.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_3ZPR = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_3ZPR = T_3ZPR.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_3ZPR = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_3ZPR = N_3ZPR.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4AMJ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4AMJ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4AMJ = T_4AMJ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4AMJ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4AMJ = N_4AMJ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4BVN.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4BVN = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4BVN = T_4BVN.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4BVN = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4BVN = N_4BVN.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4DAJ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4DAJ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4DAJ = T_4DAJ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4DAJ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4DAJ = N_4DAJ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4EA3.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4EA3 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4EA3 = T_4EA3.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4EA3 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4EA3 = N_4EA3.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4EIY.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4EIY = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4EIY = T_4EIY.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4EIY = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4EIY = N_4EIY.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4EJ4.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4EJ4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4EJ4 = T_4EJ4.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4EJ4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4EJ4 = N_4EJ4.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4GBR.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4GBR = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4GBR = T_4GBR.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4GBR = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4GBR = N_4GBR.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4IAQ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4IAQ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4IAQ = T_4IAQ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4IAQ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4IAQ = N_4IAQ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4IAR.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4IAR = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4IAR = T_4IAR.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4IAR = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4IAR = N_4IAR.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4IB4.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4IB4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4IB4 = T_4IB4.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4IB4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4IB4 = N_4IB4.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4JKV.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4JKV = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4JKV = T_4JKV.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4JKV = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4JKV = N_4JKV.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4K5Y.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4K5Y = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4K5Y = T_4K5Y.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4K5Y = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4K5Y = N_4K5Y.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4LDE.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4LDE = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4LDE = T_4LDE.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4LDE = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4LDE = N_4LDE.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4LDL.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4LDL = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4LDL = T_4LDL.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4LDL = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4LDL = N_4LDL.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4LDO.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4LDO = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4LDO = T_4LDO.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4LDO = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4LDO = N_4LDO.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4MBS.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4MBS = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4MBS = T_4MBS.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4MBS = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4MBS = N_4MBS.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4MQS.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4MQS = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4MQS = T_4MQS.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4MQS = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4MQS = N_4MQS.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4MQT.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4MQT = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4MQT = T_4MQT.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4MQT = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4MQT = N_4MQT.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4N4W.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4N4W = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4N4W = T_4N4W.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4N4W = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4N4W = N_4N4W.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4N6H.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4N6H = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4N6H = T_4N6H.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4N6H = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4N6H = N_4N6H.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4NTJ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4NTJ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4NTJ = T_4NTJ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4NTJ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4NTJ = N_4NTJ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4O9R.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4O9R = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4O9R = T_4O9R.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4O9R = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4O9R = N_4O9R.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4OO9.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4OO9 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4OO9 = T_4OO9.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4OO9 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4OO9 = N_4OO9.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4OR2.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4OR2 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4OR2 = T_4OR2.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4OR2 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4OR2 = N_4OR2.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4PXZ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4PXZ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4PXZ = T_4PXZ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4PXZ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4PXZ = N_4PXZ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4PY0.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4PY0 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4PY0 = T_4PY0.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4PY0 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4PY0 = N_4PY0.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4QIM.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4QIM = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4QIM = T_4QIM.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4QIM = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4QIM = N_4QIM.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4QIN.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4QIN = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4QIN = T_4QIN.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4QIN = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4QIN = N_4QIN.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4S0V.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4S0V = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4S0V = T_4S0V.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4S0V = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4S0V = N_4S0V.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4U14.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4U14 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4U14 = T_4U14.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4U14 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4U14 = N_4U14.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4U16.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4U16 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4U16 = T_4U16.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4U16 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4U16 = N_4U16.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4UG2.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4UG2 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4UG2 = T_4UG2.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4UG2 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4UG2 = N_4UG2.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4UHR.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4UHR = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4UHR = T_4UHR.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4UHR = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4UHR = N_4UHR.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4XNW.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4XNW = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4XNW = T_4XNW.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4XNW = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4XNW = N_4XNW.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4YAY.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4YAY = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4YAY = T_4YAY.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4YAY = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4YAY = N_4YAY.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4Z34.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4Z34 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4Z34 = T_4Z34.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4Z34 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4Z34 = N_4Z34.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4Z36.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4Z36 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4Z36 = T_4Z36.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4Z36 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4Z36 = N_4Z36.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4Z9G.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4Z9G = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4Z9G = T_4Z9G.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4Z9G = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4Z9G = N_4Z9G.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_4ZUD.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_4ZUD = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_4ZUD = T_4ZUD.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_4ZUD = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_4ZUD = N_4ZUD.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5C1M.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5C1M = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5C1M = T_5C1M.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5C1M = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5C1M = N_5C1M.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5CGC.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5CGC = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5CGC = T_5CGC.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5CGC = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5CGC = N_5CGC.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5CGD.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5CGD = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5CGD = T_5CGD.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5CGD = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5CGD = N_5CGD.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5CXV.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5CXV = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5CXV = T_5CXV.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5CXV = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5CXV = N_5CXV.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5D5B.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5D5B = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5D5B = T_5D5B.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5D5B = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5D5B = N_5D5B.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5D6L.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5D6L = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5D6L = T_5D6L.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5D6L = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5D6L = N_5D6L.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5DHG.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5DHG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5DHG = T_5DHG.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5DHG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5DHG = N_5DHG.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5DHH.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5DHH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5DHH = T_5DHH.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5DHH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5DHH = N_5DHH.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5DSG.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5DSG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5DSG = T_5DSG.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5DSG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5DSG = N_5DSG.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5F8U.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5F8U = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5F8U = T_5F8U.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5F8U = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5F8U = N_5F8U.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5G53.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5G53 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5G53 = T_5G53.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5G53 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5G53 = N_5G53.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5IU4.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5IU4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5IU4 = T_5IU4.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5IU4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5IU4 = N_5IU4.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5IU7.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5IU7 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5IU7 = T_5IU7.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5IU7 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5IU7 = N_5IU7.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5IU8.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5IU8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5IU8 = T_5IU8.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5IU8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5IU8 = N_5IU8.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5IUA.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5IUA = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5IUA = T_5IUA.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5IUA = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5IUA = N_5IUA.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5IUB.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5IUB = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5IUB = T_5IUB.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5IUB = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5IUB = N_5IUB.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5JQH.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5JQH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5JQH = T_5JQH.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5JQH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5JQH = N_5JQH.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5K2B.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5K2B = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5K2B = T_5K2B.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5K2B = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5K2B = N_5K2B.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5K2D.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5K2D = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5K2D = T_5K2D.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5K2D = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5K2D = N_5K2D.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5L7I.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5L7I = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5L7I = T_5L7I.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5L7I = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5L7I = N_5L7I.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5LWE.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5LWE = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5LWE = T_5LWE.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5LWE = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5LWE = N_5LWE.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5MZJ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5MZJ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5MZJ = T_5MZJ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5MZJ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5MZJ = N_5MZJ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5N2R.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5N2R = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5N2R = T_5N2R.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5N2R = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5N2R = N_5N2R.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5N2S.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5N2S = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5N2S = T_5N2S.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5N2S = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5N2S = N_5N2S.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5NDD.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5NDD = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5NDD = T_5NDD.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5NDD = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5NDD = N_5NDD.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5NLX.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5NLX = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5NLX = T_5NLX.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5NLX = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5NLX = N_5NLX.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5NM2.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5NM2 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5NM2 = T_5NM2.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5NM2 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5NM2 = N_5NM2.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5NM4.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5NM4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5NM4 = T_5NM4.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5NM4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5NM4 = N_5NM4.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5OLG.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5OLG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5OLG = T_5OLG.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5OLG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5OLG = N_5OLG.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5OLH.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5OLH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5OLH = T_5OLH.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5OLH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5OLH = N_5OLH.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5OLO.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5OLO = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5OLO = T_5OLO.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5OLO = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5OLO = N_5OLO.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5OLV.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5OLV = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5OLV = T_5OLV.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5OLV = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5OLV = N_5OLV.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5OLZ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5OLZ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5OLZ = T_5OLZ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5OLZ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5OLZ = N_5OLZ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5OM1.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5OM1 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5OM1 = T_5OM1.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5OM1 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5OM1 = N_5OM1.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5OM4.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5OM4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5OM4 = T_5OM4.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5OM4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5OM4 = N_5OM4.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5TGZ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5TGZ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5TGZ = T_5TGZ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5TGZ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5TGZ = N_5TGZ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5TUD.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5TUD = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5TUD = T_5TUD.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5TUD = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5TUD = N_5TUD.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5TVN.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5TVN = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5TVN = T_5TVN.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5TVN = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5TVN = N_5TVN.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5UIG.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5UIG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5UIG = T_5UIG.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5UIG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5UIG = N_5UIG.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5UNH.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5UNH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5UNH = T_5UNH.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5UNH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5UNH = N_5UNH.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5UVI.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5UVI = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5UVI = T_5UVI.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5UVI = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5UVI = N_5UVI.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5V54.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5V54 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5V54 = T_5V54.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5V54 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5V54 = N_5V54.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5V56.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5V56 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5V56 = T_5V56.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5V56 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5V56 = N_5V56.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5V57.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5V57 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5V57 = T_5V57.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5V57 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5V57 = N_5V57.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5VRA.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5VRA = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5VRA = T_5VRA.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5VRA = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5VRA = N_5VRA.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5WIU.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5WIU = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5WIU = T_5WIU.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5WIU = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5WIU = N_5WIU.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5WIV.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5WIV = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5WIV = T_5WIV.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5WIV = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5WIV = N_5WIV.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5X7D.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5X7D = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5X7D = T_5X7D.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5X7D = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5X7D = N_5X7D.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5XPR.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5XPR = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5XPR = T_5XPR.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5XPR = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5XPR = N_5XPR.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5XR8.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5XR8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5XR8 = T_5XR8.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5XR8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5XR8 = N_5XR8.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5XRA.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5XRA = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5XRA = T_5XRA.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5XRA = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5XRA = N_5XRA.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5ZBQ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5ZBQ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5ZBQ = T_5ZBQ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5ZBQ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5ZBQ = N_5ZBQ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5ZHP.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5ZHP = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5ZHP = T_5ZHP.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5ZHP = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5ZHP = N_5ZHP.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5ZK3.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5ZK3 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5ZK3 = T_5ZK3.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5ZK3 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5ZK3 = N_5ZK3.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5ZK8.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5ZK8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5ZK8 = T_5ZK8.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5ZK8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5ZK8 = N_5ZK8.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5ZKB.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5ZKB = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5ZKB = T_5ZKB.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5ZKB = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5ZKB = N_5ZKB.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5ZKC.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5ZKC = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5ZKC = T_5ZKC.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5ZKC = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5ZKC = N_5ZKC.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5ZKP.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5ZKP = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5ZKP = T_5ZKP.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5ZKP = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5ZKP = N_5ZKP.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5ZKQ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5ZKQ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5ZKQ = T_5ZKQ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5ZKQ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5ZKQ = N_5ZKQ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_5ZTY.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_5ZTY = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_5ZTY = T_5ZTY.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_5ZTY = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_5ZTY = N_5ZTY.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6A93.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6A93 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6A93 = T_6A93.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6A93 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6A93 = N_6A93.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6A94.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6A94 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6A94 = T_6A94.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6A94 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6A94 = N_6A94.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6AKX.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6AKX = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6AKX = T_6AKX.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6AKX = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6AKX = N_6AKX.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6B73.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6B73 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6B73 = T_6B73.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6B73 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6B73 = N_6B73.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6BQG.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6BQG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6BQG = T_6BQG.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6BQG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6BQG = N_6BQG.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6BQH.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6BQH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6BQH = T_6BQH.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6BQH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6BQH = N_6BQH.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6CM4.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6CM4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6CM4 = T_6CM4.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6CM4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6CM4 = N_6CM4.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6D26.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6D26 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6D26 = T_6D26.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6D26 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6D26 = N_6D26.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6DRX.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6DRX = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6DRX = T_6DRX.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6DRX = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6DRX = N_6DRX.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6DRY.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6DRY = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6DRY = T_6DRY.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6DRY = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6DRY = N_6DRY.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6DRZ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6DRZ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6DRZ = T_6DRZ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6DRZ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6DRZ = N_6DRZ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6DS0.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6DS0 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6DS0 = T_6DS0.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6DS0 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6DS0 = N_6DS0.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6E59.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6E59 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6E59 = T_6E59.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6E59 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6E59 = N_6E59.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6E67.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6E67 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6E67 = T_6E67.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6E67 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6E67 = N_6E67.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6FFH.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6FFH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6FFH = T_6FFH.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6FFH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6FFH = N_6FFH.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6FFI.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6FFI = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6FFI = T_6FFI.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6FFI = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6FFI = N_6FFI.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6FK6.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6FK6 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6FK6 = T_6FK6.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6FK6 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6FK6 = N_6FK6.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6FK7.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6FK7 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6FK7 = T_6FK7.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6FK7 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6FK7 = N_6FK7.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6FK8.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6FK8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6FK8 = T_6FK8.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6FK8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6FK8 = N_6FK8.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6FK9.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6FK9 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6FK9 = T_6FK9.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6FK9 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6FK9 = N_6FK9.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6FKA.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6FKA = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6FKA = T_6FKA.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6FKA = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6FKA = N_6FKA.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6FKB.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6FKB = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6FKB = T_6FKB.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6FKB = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6FKB = N_6FKB.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6FKD.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6FKD = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6FKD = T_6FKD.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6FKD = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6FKD = N_6FKD.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6GDG.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6GDG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6GDG = T_6GDG.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6GDG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6GDG = N_6GDG.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6GPS.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6GPS = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6GPS = T_6GPS.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6GPS = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6GPS = N_6GPS.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6GPX.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6GPX = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6GPX = T_6GPX.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6GPX = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6GPX = N_6GPX.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6GT3.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6GT3 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6GT3 = T_6GT3.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6GT3 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6GT3 = N_6GT3.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6H7J.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6H7J = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6H7J = T_6H7J.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6H7J = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6H7J = N_6H7J.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6H7L.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6H7L = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6H7L = T_6H7L.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6H7L = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6H7L = N_6H7L.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6H7M.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6H7M = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6H7M = T_6H7M.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6H7M = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6H7M = N_6H7M.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6H7N.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6H7N = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6H7N = T_6H7N.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6H7N = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6H7N = N_6H7N.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6H7O.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6H7O = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6H7O = T_6H7O.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6H7O = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6H7O = N_6H7O.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6HLL.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6HLL = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6HLL = T_6HLL.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6HLL = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6HLL = N_6HLL.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6HLO.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6HLO = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6HLO = T_6HLO.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6HLO = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6HLO = N_6HLO.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6HLP.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6HLP = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6HLP = T_6HLP.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6HLP = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6HLP = N_6HLP.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6IBL.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6IBL = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6IBL = T_6IBL.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6IBL = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6IBL = N_6IBL.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6IIU.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6IIU = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6IIU = T_6IIU.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6IIU = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6IIU = N_6IIU.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6IIV.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6IIV = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6IIV = T_6IIV.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6IIV = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6IIV = N_6IIV.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6IQL.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6IQL = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6IQL = T_6IQL.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6IQL = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6IQL = N_6IQL.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6J20.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6J20 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6J20 = T_6J20.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6J20 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6J20 = N_6J20.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6JZH.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6JZH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6JZH = T_6JZH.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6JZH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6JZH = N_6JZH.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6K1Q.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6K1Q = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6K1Q = T_6K1Q.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6K1Q = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6K1Q = N_6K1Q.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6M9T.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6M9T = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6M9T = T_6M9T.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6M9T = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6M9T = N_6M9T.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6ME2.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6ME2 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6ME2 = T_6ME2.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6ME2 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6ME2 = N_6ME2.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6ME3.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6ME3 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6ME3 = T_6ME3.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6ME3 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6ME3 = N_6ME3.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6ME4.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6ME4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6ME4 = T_6ME4.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6ME4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6ME4 = N_6ME4.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6ME5.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6ME5 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6ME5 = T_6ME5.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6ME5 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6ME5 = N_6ME5.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6ME6.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6ME6 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6ME6 = T_6ME6.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6ME6 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6ME6 = N_6ME6.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6ME7.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6ME7 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6ME7 = T_6ME7.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6ME7 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6ME7 = N_6ME7.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6ME8.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6ME8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6ME8 = T_6ME8.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6ME8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6ME8 = N_6ME8.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6ME9.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6ME9 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6ME9 = T_6ME9.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6ME9 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6ME9 = N_6ME9.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6MH8.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6MH8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6MH8 = T_6MH8.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6MH8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6MH8 = N_6MH8.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6MXT.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6MXT = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6MXT = T_6MXT.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6MXT = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6MXT = N_6MXT.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6N48.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6N48 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6N48 = T_6N48.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6N48 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6N48 = N_6N48.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6OL9.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6OL9 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6OL9 = T_6OL9.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6OL9 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6OL9 = N_6OL9.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6PRZ.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6PRZ = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6PRZ = T_6PRZ.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6PRZ = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6PRZ = N_6PRZ.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6PS0.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6PS0 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6PS0 = T_6PS0.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6PS0 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6PS0 = N_6PS0.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6PS1.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6PS1 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6PS1 = T_6PS1.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6PS1 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6PS1 = N_6PS1.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6PS2.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6PS2 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6PS2 = T_6PS2.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6PS2 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6PS2 = N_6PS2.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6PS3.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6PS3 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6PS3 = T_6PS3.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6PS3 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6PS3 = N_6PS3.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6PS4.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6PS4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6PS4 = T_6PS4.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6PS4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6PS4 = N_6PS4.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6PS5.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6PS5 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6PS5 = T_6PS5.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6PS5 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6PS5 = N_6PS5.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6PS6.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6PS6 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6PS6 = T_6PS6.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6PS6 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6PS6 = N_6PS6.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6PS7.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6PS7 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6PS7 = T_6PS7.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6PS7 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6PS7 = N_6PS7.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6PS8.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6PS8 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6PS8 = T_6PS8.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6PS8 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6PS8 = N_6PS8.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6QZH.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6QZH = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6QZH = T_6QZH.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6QZH = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6QZH = N_6QZH.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6RZ4.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6RZ4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6RZ4 = T_6RZ4.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6RZ4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6RZ4 = N_6RZ4.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6TP3.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6TP3 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6TP3 = T_6TP3.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6TP3 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6TP3 = N_6TP3.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6TP4.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6TP4 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6TP4 = T_6TP4.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6TP4 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6TP4 = N_6TP4.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6TP6.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6TP6 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6TP6 = T_6TP6.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6TP6 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6TP6 = N_6TP6.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6TPG.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6TPG = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6TPG = T_6TPG.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6TPG = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6TPG = N_6TPG.sample(n=10,replace=True)
df=pd.read_csv("./MATRIX_198/Matrix_6TPN.csv")
df["r_i_glide_rmsd_to_input"] <= 2.0
T_6TPN = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
T_6TPN = T_6TPN.sample(n=10,replace=True)
df["r_i_glide_rmsd_to_input"] > 2.0
N_6TPN = df[df["r_i_glide_rmsd_to_input"] > 2.0]
N_6TPN = N_6TPN.sample(n=10,replace=True)
```


```python

```


```python

```

## 데이터 프레임 합치기


```python
path = "./MATRIX_198" 
file_list = os.listdir(path) # 파일 이름 리스트로 설정
```


```python
for i in file_list:
    print('TN_'+i[7:11]+'= pd.concat([T_'+i[7:11]+', N_'+i[7:11]+'], ignore_index=True)')
    print('TN_'+i[7:11]+'.to_csv("TN_'+i[7:11]+'.csv", index = False)')
```

    TN_2I35= pd.concat([T_2I35, N_2I35], ignore_index=True)
    TN_2I35.to_csv("TN_2I35.csv", index = False)
    TN_2RH1= pd.concat([T_2RH1, N_2RH1], ignore_index=True)
    TN_2RH1.to_csv("TN_2RH1.csv", index = False)
    TN_2VT4= pd.concat([T_2VT4, N_2VT4], ignore_index=True)
    TN_2VT4.to_csv("TN_2VT4.csv", index = False)
    TN_2X72= pd.concat([T_2X72, N_2X72], ignore_index=True)
    TN_2X72.to_csv("TN_2X72.csv", index = False)
    TN_2Y00= pd.concat([T_2Y00, N_2Y00], ignore_index=True)
    TN_2Y00.to_csv("TN_2Y00.csv", index = False)
    TN_2Y01= pd.concat([T_2Y01, N_2Y01], ignore_index=True)
    TN_2Y01.to_csv("TN_2Y01.csv", index = False)
    TN_2Y02= pd.concat([T_2Y02, N_2Y02], ignore_index=True)
    TN_2Y02.to_csv("TN_2Y02.csv", index = False)
    TN_2Y03= pd.concat([T_2Y03, N_2Y03], ignore_index=True)
    TN_2Y03.to_csv("TN_2Y03.csv", index = False)
    TN_2Y04= pd.concat([T_2Y04, N_2Y04], ignore_index=True)
    TN_2Y04.to_csv("TN_2Y04.csv", index = False)
    TN_2YCW= pd.concat([T_2YCW, N_2YCW], ignore_index=True)
    TN_2YCW.to_csv("TN_2YCW.csv", index = False)
    TN_2YCX= pd.concat([T_2YCX, N_2YCX], ignore_index=True)
    TN_2YCX.to_csv("TN_2YCX.csv", index = False)
    TN_2YCY= pd.concat([T_2YCY, N_2YCY], ignore_index=True)
    TN_2YCY.to_csv("TN_2YCY.csv", index = False)
    TN_2YCZ= pd.concat([T_2YCZ, N_2YCZ], ignore_index=True)
    TN_2YCZ.to_csv("TN_2YCZ.csv", index = False)
    TN_2YDV= pd.concat([T_2YDV, N_2YDV], ignore_index=True)
    TN_2YDV.to_csv("TN_2YDV.csv", index = False)
    TN_3D4S= pd.concat([T_3D4S, N_3D4S], ignore_index=True)
    TN_3D4S.to_csv("TN_3D4S.csv", index = False)
    TN_3NY8= pd.concat([T_3NY8, N_3NY8], ignore_index=True)
    TN_3NY8.to_csv("TN_3NY8.csv", index = False)
    TN_3NY9= pd.concat([T_3NY9, N_3NY9], ignore_index=True)
    TN_3NY9.to_csv("TN_3NY9.csv", index = False)
    TN_3NYA= pd.concat([T_3NYA, N_3NYA], ignore_index=True)
    TN_3NYA.to_csv("TN_3NYA.csv", index = False)
    TN_3OE8= pd.concat([T_3OE8, N_3OE8], ignore_index=True)
    TN_3OE8.to_csv("TN_3OE8.csv", index = False)
    TN_3P0G= pd.concat([T_3P0G, N_3P0G], ignore_index=True)
    TN_3P0G.to_csv("TN_3P0G.csv", index = False)
    TN_3UON= pd.concat([T_3UON, N_3UON], ignore_index=True)
    TN_3UON.to_csv("TN_3UON.csv", index = False)
    TN_3V2W= pd.concat([T_3V2W, N_3V2W], ignore_index=True)
    TN_3V2W.to_csv("TN_3V2W.csv", index = False)
    TN_3V2Y= pd.concat([T_3V2Y, N_3V2Y], ignore_index=True)
    TN_3V2Y.to_csv("TN_3V2Y.csv", index = False)
    TN_3VGA= pd.concat([T_3VGA, N_3VGA], ignore_index=True)
    TN_3VGA.to_csv("TN_3VGA.csv", index = False)
    TN_3VW7= pd.concat([T_3VW7, N_3VW7], ignore_index=True)
    TN_3VW7.to_csv("TN_3VW7.csv", index = False)
    TN_3ZPQ= pd.concat([T_3ZPQ, N_3ZPQ], ignore_index=True)
    TN_3ZPQ.to_csv("TN_3ZPQ.csv", index = False)
    TN_3ZPR= pd.concat([T_3ZPR, N_3ZPR], ignore_index=True)
    TN_3ZPR.to_csv("TN_3ZPR.csv", index = False)
    TN_4AMJ= pd.concat([T_4AMJ, N_4AMJ], ignore_index=True)
    TN_4AMJ.to_csv("TN_4AMJ.csv", index = False)
    TN_4BVN= pd.concat([T_4BVN, N_4BVN], ignore_index=True)
    TN_4BVN.to_csv("TN_4BVN.csv", index = False)
    TN_4DAJ= pd.concat([T_4DAJ, N_4DAJ], ignore_index=True)
    TN_4DAJ.to_csv("TN_4DAJ.csv", index = False)
    TN_4EA3= pd.concat([T_4EA3, N_4EA3], ignore_index=True)
    TN_4EA3.to_csv("TN_4EA3.csv", index = False)
    TN_4EIY= pd.concat([T_4EIY, N_4EIY], ignore_index=True)
    TN_4EIY.to_csv("TN_4EIY.csv", index = False)
    TN_4EJ4= pd.concat([T_4EJ4, N_4EJ4], ignore_index=True)
    TN_4EJ4.to_csv("TN_4EJ4.csv", index = False)
    TN_4GBR= pd.concat([T_4GBR, N_4GBR], ignore_index=True)
    TN_4GBR.to_csv("TN_4GBR.csv", index = False)
    TN_4IAQ= pd.concat([T_4IAQ, N_4IAQ], ignore_index=True)
    TN_4IAQ.to_csv("TN_4IAQ.csv", index = False)
    TN_4IAR= pd.concat([T_4IAR, N_4IAR], ignore_index=True)
    TN_4IAR.to_csv("TN_4IAR.csv", index = False)
    TN_4IB4= pd.concat([T_4IB4, N_4IB4], ignore_index=True)
    TN_4IB4.to_csv("TN_4IB4.csv", index = False)
    TN_4JKV= pd.concat([T_4JKV, N_4JKV], ignore_index=True)
    TN_4JKV.to_csv("TN_4JKV.csv", index = False)
    TN_4K5Y= pd.concat([T_4K5Y, N_4K5Y], ignore_index=True)
    TN_4K5Y.to_csv("TN_4K5Y.csv", index = False)
    TN_4LDE= pd.concat([T_4LDE, N_4LDE], ignore_index=True)
    TN_4LDE.to_csv("TN_4LDE.csv", index = False)
    TN_4LDL= pd.concat([T_4LDL, N_4LDL], ignore_index=True)
    TN_4LDL.to_csv("TN_4LDL.csv", index = False)
    TN_4LDO= pd.concat([T_4LDO, N_4LDO], ignore_index=True)
    TN_4LDO.to_csv("TN_4LDO.csv", index = False)
    TN_4MBS= pd.concat([T_4MBS, N_4MBS], ignore_index=True)
    TN_4MBS.to_csv("TN_4MBS.csv", index = False)
    TN_4MQS= pd.concat([T_4MQS, N_4MQS], ignore_index=True)
    TN_4MQS.to_csv("TN_4MQS.csv", index = False)
    TN_4MQT= pd.concat([T_4MQT, N_4MQT], ignore_index=True)
    TN_4MQT.to_csv("TN_4MQT.csv", index = False)
    TN_4N4W= pd.concat([T_4N4W, N_4N4W], ignore_index=True)
    TN_4N4W.to_csv("TN_4N4W.csv", index = False)
    TN_4N6H= pd.concat([T_4N6H, N_4N6H], ignore_index=True)
    TN_4N6H.to_csv("TN_4N6H.csv", index = False)
    TN_4NTJ= pd.concat([T_4NTJ, N_4NTJ], ignore_index=True)
    TN_4NTJ.to_csv("TN_4NTJ.csv", index = False)
    TN_4O9R= pd.concat([T_4O9R, N_4O9R], ignore_index=True)
    TN_4O9R.to_csv("TN_4O9R.csv", index = False)
    TN_4OO9= pd.concat([T_4OO9, N_4OO9], ignore_index=True)
    TN_4OO9.to_csv("TN_4OO9.csv", index = False)
    TN_4OR2= pd.concat([T_4OR2, N_4OR2], ignore_index=True)
    TN_4OR2.to_csv("TN_4OR2.csv", index = False)
    TN_4PXZ= pd.concat([T_4PXZ, N_4PXZ], ignore_index=True)
    TN_4PXZ.to_csv("TN_4PXZ.csv", index = False)
    TN_4PY0= pd.concat([T_4PY0, N_4PY0], ignore_index=True)
    TN_4PY0.to_csv("TN_4PY0.csv", index = False)
    TN_4QIM= pd.concat([T_4QIM, N_4QIM], ignore_index=True)
    TN_4QIM.to_csv("TN_4QIM.csv", index = False)
    TN_4QIN= pd.concat([T_4QIN, N_4QIN], ignore_index=True)
    TN_4QIN.to_csv("TN_4QIN.csv", index = False)
    TN_4S0V= pd.concat([T_4S0V, N_4S0V], ignore_index=True)
    TN_4S0V.to_csv("TN_4S0V.csv", index = False)
    TN_4U14= pd.concat([T_4U14, N_4U14], ignore_index=True)
    TN_4U14.to_csv("TN_4U14.csv", index = False)
    TN_4U16= pd.concat([T_4U16, N_4U16], ignore_index=True)
    TN_4U16.to_csv("TN_4U16.csv", index = False)
    TN_4UG2= pd.concat([T_4UG2, N_4UG2], ignore_index=True)
    TN_4UG2.to_csv("TN_4UG2.csv", index = False)
    TN_4UHR= pd.concat([T_4UHR, N_4UHR], ignore_index=True)
    TN_4UHR.to_csv("TN_4UHR.csv", index = False)
    TN_4XNW= pd.concat([T_4XNW, N_4XNW], ignore_index=True)
    TN_4XNW.to_csv("TN_4XNW.csv", index = False)
    TN_4YAY= pd.concat([T_4YAY, N_4YAY], ignore_index=True)
    TN_4YAY.to_csv("TN_4YAY.csv", index = False)
    TN_4Z34= pd.concat([T_4Z34, N_4Z34], ignore_index=True)
    TN_4Z34.to_csv("TN_4Z34.csv", index = False)
    TN_4Z36= pd.concat([T_4Z36, N_4Z36], ignore_index=True)
    TN_4Z36.to_csv("TN_4Z36.csv", index = False)
    TN_4Z9G= pd.concat([T_4Z9G, N_4Z9G], ignore_index=True)
    TN_4Z9G.to_csv("TN_4Z9G.csv", index = False)
    TN_4ZUD= pd.concat([T_4ZUD, N_4ZUD], ignore_index=True)
    TN_4ZUD.to_csv("TN_4ZUD.csv", index = False)
    TN_5C1M= pd.concat([T_5C1M, N_5C1M], ignore_index=True)
    TN_5C1M.to_csv("TN_5C1M.csv", index = False)
    TN_5CGC= pd.concat([T_5CGC, N_5CGC], ignore_index=True)
    TN_5CGC.to_csv("TN_5CGC.csv", index = False)
    TN_5CGD= pd.concat([T_5CGD, N_5CGD], ignore_index=True)
    TN_5CGD.to_csv("TN_5CGD.csv", index = False)
    TN_5CXV= pd.concat([T_5CXV, N_5CXV], ignore_index=True)
    TN_5CXV.to_csv("TN_5CXV.csv", index = False)
    TN_5D5B= pd.concat([T_5D5B, N_5D5B], ignore_index=True)
    TN_5D5B.to_csv("TN_5D5B.csv", index = False)
    TN_5D6L= pd.concat([T_5D6L, N_5D6L], ignore_index=True)
    TN_5D6L.to_csv("TN_5D6L.csv", index = False)
    TN_5DHG= pd.concat([T_5DHG, N_5DHG], ignore_index=True)
    TN_5DHG.to_csv("TN_5DHG.csv", index = False)
    TN_5DHH= pd.concat([T_5DHH, N_5DHH], ignore_index=True)
    TN_5DHH.to_csv("TN_5DHH.csv", index = False)
    TN_5DSG= pd.concat([T_5DSG, N_5DSG], ignore_index=True)
    TN_5DSG.to_csv("TN_5DSG.csv", index = False)
    TN_5F8U= pd.concat([T_5F8U, N_5F8U], ignore_index=True)
    TN_5F8U.to_csv("TN_5F8U.csv", index = False)
    TN_5G53= pd.concat([T_5G53, N_5G53], ignore_index=True)
    TN_5G53.to_csv("TN_5G53.csv", index = False)
    TN_5IU4= pd.concat([T_5IU4, N_5IU4], ignore_index=True)
    TN_5IU4.to_csv("TN_5IU4.csv", index = False)
    TN_5IU7= pd.concat([T_5IU7, N_5IU7], ignore_index=True)
    TN_5IU7.to_csv("TN_5IU7.csv", index = False)
    TN_5IU8= pd.concat([T_5IU8, N_5IU8], ignore_index=True)
    TN_5IU8.to_csv("TN_5IU8.csv", index = False)
    TN_5IUA= pd.concat([T_5IUA, N_5IUA], ignore_index=True)
    TN_5IUA.to_csv("TN_5IUA.csv", index = False)
    TN_5IUB= pd.concat([T_5IUB, N_5IUB], ignore_index=True)
    TN_5IUB.to_csv("TN_5IUB.csv", index = False)
    TN_5JQH= pd.concat([T_5JQH, N_5JQH], ignore_index=True)
    TN_5JQH.to_csv("TN_5JQH.csv", index = False)
    TN_5K2B= pd.concat([T_5K2B, N_5K2B], ignore_index=True)
    TN_5K2B.to_csv("TN_5K2B.csv", index = False)
    TN_5K2D= pd.concat([T_5K2D, N_5K2D], ignore_index=True)
    TN_5K2D.to_csv("TN_5K2D.csv", index = False)
    TN_5L7I= pd.concat([T_5L7I, N_5L7I], ignore_index=True)
    TN_5L7I.to_csv("TN_5L7I.csv", index = False)
    TN_5LWE= pd.concat([T_5LWE, N_5LWE], ignore_index=True)
    TN_5LWE.to_csv("TN_5LWE.csv", index = False)
    TN_5MZJ= pd.concat([T_5MZJ, N_5MZJ], ignore_index=True)
    TN_5MZJ.to_csv("TN_5MZJ.csv", index = False)
    TN_5N2R= pd.concat([T_5N2R, N_5N2R], ignore_index=True)
    TN_5N2R.to_csv("TN_5N2R.csv", index = False)
    TN_5N2S= pd.concat([T_5N2S, N_5N2S], ignore_index=True)
    TN_5N2S.to_csv("TN_5N2S.csv", index = False)
    TN_5NDD= pd.concat([T_5NDD, N_5NDD], ignore_index=True)
    TN_5NDD.to_csv("TN_5NDD.csv", index = False)
    TN_5NLX= pd.concat([T_5NLX, N_5NLX], ignore_index=True)
    TN_5NLX.to_csv("TN_5NLX.csv", index = False)
    TN_5NM2= pd.concat([T_5NM2, N_5NM2], ignore_index=True)
    TN_5NM2.to_csv("TN_5NM2.csv", index = False)
    TN_5NM4= pd.concat([T_5NM4, N_5NM4], ignore_index=True)
    TN_5NM4.to_csv("TN_5NM4.csv", index = False)
    TN_5OLG= pd.concat([T_5OLG, N_5OLG], ignore_index=True)
    TN_5OLG.to_csv("TN_5OLG.csv", index = False)
    TN_5OLH= pd.concat([T_5OLH, N_5OLH], ignore_index=True)
    TN_5OLH.to_csv("TN_5OLH.csv", index = False)
    TN_5OLO= pd.concat([T_5OLO, N_5OLO], ignore_index=True)
    TN_5OLO.to_csv("TN_5OLO.csv", index = False)
    TN_5OLV= pd.concat([T_5OLV, N_5OLV], ignore_index=True)
    TN_5OLV.to_csv("TN_5OLV.csv", index = False)
    TN_5OLZ= pd.concat([T_5OLZ, N_5OLZ], ignore_index=True)
    TN_5OLZ.to_csv("TN_5OLZ.csv", index = False)
    TN_5OM1= pd.concat([T_5OM1, N_5OM1], ignore_index=True)
    TN_5OM1.to_csv("TN_5OM1.csv", index = False)
    TN_5OM4= pd.concat([T_5OM4, N_5OM4], ignore_index=True)
    TN_5OM4.to_csv("TN_5OM4.csv", index = False)
    TN_5TGZ= pd.concat([T_5TGZ, N_5TGZ], ignore_index=True)
    TN_5TGZ.to_csv("TN_5TGZ.csv", index = False)
    TN_5TUD= pd.concat([T_5TUD, N_5TUD], ignore_index=True)
    TN_5TUD.to_csv("TN_5TUD.csv", index = False)
    TN_5TVN= pd.concat([T_5TVN, N_5TVN], ignore_index=True)
    TN_5TVN.to_csv("TN_5TVN.csv", index = False)
    TN_5UIG= pd.concat([T_5UIG, N_5UIG], ignore_index=True)
    TN_5UIG.to_csv("TN_5UIG.csv", index = False)
    TN_5UNH= pd.concat([T_5UNH, N_5UNH], ignore_index=True)
    TN_5UNH.to_csv("TN_5UNH.csv", index = False)
    TN_5UVI= pd.concat([T_5UVI, N_5UVI], ignore_index=True)
    TN_5UVI.to_csv("TN_5UVI.csv", index = False)
    TN_5V54= pd.concat([T_5V54, N_5V54], ignore_index=True)
    TN_5V54.to_csv("TN_5V54.csv", index = False)
    TN_5V56= pd.concat([T_5V56, N_5V56], ignore_index=True)
    TN_5V56.to_csv("TN_5V56.csv", index = False)
    TN_5V57= pd.concat([T_5V57, N_5V57], ignore_index=True)
    TN_5V57.to_csv("TN_5V57.csv", index = False)
    TN_5VRA= pd.concat([T_5VRA, N_5VRA], ignore_index=True)
    TN_5VRA.to_csv("TN_5VRA.csv", index = False)
    TN_5WIU= pd.concat([T_5WIU, N_5WIU], ignore_index=True)
    TN_5WIU.to_csv("TN_5WIU.csv", index = False)
    TN_5WIV= pd.concat([T_5WIV, N_5WIV], ignore_index=True)
    TN_5WIV.to_csv("TN_5WIV.csv", index = False)
    TN_5X7D= pd.concat([T_5X7D, N_5X7D], ignore_index=True)
    TN_5X7D.to_csv("TN_5X7D.csv", index = False)
    TN_5XPR= pd.concat([T_5XPR, N_5XPR], ignore_index=True)
    TN_5XPR.to_csv("TN_5XPR.csv", index = False)
    TN_5XR8= pd.concat([T_5XR8, N_5XR8], ignore_index=True)
    TN_5XR8.to_csv("TN_5XR8.csv", index = False)
    TN_5XRA= pd.concat([T_5XRA, N_5XRA], ignore_index=True)
    TN_5XRA.to_csv("TN_5XRA.csv", index = False)
    TN_5ZBQ= pd.concat([T_5ZBQ, N_5ZBQ], ignore_index=True)
    TN_5ZBQ.to_csv("TN_5ZBQ.csv", index = False)
    TN_5ZHP= pd.concat([T_5ZHP, N_5ZHP], ignore_index=True)
    TN_5ZHP.to_csv("TN_5ZHP.csv", index = False)
    TN_5ZK3= pd.concat([T_5ZK3, N_5ZK3], ignore_index=True)
    TN_5ZK3.to_csv("TN_5ZK3.csv", index = False)
    TN_5ZK8= pd.concat([T_5ZK8, N_5ZK8], ignore_index=True)
    TN_5ZK8.to_csv("TN_5ZK8.csv", index = False)
    TN_5ZKB= pd.concat([T_5ZKB, N_5ZKB], ignore_index=True)
    TN_5ZKB.to_csv("TN_5ZKB.csv", index = False)
    TN_5ZKC= pd.concat([T_5ZKC, N_5ZKC], ignore_index=True)
    TN_5ZKC.to_csv("TN_5ZKC.csv", index = False)
    TN_5ZKP= pd.concat([T_5ZKP, N_5ZKP], ignore_index=True)
    TN_5ZKP.to_csv("TN_5ZKP.csv", index = False)
    TN_5ZKQ= pd.concat([T_5ZKQ, N_5ZKQ], ignore_index=True)
    TN_5ZKQ.to_csv("TN_5ZKQ.csv", index = False)
    TN_5ZTY= pd.concat([T_5ZTY, N_5ZTY], ignore_index=True)
    TN_5ZTY.to_csv("TN_5ZTY.csv", index = False)
    TN_6A93= pd.concat([T_6A93, N_6A93], ignore_index=True)
    TN_6A93.to_csv("TN_6A93.csv", index = False)
    TN_6A94= pd.concat([T_6A94, N_6A94], ignore_index=True)
    TN_6A94.to_csv("TN_6A94.csv", index = False)
    TN_6AKX= pd.concat([T_6AKX, N_6AKX], ignore_index=True)
    TN_6AKX.to_csv("TN_6AKX.csv", index = False)
    TN_6B73= pd.concat([T_6B73, N_6B73], ignore_index=True)
    TN_6B73.to_csv("TN_6B73.csv", index = False)
    TN_6BQG= pd.concat([T_6BQG, N_6BQG], ignore_index=True)
    TN_6BQG.to_csv("TN_6BQG.csv", index = False)
    TN_6BQH= pd.concat([T_6BQH, N_6BQH], ignore_index=True)
    TN_6BQH.to_csv("TN_6BQH.csv", index = False)
    TN_6CM4= pd.concat([T_6CM4, N_6CM4], ignore_index=True)
    TN_6CM4.to_csv("TN_6CM4.csv", index = False)
    TN_6D26= pd.concat([T_6D26, N_6D26], ignore_index=True)
    TN_6D26.to_csv("TN_6D26.csv", index = False)
    TN_6DRX= pd.concat([T_6DRX, N_6DRX], ignore_index=True)
    TN_6DRX.to_csv("TN_6DRX.csv", index = False)
    TN_6DRY= pd.concat([T_6DRY, N_6DRY], ignore_index=True)
    TN_6DRY.to_csv("TN_6DRY.csv", index = False)
    TN_6DRZ= pd.concat([T_6DRZ, N_6DRZ], ignore_index=True)
    TN_6DRZ.to_csv("TN_6DRZ.csv", index = False)
    TN_6DS0= pd.concat([T_6DS0, N_6DS0], ignore_index=True)
    TN_6DS0.to_csv("TN_6DS0.csv", index = False)
    TN_6E59= pd.concat([T_6E59, N_6E59], ignore_index=True)
    TN_6E59.to_csv("TN_6E59.csv", index = False)
    TN_6E67= pd.concat([T_6E67, N_6E67], ignore_index=True)
    TN_6E67.to_csv("TN_6E67.csv", index = False)
    TN_6FFH= pd.concat([T_6FFH, N_6FFH], ignore_index=True)
    TN_6FFH.to_csv("TN_6FFH.csv", index = False)
    TN_6FFI= pd.concat([T_6FFI, N_6FFI], ignore_index=True)
    TN_6FFI.to_csv("TN_6FFI.csv", index = False)
    TN_6FK6= pd.concat([T_6FK6, N_6FK6], ignore_index=True)
    TN_6FK6.to_csv("TN_6FK6.csv", index = False)
    TN_6FK7= pd.concat([T_6FK7, N_6FK7], ignore_index=True)
    TN_6FK7.to_csv("TN_6FK7.csv", index = False)
    TN_6FK8= pd.concat([T_6FK8, N_6FK8], ignore_index=True)
    TN_6FK8.to_csv("TN_6FK8.csv", index = False)
    TN_6FK9= pd.concat([T_6FK9, N_6FK9], ignore_index=True)
    TN_6FK9.to_csv("TN_6FK9.csv", index = False)
    TN_6FKA= pd.concat([T_6FKA, N_6FKA], ignore_index=True)
    TN_6FKA.to_csv("TN_6FKA.csv", index = False)
    TN_6FKB= pd.concat([T_6FKB, N_6FKB], ignore_index=True)
    TN_6FKB.to_csv("TN_6FKB.csv", index = False)
    TN_6FKD= pd.concat([T_6FKD, N_6FKD], ignore_index=True)
    TN_6FKD.to_csv("TN_6FKD.csv", index = False)
    TN_6GDG= pd.concat([T_6GDG, N_6GDG], ignore_index=True)
    TN_6GDG.to_csv("TN_6GDG.csv", index = False)
    TN_6GPS= pd.concat([T_6GPS, N_6GPS], ignore_index=True)
    TN_6GPS.to_csv("TN_6GPS.csv", index = False)
    TN_6GPX= pd.concat([T_6GPX, N_6GPX], ignore_index=True)
    TN_6GPX.to_csv("TN_6GPX.csv", index = False)
    TN_6GT3= pd.concat([T_6GT3, N_6GT3], ignore_index=True)
    TN_6GT3.to_csv("TN_6GT3.csv", index = False)
    TN_6H7J= pd.concat([T_6H7J, N_6H7J], ignore_index=True)
    TN_6H7J.to_csv("TN_6H7J.csv", index = False)
    TN_6H7L= pd.concat([T_6H7L, N_6H7L], ignore_index=True)
    TN_6H7L.to_csv("TN_6H7L.csv", index = False)
    TN_6H7M= pd.concat([T_6H7M, N_6H7M], ignore_index=True)
    TN_6H7M.to_csv("TN_6H7M.csv", index = False)
    TN_6H7N= pd.concat([T_6H7N, N_6H7N], ignore_index=True)
    TN_6H7N.to_csv("TN_6H7N.csv", index = False)
    TN_6H7O= pd.concat([T_6H7O, N_6H7O], ignore_index=True)
    TN_6H7O.to_csv("TN_6H7O.csv", index = False)
    TN_6HLL= pd.concat([T_6HLL, N_6HLL], ignore_index=True)
    TN_6HLL.to_csv("TN_6HLL.csv", index = False)
    TN_6HLO= pd.concat([T_6HLO, N_6HLO], ignore_index=True)
    TN_6HLO.to_csv("TN_6HLO.csv", index = False)
    TN_6HLP= pd.concat([T_6HLP, N_6HLP], ignore_index=True)
    TN_6HLP.to_csv("TN_6HLP.csv", index = False)
    TN_6IBL= pd.concat([T_6IBL, N_6IBL], ignore_index=True)
    TN_6IBL.to_csv("TN_6IBL.csv", index = False)
    TN_6IIU= pd.concat([T_6IIU, N_6IIU], ignore_index=True)
    TN_6IIU.to_csv("TN_6IIU.csv", index = False)
    TN_6IIV= pd.concat([T_6IIV, N_6IIV], ignore_index=True)
    TN_6IIV.to_csv("TN_6IIV.csv", index = False)
    TN_6IQL= pd.concat([T_6IQL, N_6IQL], ignore_index=True)
    TN_6IQL.to_csv("TN_6IQL.csv", index = False)
    TN_6J20= pd.concat([T_6J20, N_6J20], ignore_index=True)
    TN_6J20.to_csv("TN_6J20.csv", index = False)
    TN_6JZH= pd.concat([T_6JZH, N_6JZH], ignore_index=True)
    TN_6JZH.to_csv("TN_6JZH.csv", index = False)
    TN_6K1Q= pd.concat([T_6K1Q, N_6K1Q], ignore_index=True)
    TN_6K1Q.to_csv("TN_6K1Q.csv", index = False)
    TN_6M9T= pd.concat([T_6M9T, N_6M9T], ignore_index=True)
    TN_6M9T.to_csv("TN_6M9T.csv", index = False)
    TN_6ME2= pd.concat([T_6ME2, N_6ME2], ignore_index=True)
    TN_6ME2.to_csv("TN_6ME2.csv", index = False)
    TN_6ME3= pd.concat([T_6ME3, N_6ME3], ignore_index=True)
    TN_6ME3.to_csv("TN_6ME3.csv", index = False)
    TN_6ME4= pd.concat([T_6ME4, N_6ME4], ignore_index=True)
    TN_6ME4.to_csv("TN_6ME4.csv", index = False)
    TN_6ME5= pd.concat([T_6ME5, N_6ME5], ignore_index=True)
    TN_6ME5.to_csv("TN_6ME5.csv", index = False)
    TN_6ME6= pd.concat([T_6ME6, N_6ME6], ignore_index=True)
    TN_6ME6.to_csv("TN_6ME6.csv", index = False)
    TN_6ME7= pd.concat([T_6ME7, N_6ME7], ignore_index=True)
    TN_6ME7.to_csv("TN_6ME7.csv", index = False)
    TN_6ME8= pd.concat([T_6ME8, N_6ME8], ignore_index=True)
    TN_6ME8.to_csv("TN_6ME8.csv", index = False)
    TN_6ME9= pd.concat([T_6ME9, N_6ME9], ignore_index=True)
    TN_6ME9.to_csv("TN_6ME9.csv", index = False)
    TN_6MH8= pd.concat([T_6MH8, N_6MH8], ignore_index=True)
    TN_6MH8.to_csv("TN_6MH8.csv", index = False)
    TN_6MXT= pd.concat([T_6MXT, N_6MXT], ignore_index=True)
    TN_6MXT.to_csv("TN_6MXT.csv", index = False)
    TN_6N48= pd.concat([T_6N48, N_6N48], ignore_index=True)
    TN_6N48.to_csv("TN_6N48.csv", index = False)
    TN_6OL9= pd.concat([T_6OL9, N_6OL9], ignore_index=True)
    TN_6OL9.to_csv("TN_6OL9.csv", index = False)
    TN_6PRZ= pd.concat([T_6PRZ, N_6PRZ], ignore_index=True)
    TN_6PRZ.to_csv("TN_6PRZ.csv", index = False)
    TN_6PS0= pd.concat([T_6PS0, N_6PS0], ignore_index=True)
    TN_6PS0.to_csv("TN_6PS0.csv", index = False)
    TN_6PS1= pd.concat([T_6PS1, N_6PS1], ignore_index=True)
    TN_6PS1.to_csv("TN_6PS1.csv", index = False)
    TN_6PS2= pd.concat([T_6PS2, N_6PS2], ignore_index=True)
    TN_6PS2.to_csv("TN_6PS2.csv", index = False)
    TN_6PS3= pd.concat([T_6PS3, N_6PS3], ignore_index=True)
    TN_6PS3.to_csv("TN_6PS3.csv", index = False)
    TN_6PS4= pd.concat([T_6PS4, N_6PS4], ignore_index=True)
    TN_6PS4.to_csv("TN_6PS4.csv", index = False)
    TN_6PS5= pd.concat([T_6PS5, N_6PS5], ignore_index=True)
    TN_6PS5.to_csv("TN_6PS5.csv", index = False)
    TN_6PS6= pd.concat([T_6PS6, N_6PS6], ignore_index=True)
    TN_6PS6.to_csv("TN_6PS6.csv", index = False)
    TN_6PS7= pd.concat([T_6PS7, N_6PS7], ignore_index=True)
    TN_6PS7.to_csv("TN_6PS7.csv", index = False)
    TN_6PS8= pd.concat([T_6PS8, N_6PS8], ignore_index=True)
    TN_6PS8.to_csv("TN_6PS8.csv", index = False)
    TN_6QZH= pd.concat([T_6QZH, N_6QZH], ignore_index=True)
    TN_6QZH.to_csv("TN_6QZH.csv", index = False)
    TN_6RZ4= pd.concat([T_6RZ4, N_6RZ4], ignore_index=True)
    TN_6RZ4.to_csv("TN_6RZ4.csv", index = False)
    TN_6TP3= pd.concat([T_6TP3, N_6TP3], ignore_index=True)
    TN_6TP3.to_csv("TN_6TP3.csv", index = False)
    TN_6TP4= pd.concat([T_6TP4, N_6TP4], ignore_index=True)
    TN_6TP4.to_csv("TN_6TP4.csv", index = False)
    TN_6TP6= pd.concat([T_6TP6, N_6TP6], ignore_index=True)
    TN_6TP6.to_csv("TN_6TP6.csv", index = False)
    TN_6TPG= pd.concat([T_6TPG, N_6TPG], ignore_index=True)
    TN_6TPG.to_csv("TN_6TPG.csv", index = False)
    TN_6TPN= pd.concat([T_6TPN, N_6TPN], ignore_index=True)
    TN_6TPN.to_csv("TN_6TPN.csv", index = False)
    


```python
TN_2I35= pd.concat([T_2I35, N_2I35], ignore_index=True)
TN_2I35.to_csv("TN_2I35.csv", index = False)
TN_2RH1= pd.concat([T_2RH1, N_2RH1], ignore_index=True)
TN_2RH1.to_csv("TN_2RH1.csv", index = False)
TN_2VT4= pd.concat([T_2VT4, N_2VT4], ignore_index=True)
TN_2VT4.to_csv("TN_2VT4.csv", index = False)
TN_2X72= pd.concat([T_2X72, N_2X72], ignore_index=True)
TN_2X72.to_csv("TN_2X72.csv", index = False)
TN_2Y00= pd.concat([T_2Y00, N_2Y00], ignore_index=True)
TN_2Y00.to_csv("TN_2Y00.csv", index = False)
TN_2Y01= pd.concat([T_2Y01, N_2Y01], ignore_index=True)
TN_2Y01.to_csv("TN_2Y01.csv", index = False)
TN_2Y02= pd.concat([T_2Y02, N_2Y02], ignore_index=True)
TN_2Y02.to_csv("TN_2Y02.csv", index = False)
TN_2Y03= pd.concat([T_2Y03, N_2Y03], ignore_index=True)
TN_2Y03.to_csv("TN_2Y03.csv", index = False)
TN_2Y04= pd.concat([T_2Y04, N_2Y04], ignore_index=True)
TN_2Y04.to_csv("TN_2Y04.csv", index = False)
TN_2YCW= pd.concat([T_2YCW, N_2YCW], ignore_index=True)
TN_2YCW.to_csv("TN_2YCW.csv", index = False)
TN_2YCX= pd.concat([T_2YCX, N_2YCX], ignore_index=True)
TN_2YCX.to_csv("TN_2YCX.csv", index = False)
TN_2YCY= pd.concat([T_2YCY, N_2YCY], ignore_index=True)
TN_2YCY.to_csv("TN_2YCY.csv", index = False)
TN_2YCZ= pd.concat([T_2YCZ, N_2YCZ], ignore_index=True)
TN_2YCZ.to_csv("TN_2YCZ.csv", index = False)
TN_2YDV= pd.concat([T_2YDV, N_2YDV], ignore_index=True)
TN_2YDV.to_csv("TN_2YDV.csv", index = False)
TN_3D4S= pd.concat([T_3D4S, N_3D4S], ignore_index=True)
TN_3D4S.to_csv("TN_3D4S.csv", index = False)
TN_3NY8= pd.concat([T_3NY8, N_3NY8], ignore_index=True)
TN_3NY8.to_csv("TN_3NY8.csv", index = False)
TN_3NY9= pd.concat([T_3NY9, N_3NY9], ignore_index=True)
TN_3NY9.to_csv("TN_3NY9.csv", index = False)
TN_3NYA= pd.concat([T_3NYA, N_3NYA], ignore_index=True)
TN_3NYA.to_csv("TN_3NYA.csv", index = False)
TN_3OE8= pd.concat([T_3OE8, N_3OE8], ignore_index=True)
TN_3OE8.to_csv("TN_3OE8.csv", index = False)
TN_3P0G= pd.concat([T_3P0G, N_3P0G], ignore_index=True)
TN_3P0G.to_csv("TN_3P0G.csv", index = False)
TN_3UON= pd.concat([T_3UON, N_3UON], ignore_index=True)
TN_3UON.to_csv("TN_3UON.csv", index = False)
TN_3V2W= pd.concat([T_3V2W, N_3V2W], ignore_index=True)
TN_3V2W.to_csv("TN_3V2W.csv", index = False)
TN_3V2Y= pd.concat([T_3V2Y, N_3V2Y], ignore_index=True)
TN_3V2Y.to_csv("TN_3V2Y.csv", index = False)
TN_3VGA= pd.concat([T_3VGA, N_3VGA], ignore_index=True)
TN_3VGA.to_csv("TN_3VGA.csv", index = False)
TN_3VW7= pd.concat([T_3VW7, N_3VW7], ignore_index=True)
TN_3VW7.to_csv("TN_3VW7.csv", index = False)
TN_3ZPQ= pd.concat([T_3ZPQ, N_3ZPQ], ignore_index=True)
TN_3ZPQ.to_csv("TN_3ZPQ.csv", index = False)
TN_3ZPR= pd.concat([T_3ZPR, N_3ZPR], ignore_index=True)
TN_3ZPR.to_csv("TN_3ZPR.csv", index = False)
TN_4AMJ= pd.concat([T_4AMJ, N_4AMJ], ignore_index=True)
TN_4AMJ.to_csv("TN_4AMJ.csv", index = False)
TN_4BVN= pd.concat([T_4BVN, N_4BVN], ignore_index=True)
TN_4BVN.to_csv("TN_4BVN.csv", index = False)
TN_4DAJ= pd.concat([T_4DAJ, N_4DAJ], ignore_index=True)
TN_4DAJ.to_csv("TN_4DAJ.csv", index = False)
TN_4EA3= pd.concat([T_4EA3, N_4EA3], ignore_index=True)
TN_4EA3.to_csv("TN_4EA3.csv", index = False)
TN_4EIY= pd.concat([T_4EIY, N_4EIY], ignore_index=True)
TN_4EIY.to_csv("TN_4EIY.csv", index = False)
TN_4EJ4= pd.concat([T_4EJ4, N_4EJ4], ignore_index=True)
TN_4EJ4.to_csv("TN_4EJ4.csv", index = False)
TN_4GBR= pd.concat([T_4GBR, N_4GBR], ignore_index=True)
TN_4GBR.to_csv("TN_4GBR.csv", index = False)
TN_4IAQ= pd.concat([T_4IAQ, N_4IAQ], ignore_index=True)
TN_4IAQ.to_csv("TN_4IAQ.csv", index = False)
TN_4IAR= pd.concat([T_4IAR, N_4IAR], ignore_index=True)
TN_4IAR.to_csv("TN_4IAR.csv", index = False)
TN_4IB4= pd.concat([T_4IB4, N_4IB4], ignore_index=True)
TN_4IB4.to_csv("TN_4IB4.csv", index = False)
TN_4JKV= pd.concat([T_4JKV, N_4JKV], ignore_index=True)
TN_4JKV.to_csv("TN_4JKV.csv", index = False)
TN_4K5Y= pd.concat([T_4K5Y, N_4K5Y], ignore_index=True)
TN_4K5Y.to_csv("TN_4K5Y.csv", index = False)
TN_4LDE= pd.concat([T_4LDE, N_4LDE], ignore_index=True)
TN_4LDE.to_csv("TN_4LDE.csv", index = False)
TN_4LDL= pd.concat([T_4LDL, N_4LDL], ignore_index=True)
TN_4LDL.to_csv("TN_4LDL.csv", index = False)
TN_4LDO= pd.concat([T_4LDO, N_4LDO], ignore_index=True)
TN_4LDO.to_csv("TN_4LDO.csv", index = False)
TN_4MBS= pd.concat([T_4MBS, N_4MBS], ignore_index=True)
TN_4MBS.to_csv("TN_4MBS.csv", index = False)
TN_4MQS= pd.concat([T_4MQS, N_4MQS], ignore_index=True)
TN_4MQS.to_csv("TN_4MQS.csv", index = False)
TN_4MQT= pd.concat([T_4MQT, N_4MQT], ignore_index=True)
TN_4MQT.to_csv("TN_4MQT.csv", index = False)
TN_4N4W= pd.concat([T_4N4W, N_4N4W], ignore_index=True)
TN_4N4W.to_csv("TN_4N4W.csv", index = False)
TN_4N6H= pd.concat([T_4N6H, N_4N6H], ignore_index=True)
TN_4N6H.to_csv("TN_4N6H.csv", index = False)
TN_4NTJ= pd.concat([T_4NTJ, N_4NTJ], ignore_index=True)
TN_4NTJ.to_csv("TN_4NTJ.csv", index = False)
TN_4O9R= pd.concat([T_4O9R, N_4O9R], ignore_index=True)
TN_4O9R.to_csv("TN_4O9R.csv", index = False)
TN_4OO9= pd.concat([T_4OO9, N_4OO9], ignore_index=True)
TN_4OO9.to_csv("TN_4OO9.csv", index = False)
TN_4OR2= pd.concat([T_4OR2, N_4OR2], ignore_index=True)
TN_4OR2.to_csv("TN_4OR2.csv", index = False)
TN_4PXZ= pd.concat([T_4PXZ, N_4PXZ], ignore_index=True)
TN_4PXZ.to_csv("TN_4PXZ.csv", index = False)
TN_4PY0= pd.concat([T_4PY0, N_4PY0], ignore_index=True)
TN_4PY0.to_csv("TN_4PY0.csv", index = False)
TN_4QIM= pd.concat([T_4QIM, N_4QIM], ignore_index=True)
TN_4QIM.to_csv("TN_4QIM.csv", index = False)
TN_4QIN= pd.concat([T_4QIN, N_4QIN], ignore_index=True)
TN_4QIN.to_csv("TN_4QIN.csv", index = False)
TN_4S0V= pd.concat([T_4S0V, N_4S0V], ignore_index=True)
TN_4S0V.to_csv("TN_4S0V.csv", index = False)
TN_4U14= pd.concat([T_4U14, N_4U14], ignore_index=True)
TN_4U14.to_csv("TN_4U14.csv", index = False)
TN_4U16= pd.concat([T_4U16, N_4U16], ignore_index=True)
TN_4U16.to_csv("TN_4U16.csv", index = False)
TN_4UG2= pd.concat([T_4UG2, N_4UG2], ignore_index=True)
TN_4UG2.to_csv("TN_4UG2.csv", index = False)
TN_4UHR= pd.concat([T_4UHR, N_4UHR], ignore_index=True)
TN_4UHR.to_csv("TN_4UHR.csv", index = False)
TN_4XNW= pd.concat([T_4XNW, N_4XNW], ignore_index=True)
TN_4XNW.to_csv("TN_4XNW.csv", index = False)
TN_4YAY= pd.concat([T_4YAY, N_4YAY], ignore_index=True)
TN_4YAY.to_csv("TN_4YAY.csv", index = False)
TN_4Z34= pd.concat([T_4Z34, N_4Z34], ignore_index=True)
TN_4Z34.to_csv("TN_4Z34.csv", index = False)
TN_4Z36= pd.concat([T_4Z36, N_4Z36], ignore_index=True)
TN_4Z36.to_csv("TN_4Z36.csv", index = False)
TN_4Z9G= pd.concat([T_4Z9G, N_4Z9G], ignore_index=True)
TN_4Z9G.to_csv("TN_4Z9G.csv", index = False)
TN_4ZUD= pd.concat([T_4ZUD, N_4ZUD], ignore_index=True)
TN_4ZUD.to_csv("TN_4ZUD.csv", index = False)
TN_5C1M= pd.concat([T_5C1M, N_5C1M], ignore_index=True)
TN_5C1M.to_csv("TN_5C1M.csv", index = False)
TN_5CGC= pd.concat([T_5CGC, N_5CGC], ignore_index=True)
TN_5CGC.to_csv("TN_5CGC.csv", index = False)
TN_5CGD= pd.concat([T_5CGD, N_5CGD], ignore_index=True)
TN_5CGD.to_csv("TN_5CGD.csv", index = False)
TN_5CXV= pd.concat([T_5CXV, N_5CXV], ignore_index=True)
TN_5CXV.to_csv("TN_5CXV.csv", index = False)
TN_5D5B= pd.concat([T_5D5B, N_5D5B], ignore_index=True)
TN_5D5B.to_csv("TN_5D5B.csv", index = False)
TN_5D6L= pd.concat([T_5D6L, N_5D6L], ignore_index=True)
TN_5D6L.to_csv("TN_5D6L.csv", index = False)
TN_5DHG= pd.concat([T_5DHG, N_5DHG], ignore_index=True)
TN_5DHG.to_csv("TN_5DHG.csv", index = False)
TN_5DHH= pd.concat([T_5DHH, N_5DHH], ignore_index=True)
TN_5DHH.to_csv("TN_5DHH.csv", index = False)
TN_5DSG= pd.concat([T_5DSG, N_5DSG], ignore_index=True)
TN_5DSG.to_csv("TN_5DSG.csv", index = False)
TN_5F8U= pd.concat([T_5F8U, N_5F8U], ignore_index=True)
TN_5F8U.to_csv("TN_5F8U.csv", index = False)
TN_5G53= pd.concat([T_5G53, N_5G53], ignore_index=True)
TN_5G53.to_csv("TN_5G53.csv", index = False)
TN_5IU4= pd.concat([T_5IU4, N_5IU4], ignore_index=True)
TN_5IU4.to_csv("TN_5IU4.csv", index = False)
TN_5IU7= pd.concat([T_5IU7, N_5IU7], ignore_index=True)
TN_5IU7.to_csv("TN_5IU7.csv", index = False)
TN_5IU8= pd.concat([T_5IU8, N_5IU8], ignore_index=True)
TN_5IU8.to_csv("TN_5IU8.csv", index = False)
TN_5IUA= pd.concat([T_5IUA, N_5IUA], ignore_index=True)
TN_5IUA.to_csv("TN_5IUA.csv", index = False)
TN_5IUB= pd.concat([T_5IUB, N_5IUB], ignore_index=True)
TN_5IUB.to_csv("TN_5IUB.csv", index = False)
TN_5JQH= pd.concat([T_5JQH, N_5JQH], ignore_index=True)
TN_5JQH.to_csv("TN_5JQH.csv", index = False)
TN_5K2B= pd.concat([T_5K2B, N_5K2B], ignore_index=True)
TN_5K2B.to_csv("TN_5K2B.csv", index = False)
TN_5K2D= pd.concat([T_5K2D, N_5K2D], ignore_index=True)
TN_5K2D.to_csv("TN_5K2D.csv", index = False)
TN_5L7I= pd.concat([T_5L7I, N_5L7I], ignore_index=True)
TN_5L7I.to_csv("TN_5L7I.csv", index = False)
TN_5LWE= pd.concat([T_5LWE, N_5LWE], ignore_index=True)
TN_5LWE.to_csv("TN_5LWE.csv", index = False)
TN_5MZJ= pd.concat([T_5MZJ, N_5MZJ], ignore_index=True)
TN_5MZJ.to_csv("TN_5MZJ.csv", index = False)
TN_5N2R= pd.concat([T_5N2R, N_5N2R], ignore_index=True)
TN_5N2R.to_csv("TN_5N2R.csv", index = False)
TN_5N2S= pd.concat([T_5N2S, N_5N2S], ignore_index=True)
TN_5N2S.to_csv("TN_5N2S.csv", index = False)
TN_5NDD= pd.concat([T_5NDD, N_5NDD], ignore_index=True)
TN_5NDD.to_csv("TN_5NDD.csv", index = False)
TN_5NLX= pd.concat([T_5NLX, N_5NLX], ignore_index=True)
TN_5NLX.to_csv("TN_5NLX.csv", index = False)
TN_5NM2= pd.concat([T_5NM2, N_5NM2], ignore_index=True)
TN_5NM2.to_csv("TN_5NM2.csv", index = False)
TN_5NM4= pd.concat([T_5NM4, N_5NM4], ignore_index=True)
TN_5NM4.to_csv("TN_5NM4.csv", index = False)
TN_5OLG= pd.concat([T_5OLG, N_5OLG], ignore_index=True)
TN_5OLG.to_csv("TN_5OLG.csv", index = False)
TN_5OLH= pd.concat([T_5OLH, N_5OLH], ignore_index=True)
TN_5OLH.to_csv("TN_5OLH.csv", index = False)
TN_5OLO= pd.concat([T_5OLO, N_5OLO], ignore_index=True)
TN_5OLO.to_csv("TN_5OLO.csv", index = False)
TN_5OLV= pd.concat([T_5OLV, N_5OLV], ignore_index=True)
TN_5OLV.to_csv("TN_5OLV.csv", index = False)
TN_5OLZ= pd.concat([T_5OLZ, N_5OLZ], ignore_index=True)
TN_5OLZ.to_csv("TN_5OLZ.csv", index = False)
TN_5OM1= pd.concat([T_5OM1, N_5OM1], ignore_index=True)
TN_5OM1.to_csv("TN_5OM1.csv", index = False)
TN_5OM4= pd.concat([T_5OM4, N_5OM4], ignore_index=True)
TN_5OM4.to_csv("TN_5OM4.csv", index = False)
TN_5TGZ= pd.concat([T_5TGZ, N_5TGZ], ignore_index=True)
TN_5TGZ.to_csv("TN_5TGZ.csv", index = False)
TN_5TUD= pd.concat([T_5TUD, N_5TUD], ignore_index=True)
TN_5TUD.to_csv("TN_5TUD.csv", index = False)
TN_5TVN= pd.concat([T_5TVN, N_5TVN], ignore_index=True)
TN_5TVN.to_csv("TN_5TVN.csv", index = False)
TN_5UIG= pd.concat([T_5UIG, N_5UIG], ignore_index=True)
TN_5UIG.to_csv("TN_5UIG.csv", index = False)
TN_5UNH= pd.concat([T_5UNH, N_5UNH], ignore_index=True)
TN_5UNH.to_csv("TN_5UNH.csv", index = False)
TN_5UVI= pd.concat([T_5UVI, N_5UVI], ignore_index=True)
TN_5UVI.to_csv("TN_5UVI.csv", index = False)
TN_5V54= pd.concat([T_5V54, N_5V54], ignore_index=True)
TN_5V54.to_csv("TN_5V54.csv", index = False)
TN_5V56= pd.concat([T_5V56, N_5V56], ignore_index=True)
TN_5V56.to_csv("TN_5V56.csv", index = False)
TN_5V57= pd.concat([T_5V57, N_5V57], ignore_index=True)
TN_5V57.to_csv("TN_5V57.csv", index = False)
TN_5VRA= pd.concat([T_5VRA, N_5VRA], ignore_index=True)
TN_5VRA.to_csv("TN_5VRA.csv", index = False)
TN_5WIU= pd.concat([T_5WIU, N_5WIU], ignore_index=True)
TN_5WIU.to_csv("TN_5WIU.csv", index = False)
TN_5WIV= pd.concat([T_5WIV, N_5WIV], ignore_index=True)
TN_5WIV.to_csv("TN_5WIV.csv", index = False)
TN_5X7D= pd.concat([T_5X7D, N_5X7D], ignore_index=True)
TN_5X7D.to_csv("TN_5X7D.csv", index = False)
TN_5XPR= pd.concat([T_5XPR, N_5XPR], ignore_index=True)
TN_5XPR.to_csv("TN_5XPR.csv", index = False)
TN_5XR8= pd.concat([T_5XR8, N_5XR8], ignore_index=True)
TN_5XR8.to_csv("TN_5XR8.csv", index = False)
TN_5XRA= pd.concat([T_5XRA, N_5XRA], ignore_index=True)
TN_5XRA.to_csv("TN_5XRA.csv", index = False)
TN_5ZBQ= pd.concat([T_5ZBQ, N_5ZBQ], ignore_index=True)
TN_5ZBQ.to_csv("TN_5ZBQ.csv", index = False)
TN_5ZHP= pd.concat([T_5ZHP, N_5ZHP], ignore_index=True)
TN_5ZHP.to_csv("TN_5ZHP.csv", index = False)
TN_5ZK3= pd.concat([T_5ZK3, N_5ZK3], ignore_index=True)
TN_5ZK3.to_csv("TN_5ZK3.csv", index = False)
TN_5ZK8= pd.concat([T_5ZK8, N_5ZK8], ignore_index=True)
TN_5ZK8.to_csv("TN_5ZK8.csv", index = False)
TN_5ZKB= pd.concat([T_5ZKB, N_5ZKB], ignore_index=True)
TN_5ZKB.to_csv("TN_5ZKB.csv", index = False)
TN_5ZKC= pd.concat([T_5ZKC, N_5ZKC], ignore_index=True)
TN_5ZKC.to_csv("TN_5ZKC.csv", index = False)
TN_5ZKP= pd.concat([T_5ZKP, N_5ZKP], ignore_index=True)
TN_5ZKP.to_csv("TN_5ZKP.csv", index = False)
TN_5ZKQ= pd.concat([T_5ZKQ, N_5ZKQ], ignore_index=True)
TN_5ZKQ.to_csv("TN_5ZKQ.csv", index = False)
TN_5ZTY= pd.concat([T_5ZTY, N_5ZTY], ignore_index=True)
TN_5ZTY.to_csv("TN_5ZTY.csv", index = False)
TN_6A93= pd.concat([T_6A93, N_6A93], ignore_index=True)
TN_6A93.to_csv("TN_6A93.csv", index = False)
TN_6A94= pd.concat([T_6A94, N_6A94], ignore_index=True)
TN_6A94.to_csv("TN_6A94.csv", index = False)
TN_6AKX= pd.concat([T_6AKX, N_6AKX], ignore_index=True)
TN_6AKX.to_csv("TN_6AKX.csv", index = False)
TN_6B73= pd.concat([T_6B73, N_6B73], ignore_index=True)
TN_6B73.to_csv("TN_6B73.csv", index = False)
TN_6BQG= pd.concat([T_6BQG, N_6BQG], ignore_index=True)
TN_6BQG.to_csv("TN_6BQG.csv", index = False)
TN_6BQH= pd.concat([T_6BQH, N_6BQH], ignore_index=True)
TN_6BQH.to_csv("TN_6BQH.csv", index = False)
TN_6CM4= pd.concat([T_6CM4, N_6CM4], ignore_index=True)
TN_6CM4.to_csv("TN_6CM4.csv", index = False)
TN_6D26= pd.concat([T_6D26, N_6D26], ignore_index=True)
TN_6D26.to_csv("TN_6D26.csv", index = False)
TN_6DRX= pd.concat([T_6DRX, N_6DRX], ignore_index=True)
TN_6DRX.to_csv("TN_6DRX.csv", index = False)
TN_6DRY= pd.concat([T_6DRY, N_6DRY], ignore_index=True)
TN_6DRY.to_csv("TN_6DRY.csv", index = False)
TN_6DRZ= pd.concat([T_6DRZ, N_6DRZ], ignore_index=True)
TN_6DRZ.to_csv("TN_6DRZ.csv", index = False)
TN_6DS0= pd.concat([T_6DS0, N_6DS0], ignore_index=True)
TN_6DS0.to_csv("TN_6DS0.csv", index = False)
TN_6E59= pd.concat([T_6E59, N_6E59], ignore_index=True)
TN_6E59.to_csv("TN_6E59.csv", index = False)
TN_6E67= pd.concat([T_6E67, N_6E67], ignore_index=True)
TN_6E67.to_csv("TN_6E67.csv", index = False)
TN_6FFH= pd.concat([T_6FFH, N_6FFH], ignore_index=True)
TN_6FFH.to_csv("TN_6FFH.csv", index = False)
TN_6FFI= pd.concat([T_6FFI, N_6FFI], ignore_index=True)
TN_6FFI.to_csv("TN_6FFI.csv", index = False)
TN_6FK6= pd.concat([T_6FK6, N_6FK6], ignore_index=True)
TN_6FK6.to_csv("TN_6FK6.csv", index = False)
TN_6FK7= pd.concat([T_6FK7, N_6FK7], ignore_index=True)
TN_6FK7.to_csv("TN_6FK7.csv", index = False)
TN_6FK8= pd.concat([T_6FK8, N_6FK8], ignore_index=True)
TN_6FK8.to_csv("TN_6FK8.csv", index = False)
TN_6FK9= pd.concat([T_6FK9, N_6FK9], ignore_index=True)
TN_6FK9.to_csv("TN_6FK9.csv", index = False)
TN_6FKA= pd.concat([T_6FKA, N_6FKA], ignore_index=True)
TN_6FKA.to_csv("TN_6FKA.csv", index = False)
TN_6FKB= pd.concat([T_6FKB, N_6FKB], ignore_index=True)
TN_6FKB.to_csv("TN_6FKB.csv", index = False)
TN_6FKD= pd.concat([T_6FKD, N_6FKD], ignore_index=True)
TN_6FKD.to_csv("TN_6FKD.csv", index = False)
TN_6GDG= pd.concat([T_6GDG, N_6GDG], ignore_index=True)
TN_6GDG.to_csv("TN_6GDG.csv", index = False)
TN_6GPS= pd.concat([T_6GPS, N_6GPS], ignore_index=True)
TN_6GPS.to_csv("TN_6GPS.csv", index = False)
TN_6GPX= pd.concat([T_6GPX, N_6GPX], ignore_index=True)
TN_6GPX.to_csv("TN_6GPX.csv", index = False)
TN_6GT3= pd.concat([T_6GT3, N_6GT3], ignore_index=True)
TN_6GT3.to_csv("TN_6GT3.csv", index = False)
TN_6H7J= pd.concat([T_6H7J, N_6H7J], ignore_index=True)
TN_6H7J.to_csv("TN_6H7J.csv", index = False)
TN_6H7L= pd.concat([T_6H7L, N_6H7L], ignore_index=True)
TN_6H7L.to_csv("TN_6H7L.csv", index = False)
TN_6H7M= pd.concat([T_6H7M, N_6H7M], ignore_index=True)
TN_6H7M.to_csv("TN_6H7M.csv", index = False)
TN_6H7N= pd.concat([T_6H7N, N_6H7N], ignore_index=True)
TN_6H7N.to_csv("TN_6H7N.csv", index = False)
TN_6H7O= pd.concat([T_6H7O, N_6H7O], ignore_index=True)
TN_6H7O.to_csv("TN_6H7O.csv", index = False)
TN_6HLL= pd.concat([T_6HLL, N_6HLL], ignore_index=True)
TN_6HLL.to_csv("TN_6HLL.csv", index = False)
TN_6HLO= pd.concat([T_6HLO, N_6HLO], ignore_index=True)
TN_6HLO.to_csv("TN_6HLO.csv", index = False)
TN_6HLP= pd.concat([T_6HLP, N_6HLP], ignore_index=True)
TN_6HLP.to_csv("TN_6HLP.csv", index = False)
TN_6IBL= pd.concat([T_6IBL, N_6IBL], ignore_index=True)
TN_6IBL.to_csv("TN_6IBL.csv", index = False)
TN_6IIU= pd.concat([T_6IIU, N_6IIU], ignore_index=True)
TN_6IIU.to_csv("TN_6IIU.csv", index = False)
TN_6IIV= pd.concat([T_6IIV, N_6IIV], ignore_index=True)
TN_6IIV.to_csv("TN_6IIV.csv", index = False)
TN_6IQL= pd.concat([T_6IQL, N_6IQL], ignore_index=True)
TN_6IQL.to_csv("TN_6IQL.csv", index = False)
TN_6J20= pd.concat([T_6J20, N_6J20], ignore_index=True)
TN_6J20.to_csv("TN_6J20.csv", index = False)
TN_6JZH= pd.concat([T_6JZH, N_6JZH], ignore_index=True)
TN_6JZH.to_csv("TN_6JZH.csv", index = False)
TN_6K1Q= pd.concat([T_6K1Q, N_6K1Q], ignore_index=True)
TN_6K1Q.to_csv("TN_6K1Q.csv", index = False)
TN_6M9T= pd.concat([T_6M9T, N_6M9T], ignore_index=True)
TN_6M9T.to_csv("TN_6M9T.csv", index = False)
TN_6ME2= pd.concat([T_6ME2, N_6ME2], ignore_index=True)
TN_6ME2.to_csv("TN_6ME2.csv", index = False)
TN_6ME3= pd.concat([T_6ME3, N_6ME3], ignore_index=True)
TN_6ME3.to_csv("TN_6ME3.csv", index = False)
TN_6ME4= pd.concat([T_6ME4, N_6ME4], ignore_index=True)
TN_6ME4.to_csv("TN_6ME4.csv", index = False)
TN_6ME5= pd.concat([T_6ME5, N_6ME5], ignore_index=True)
TN_6ME5.to_csv("TN_6ME5.csv", index = False)
TN_6ME6= pd.concat([T_6ME6, N_6ME6], ignore_index=True)
TN_6ME6.to_csv("TN_6ME6.csv", index = False)
TN_6ME7= pd.concat([T_6ME7, N_6ME7], ignore_index=True)
TN_6ME7.to_csv("TN_6ME7.csv", index = False)
TN_6ME8= pd.concat([T_6ME8, N_6ME8], ignore_index=True)
TN_6ME8.to_csv("TN_6ME8.csv", index = False)
TN_6ME9= pd.concat([T_6ME9, N_6ME9], ignore_index=True)
TN_6ME9.to_csv("TN_6ME9.csv", index = False)
TN_6MH8= pd.concat([T_6MH8, N_6MH8], ignore_index=True)
TN_6MH8.to_csv("TN_6MH8.csv", index = False)
TN_6MXT= pd.concat([T_6MXT, N_6MXT], ignore_index=True)
TN_6MXT.to_csv("TN_6MXT.csv", index = False)
TN_6N48= pd.concat([T_6N48, N_6N48], ignore_index=True)
TN_6N48.to_csv("TN_6N48.csv", index = False)
TN_6OL9= pd.concat([T_6OL9, N_6OL9], ignore_index=True)
TN_6OL9.to_csv("TN_6OL9.csv", index = False)
TN_6PRZ= pd.concat([T_6PRZ, N_6PRZ], ignore_index=True)
TN_6PRZ.to_csv("TN_6PRZ.csv", index = False)
TN_6PS0= pd.concat([T_6PS0, N_6PS0], ignore_index=True)
TN_6PS0.to_csv("TN_6PS0.csv", index = False)
TN_6PS1= pd.concat([T_6PS1, N_6PS1], ignore_index=True)
TN_6PS1.to_csv("TN_6PS1.csv", index = False)
TN_6PS2= pd.concat([T_6PS2, N_6PS2], ignore_index=True)
TN_6PS2.to_csv("TN_6PS2.csv", index = False)
TN_6PS3= pd.concat([T_6PS3, N_6PS3], ignore_index=True)
TN_6PS3.to_csv("TN_6PS3.csv", index = False)
TN_6PS4= pd.concat([T_6PS4, N_6PS4], ignore_index=True)
TN_6PS4.to_csv("TN_6PS4.csv", index = False)
TN_6PS5= pd.concat([T_6PS5, N_6PS5], ignore_index=True)
TN_6PS5.to_csv("TN_6PS5.csv", index = False)
TN_6PS6= pd.concat([T_6PS6, N_6PS6], ignore_index=True)
TN_6PS6.to_csv("TN_6PS6.csv", index = False)
TN_6PS7= pd.concat([T_6PS7, N_6PS7], ignore_index=True)
TN_6PS7.to_csv("TN_6PS7.csv", index = False)
TN_6PS8= pd.concat([T_6PS8, N_6PS8], ignore_index=True)
TN_6PS8.to_csv("TN_6PS8.csv", index = False)
TN_6QZH= pd.concat([T_6QZH, N_6QZH], ignore_index=True)
TN_6QZH.to_csv("TN_6QZH.csv", index = False)
TN_6RZ4= pd.concat([T_6RZ4, N_6RZ4], ignore_index=True)
TN_6RZ4.to_csv("TN_6RZ4.csv", index = False)
TN_6TP3= pd.concat([T_6TP3, N_6TP3], ignore_index=True)
TN_6TP3.to_csv("TN_6TP3.csv", index = False)
TN_6TP4= pd.concat([T_6TP4, N_6TP4], ignore_index=True)
TN_6TP4.to_csv("TN_6TP4.csv", index = False)
TN_6TP6= pd.concat([T_6TP6, N_6TP6], ignore_index=True)
TN_6TP6.to_csv("TN_6TP6.csv", index = False)
TN_6TPG= pd.concat([T_6TPG, N_6TPG], ignore_index=True)
TN_6TPG.to_csv("TN_6TPG.csv", index = False)
TN_6TPN= pd.concat([T_6TPN, N_6TPN], ignore_index=True)
TN_6TPN.to_csv("TN_6TPN.csv", index = False)
```


```python

```


```python

```

## information
# 조건을 둘다 만족해야 할때
df[(조건1) & (조건2)]

# 조건 중 하나라도 만족하면 될때
df[(조건1) | (조건2)]