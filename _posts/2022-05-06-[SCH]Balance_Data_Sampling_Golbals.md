```python
import os
import pandas as pd
from io import StringIO
```


```python
df=pd.read_csv("./MATRIX_232/Matrix_2I35.csv")
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

## 많은 파일에 적용 -- 변수로 적용


```python
import os
import pandas as pd

```

[참고 자료 -- globals 함수](https://boleumdal.tistory.com/entry/Python-%EB%B0%98%EB%B3%B5%EB%AC%B8%EC%97%90%EC%84%9C-%EB%B3%80%EC%88%98-%EC%84%A0%EC%96%B8%ED%95%98%EB%8A%94-%EB%B2%95)


```python
path = "./MATRIX_198" 
file_list = os.listdir(path) # 파일 이름 리스트로 설정
```


```python
for i in file_list:
    df=pd.read_csv("./MATRIX_198/"+i) # df=pd.read_csv("./MATRIX_198/Matrix_2I35.csv")
    df["r_i_glide_rmsd_to_input"] <= 2.0
    globals()["T_"+i[7:11]] = df[df["r_i_glide_rmsd_to_input"] <= 2.0] # ex) T_2I35 = df[df["r_i_glide_rmsd_to_input"] <= 2.0]
    globals()["T_"+i[7:11]] = globals()["T_"+i[7:11]].sample(n=50,replace=True) # ex) T_2I35 = T_2I35.sample(n=40,replace=True)
    df["r_i_glide_rmsd_to_input"] > 2.0
    globals()["N_"+i[7:11]] = df[df["r_i_glide_rmsd_to_input"] <= 2.0] # ex) N_2I35 = df[df["r_i_glide_rmsd_to_input"] > 2.0]
    globals()["N_"+i[7:11]] = globals()["T_"+i[7:11]].sample(n=50,replace=True) # ex) N_2I35 = N_2I35.sample(n=40,replace=True)

print("변수 선언 완료")
```

    변수 선언 완료
    


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
    globals()["TN_"+i[7:11]] = pd.concat([globals()["T_"+i[7:11]], globals()["N_"+i[7:11]]], ignore_index=True) # ex) TN_2I35= pd.concat([T_2I35, N_2I35], ignore_index=True)
```


```python

```

## 저장하기


```python
for i in file_list:
    print('TN_'+i[7:11]+'.to_csv("TN_'+i[7:11]+'.csv", index = True)')
```

    TN_2I35.to_csv("TN_2I35.csv", index = True)
    TN_2RH1.to_csv("TN_2RH1.csv", index = True)
    TN_2VT4.to_csv("TN_2VT4.csv", index = True)
    TN_2X72.to_csv("TN_2X72.csv", index = True)
    TN_2Y00.to_csv("TN_2Y00.csv", index = True)
    TN_2Y01.to_csv("TN_2Y01.csv", index = True)
    TN_2Y02.to_csv("TN_2Y02.csv", index = True)
    TN_2Y03.to_csv("TN_2Y03.csv", index = True)
    TN_2Y04.to_csv("TN_2Y04.csv", index = True)
    TN_2YCW.to_csv("TN_2YCW.csv", index = True)
    TN_2YCX.to_csv("TN_2YCX.csv", index = True)
    TN_2YCY.to_csv("TN_2YCY.csv", index = True)
    TN_2YCZ.to_csv("TN_2YCZ.csv", index = True)
    TN_2YDV.to_csv("TN_2YDV.csv", index = True)
    TN_3D4S.to_csv("TN_3D4S.csv", index = True)
    TN_3NY8.to_csv("TN_3NY8.csv", index = True)
    TN_3NY9.to_csv("TN_3NY9.csv", index = True)
    TN_3NYA.to_csv("TN_3NYA.csv", index = True)
    TN_3OE8.to_csv("TN_3OE8.csv", index = True)
    TN_3P0G.to_csv("TN_3P0G.csv", index = True)
    TN_3UON.to_csv("TN_3UON.csv", index = True)
    TN_3V2W.to_csv("TN_3V2W.csv", index = True)
    TN_3V2Y.to_csv("TN_3V2Y.csv", index = True)
    TN_3VGA.to_csv("TN_3VGA.csv", index = True)
    TN_3VW7.to_csv("TN_3VW7.csv", index = True)
    TN_3ZPQ.to_csv("TN_3ZPQ.csv", index = True)
    TN_3ZPR.to_csv("TN_3ZPR.csv", index = True)
    TN_4AMJ.to_csv("TN_4AMJ.csv", index = True)
    TN_4BVN.to_csv("TN_4BVN.csv", index = True)
    TN_4DAJ.to_csv("TN_4DAJ.csv", index = True)
    TN_4EA3.to_csv("TN_4EA3.csv", index = True)
    TN_4EIY.to_csv("TN_4EIY.csv", index = True)
    TN_4EJ4.to_csv("TN_4EJ4.csv", index = True)
    TN_4GBR.to_csv("TN_4GBR.csv", index = True)
    TN_4IAQ.to_csv("TN_4IAQ.csv", index = True)
    TN_4IAR.to_csv("TN_4IAR.csv", index = True)
    TN_4IB4.to_csv("TN_4IB4.csv", index = True)
    TN_4JKV.to_csv("TN_4JKV.csv", index = True)
    TN_4K5Y.to_csv("TN_4K5Y.csv", index = True)
    TN_4LDE.to_csv("TN_4LDE.csv", index = True)
    TN_4LDL.to_csv("TN_4LDL.csv", index = True)
    TN_4LDO.to_csv("TN_4LDO.csv", index = True)
    TN_4MBS.to_csv("TN_4MBS.csv", index = True)
    TN_4MQS.to_csv("TN_4MQS.csv", index = True)
    TN_4MQT.to_csv("TN_4MQT.csv", index = True)
    TN_4N4W.to_csv("TN_4N4W.csv", index = True)
    TN_4N6H.to_csv("TN_4N6H.csv", index = True)
    TN_4NTJ.to_csv("TN_4NTJ.csv", index = True)
    TN_4O9R.to_csv("TN_4O9R.csv", index = True)
    TN_4OO9.to_csv("TN_4OO9.csv", index = True)
    TN_4OR2.to_csv("TN_4OR2.csv", index = True)
    TN_4PXZ.to_csv("TN_4PXZ.csv", index = True)
    TN_4PY0.to_csv("TN_4PY0.csv", index = True)
    TN_4QIM.to_csv("TN_4QIM.csv", index = True)
    TN_4QIN.to_csv("TN_4QIN.csv", index = True)
    TN_4S0V.to_csv("TN_4S0V.csv", index = True)
    TN_4U14.to_csv("TN_4U14.csv", index = True)
    TN_4U16.to_csv("TN_4U16.csv", index = True)
    TN_4UG2.to_csv("TN_4UG2.csv", index = True)
    TN_4UHR.to_csv("TN_4UHR.csv", index = True)
    TN_4XNW.to_csv("TN_4XNW.csv", index = True)
    TN_4YAY.to_csv("TN_4YAY.csv", index = True)
    TN_4Z34.to_csv("TN_4Z34.csv", index = True)
    TN_4Z36.to_csv("TN_4Z36.csv", index = True)
    TN_4Z9G.to_csv("TN_4Z9G.csv", index = True)
    TN_4ZUD.to_csv("TN_4ZUD.csv", index = True)
    TN_5C1M.to_csv("TN_5C1M.csv", index = True)
    TN_5CGC.to_csv("TN_5CGC.csv", index = True)
    TN_5CGD.to_csv("TN_5CGD.csv", index = True)
    TN_5CXV.to_csv("TN_5CXV.csv", index = True)
    TN_5D5B.to_csv("TN_5D5B.csv", index = True)
    TN_5D6L.to_csv("TN_5D6L.csv", index = True)
    TN_5DHG.to_csv("TN_5DHG.csv", index = True)
    TN_5DHH.to_csv("TN_5DHH.csv", index = True)
    TN_5DSG.to_csv("TN_5DSG.csv", index = True)
    TN_5F8U.to_csv("TN_5F8U.csv", index = True)
    TN_5G53.to_csv("TN_5G53.csv", index = True)
    TN_5IU4.to_csv("TN_5IU4.csv", index = True)
    TN_5IU7.to_csv("TN_5IU7.csv", index = True)
    TN_5IU8.to_csv("TN_5IU8.csv", index = True)
    TN_5IUA.to_csv("TN_5IUA.csv", index = True)
    TN_5IUB.to_csv("TN_5IUB.csv", index = True)
    TN_5JQH.to_csv("TN_5JQH.csv", index = True)
    TN_5K2B.to_csv("TN_5K2B.csv", index = True)
    TN_5K2D.to_csv("TN_5K2D.csv", index = True)
    TN_5L7I.to_csv("TN_5L7I.csv", index = True)
    TN_5LWE.to_csv("TN_5LWE.csv", index = True)
    TN_5MZJ.to_csv("TN_5MZJ.csv", index = True)
    TN_5N2R.to_csv("TN_5N2R.csv", index = True)
    TN_5N2S.to_csv("TN_5N2S.csv", index = True)
    TN_5NDD.to_csv("TN_5NDD.csv", index = True)
    TN_5NLX.to_csv("TN_5NLX.csv", index = True)
    TN_5NM2.to_csv("TN_5NM2.csv", index = True)
    TN_5NM4.to_csv("TN_5NM4.csv", index = True)
    TN_5OLG.to_csv("TN_5OLG.csv", index = True)
    TN_5OLH.to_csv("TN_5OLH.csv", index = True)
    TN_5OLO.to_csv("TN_5OLO.csv", index = True)
    TN_5OLV.to_csv("TN_5OLV.csv", index = True)
    TN_5OLZ.to_csv("TN_5OLZ.csv", index = True)
    TN_5OM1.to_csv("TN_5OM1.csv", index = True)
    TN_5OM4.to_csv("TN_5OM4.csv", index = True)
    TN_5TGZ.to_csv("TN_5TGZ.csv", index = True)
    TN_5TUD.to_csv("TN_5TUD.csv", index = True)
    TN_5TVN.to_csv("TN_5TVN.csv", index = True)
    TN_5UIG.to_csv("TN_5UIG.csv", index = True)
    TN_5UNH.to_csv("TN_5UNH.csv", index = True)
    TN_5UVI.to_csv("TN_5UVI.csv", index = True)
    TN_5V54.to_csv("TN_5V54.csv", index = True)
    TN_5V56.to_csv("TN_5V56.csv", index = True)
    TN_5V57.to_csv("TN_5V57.csv", index = True)
    TN_5VRA.to_csv("TN_5VRA.csv", index = True)
    TN_5WIU.to_csv("TN_5WIU.csv", index = True)
    TN_5WIV.to_csv("TN_5WIV.csv", index = True)
    TN_5X7D.to_csv("TN_5X7D.csv", index = True)
    TN_5XPR.to_csv("TN_5XPR.csv", index = True)
    TN_5XR8.to_csv("TN_5XR8.csv", index = True)
    TN_5XRA.to_csv("TN_5XRA.csv", index = True)
    TN_5ZBQ.to_csv("TN_5ZBQ.csv", index = True)
    TN_5ZHP.to_csv("TN_5ZHP.csv", index = True)
    TN_5ZK3.to_csv("TN_5ZK3.csv", index = True)
    TN_5ZK8.to_csv("TN_5ZK8.csv", index = True)
    TN_5ZKB.to_csv("TN_5ZKB.csv", index = True)
    TN_5ZKC.to_csv("TN_5ZKC.csv", index = True)
    TN_5ZKP.to_csv("TN_5ZKP.csv", index = True)
    TN_5ZKQ.to_csv("TN_5ZKQ.csv", index = True)
    TN_5ZTY.to_csv("TN_5ZTY.csv", index = True)
    TN_6A93.to_csv("TN_6A93.csv", index = True)
    TN_6A94.to_csv("TN_6A94.csv", index = True)
    TN_6AKX.to_csv("TN_6AKX.csv", index = True)
    TN_6B73.to_csv("TN_6B73.csv", index = True)
    TN_6BQG.to_csv("TN_6BQG.csv", index = True)
    TN_6BQH.to_csv("TN_6BQH.csv", index = True)
    TN_6CM4.to_csv("TN_6CM4.csv", index = True)
    TN_6D26.to_csv("TN_6D26.csv", index = True)
    TN_6DRX.to_csv("TN_6DRX.csv", index = True)
    TN_6DRY.to_csv("TN_6DRY.csv", index = True)
    TN_6DRZ.to_csv("TN_6DRZ.csv", index = True)
    TN_6DS0.to_csv("TN_6DS0.csv", index = True)
    TN_6E59.to_csv("TN_6E59.csv", index = True)
    TN_6E67.to_csv("TN_6E67.csv", index = True)
    TN_6FFH.to_csv("TN_6FFH.csv", index = True)
    TN_6FFI.to_csv("TN_6FFI.csv", index = True)
    TN_6FK6.to_csv("TN_6FK6.csv", index = True)
    TN_6FK7.to_csv("TN_6FK7.csv", index = True)
    TN_6FK8.to_csv("TN_6FK8.csv", index = True)
    TN_6FK9.to_csv("TN_6FK9.csv", index = True)
    TN_6FKA.to_csv("TN_6FKA.csv", index = True)
    TN_6FKB.to_csv("TN_6FKB.csv", index = True)
    TN_6FKD.to_csv("TN_6FKD.csv", index = True)
    TN_6GDG.to_csv("TN_6GDG.csv", index = True)
    TN_6GPS.to_csv("TN_6GPS.csv", index = True)
    TN_6GPX.to_csv("TN_6GPX.csv", index = True)
    TN_6GT3.to_csv("TN_6GT3.csv", index = True)
    TN_6H7J.to_csv("TN_6H7J.csv", index = True)
    TN_6H7L.to_csv("TN_6H7L.csv", index = True)
    TN_6H7M.to_csv("TN_6H7M.csv", index = True)
    TN_6H7N.to_csv("TN_6H7N.csv", index = True)
    TN_6H7O.to_csv("TN_6H7O.csv", index = True)
    TN_6HLL.to_csv("TN_6HLL.csv", index = True)
    TN_6HLO.to_csv("TN_6HLO.csv", index = True)
    TN_6HLP.to_csv("TN_6HLP.csv", index = True)
    TN_6IBL.to_csv("TN_6IBL.csv", index = True)
    TN_6IIU.to_csv("TN_6IIU.csv", index = True)
    TN_6IIV.to_csv("TN_6IIV.csv", index = True)
    TN_6IQL.to_csv("TN_6IQL.csv", index = True)
    TN_6J20.to_csv("TN_6J20.csv", index = True)
    TN_6JZH.to_csv("TN_6JZH.csv", index = True)
    TN_6K1Q.to_csv("TN_6K1Q.csv", index = True)
    TN_6M9T.to_csv("TN_6M9T.csv", index = True)
    TN_6ME2.to_csv("TN_6ME2.csv", index = True)
    TN_6ME3.to_csv("TN_6ME3.csv", index = True)
    TN_6ME4.to_csv("TN_6ME4.csv", index = True)
    TN_6ME5.to_csv("TN_6ME5.csv", index = True)
    TN_6ME6.to_csv("TN_6ME6.csv", index = True)
    TN_6ME7.to_csv("TN_6ME7.csv", index = True)
    TN_6ME8.to_csv("TN_6ME8.csv", index = True)
    TN_6ME9.to_csv("TN_6ME9.csv", index = True)
    TN_6MH8.to_csv("TN_6MH8.csv", index = True)
    TN_6MXT.to_csv("TN_6MXT.csv", index = True)
    TN_6N48.to_csv("TN_6N48.csv", index = True)
    TN_6OL9.to_csv("TN_6OL9.csv", index = True)
    TN_6PRZ.to_csv("TN_6PRZ.csv", index = True)
    TN_6PS0.to_csv("TN_6PS0.csv", index = True)
    TN_6PS1.to_csv("TN_6PS1.csv", index = True)
    TN_6PS2.to_csv("TN_6PS2.csv", index = True)
    TN_6PS3.to_csv("TN_6PS3.csv", index = True)
    TN_6PS4.to_csv("TN_6PS4.csv", index = True)
    TN_6PS5.to_csv("TN_6PS5.csv", index = True)
    TN_6PS6.to_csv("TN_6PS6.csv", index = True)
    TN_6PS7.to_csv("TN_6PS7.csv", index = True)
    TN_6PS8.to_csv("TN_6PS8.csv", index = True)
    TN_6QZH.to_csv("TN_6QZH.csv", index = True)
    TN_6RZ4.to_csv("TN_6RZ4.csv", index = True)
    TN_6TP3.to_csv("TN_6TP3.csv", index = True)
    TN_6TP4.to_csv("TN_6TP4.csv", index = True)
    TN_6TP6.to_csv("TN_6TP6.csv", index = True)
    TN_6TPG.to_csv("TN_6TPG.csv", index = True)
    TN_6TPN.to_csv("TN_6TPN.csv", index = True)
    


```python
for i in file_list:
    globals()["TN_"+i[7:11]].to_csv(globals()["TN_"+i[7:11]+".csv"], index = True)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-99-7c2425e2470e> in <module>
          1 for i in file_list:
    ----> 2     globals()["TN_"+i[7:11]].to_csv(globals()["TN_"+i[7:11]+".csv"], index = True)
    

    KeyError: 'TN_2I35.csv'



```python
TN_2I35.to_csv("TN_2I35.csv", index = True)
TN_2RH1.to_csv("TN_2RH1.csv", index = True)
TN_2VT4.to_csv("TN_2VT4.csv", index = True)
TN_2X72.to_csv("TN_2X72.csv", index = True)
TN_2Y00.to_csv("TN_2Y00.csv", index = True)
TN_2Y01.to_csv("TN_2Y01.csv", index = True)
TN_2Y02.to_csv("TN_2Y02.csv", index = True)
TN_2Y03.to_csv("TN_2Y03.csv", index = True)
TN_2Y04.to_csv("TN_2Y04.csv", index = True)
TN_2YCW.to_csv("TN_2YCW.csv", index = True)
TN_2YCX.to_csv("TN_2YCX.csv", index = True)
TN_2YCY.to_csv("TN_2YCY.csv", index = True)
TN_2YCZ.to_csv("TN_2YCZ.csv", index = True)
TN_2YDV.to_csv("TN_2YDV.csv", index = True)
TN_3D4S.to_csv("TN_3D4S.csv", index = True)
TN_3NY8.to_csv("TN_3NY8.csv", index = True)
TN_3NY9.to_csv("TN_3NY9.csv", index = True)
TN_3NYA.to_csv("TN_3NYA.csv", index = True)
TN_3OE8.to_csv("TN_3OE8.csv", index = True)
TN_3P0G.to_csv("TN_3P0G.csv", index = True)
TN_3UON.to_csv("TN_3UON.csv", index = True)
TN_3V2W.to_csv("TN_3V2W.csv", index = True)
TN_3V2Y.to_csv("TN_3V2Y.csv", index = True)
TN_3VGA.to_csv("TN_3VGA.csv", index = True)
TN_3VW7.to_csv("TN_3VW7.csv", index = True)
TN_3ZPQ.to_csv("TN_3ZPQ.csv", index = True)
TN_3ZPR.to_csv("TN_3ZPR.csv", index = True)
TN_4AMJ.to_csv("TN_4AMJ.csv", index = True)
TN_4BVN.to_csv("TN_4BVN.csv", index = True)
TN_4DAJ.to_csv("TN_4DAJ.csv", index = True)
TN_4EA3.to_csv("TN_4EA3.csv", index = True)
TN_4EIY.to_csv("TN_4EIY.csv", index = True)
TN_4EJ4.to_csv("TN_4EJ4.csv", index = True)
TN_4GBR.to_csv("TN_4GBR.csv", index = True)
TN_4IAQ.to_csv("TN_4IAQ.csv", index = True)
TN_4IAR.to_csv("TN_4IAR.csv", index = True)
TN_4IB4.to_csv("TN_4IB4.csv", index = True)
TN_4JKV.to_csv("TN_4JKV.csv", index = True)
TN_4K5Y.to_csv("TN_4K5Y.csv", index = True)
TN_4LDE.to_csv("TN_4LDE.csv", index = True)
TN_4LDL.to_csv("TN_4LDL.csv", index = True)
TN_4LDO.to_csv("TN_4LDO.csv", index = True)
TN_4MBS.to_csv("TN_4MBS.csv", index = True)
TN_4MQS.to_csv("TN_4MQS.csv", index = True)
TN_4MQT.to_csv("TN_4MQT.csv", index = True)
TN_4N4W.to_csv("TN_4N4W.csv", index = True)
TN_4N6H.to_csv("TN_4N6H.csv", index = True)
TN_4NTJ.to_csv("TN_4NTJ.csv", index = True)
TN_4O9R.to_csv("TN_4O9R.csv", index = True)
TN_4OO9.to_csv("TN_4OO9.csv", index = True)
TN_4OR2.to_csv("TN_4OR2.csv", index = True)
TN_4PXZ.to_csv("TN_4PXZ.csv", index = True)
TN_4PY0.to_csv("TN_4PY0.csv", index = True)
TN_4QIM.to_csv("TN_4QIM.csv", index = True)
TN_4QIN.to_csv("TN_4QIN.csv", index = True)
TN_4S0V.to_csv("TN_4S0V.csv", index = True)
TN_4U14.to_csv("TN_4U14.csv", index = True)
TN_4U16.to_csv("TN_4U16.csv", index = True)
TN_4UG2.to_csv("TN_4UG2.csv", index = True)
TN_4UHR.to_csv("TN_4UHR.csv", index = True)
TN_4XNW.to_csv("TN_4XNW.csv", index = True)
TN_4YAY.to_csv("TN_4YAY.csv", index = True)
TN_4Z34.to_csv("TN_4Z34.csv", index = True)
TN_4Z36.to_csv("TN_4Z36.csv", index = True)
TN_4Z9G.to_csv("TN_4Z9G.csv", index = True)
TN_4ZUD.to_csv("TN_4ZUD.csv", index = True)
TN_5C1M.to_csv("TN_5C1M.csv", index = True)
TN_5CGC.to_csv("TN_5CGC.csv", index = True)
TN_5CGD.to_csv("TN_5CGD.csv", index = True)
TN_5CXV.to_csv("TN_5CXV.csv", index = True)
TN_5D5B.to_csv("TN_5D5B.csv", index = True)
TN_5D6L.to_csv("TN_5D6L.csv", index = True)
TN_5DHG.to_csv("TN_5DHG.csv", index = True)
TN_5DHH.to_csv("TN_5DHH.csv", index = True)
TN_5DSG.to_csv("TN_5DSG.csv", index = True)
TN_5F8U.to_csv("TN_5F8U.csv", index = True)
TN_5G53.to_csv("TN_5G53.csv", index = True)
TN_5IU4.to_csv("TN_5IU4.csv", index = True)
TN_5IU7.to_csv("TN_5IU7.csv", index = True)
TN_5IU8.to_csv("TN_5IU8.csv", index = True)
TN_5IUA.to_csv("TN_5IUA.csv", index = True)
TN_5IUB.to_csv("TN_5IUB.csv", index = True)
TN_5JQH.to_csv("TN_5JQH.csv", index = True)
TN_5K2B.to_csv("TN_5K2B.csv", index = True)
TN_5K2D.to_csv("TN_5K2D.csv", index = True)
TN_5L7I.to_csv("TN_5L7I.csv", index = True)
TN_5LWE.to_csv("TN_5LWE.csv", index = True)
TN_5MZJ.to_csv("TN_5MZJ.csv", index = True)
TN_5N2R.to_csv("TN_5N2R.csv", index = True)
TN_5N2S.to_csv("TN_5N2S.csv", index = True)
TN_5NDD.to_csv("TN_5NDD.csv", index = True)
TN_5NLX.to_csv("TN_5NLX.csv", index = True)
TN_5NM2.to_csv("TN_5NM2.csv", index = True)
TN_5NM4.to_csv("TN_5NM4.csv", index = True)
TN_5OLG.to_csv("TN_5OLG.csv", index = True)
TN_5OLH.to_csv("TN_5OLH.csv", index = True)
TN_5OLO.to_csv("TN_5OLO.csv", index = True)
TN_5OLV.to_csv("TN_5OLV.csv", index = True)
TN_5OLZ.to_csv("TN_5OLZ.csv", index = True)
TN_5OM1.to_csv("TN_5OM1.csv", index = True)
TN_5OM4.to_csv("TN_5OM4.csv", index = True)
TN_5TGZ.to_csv("TN_5TGZ.csv", index = True)
TN_5TUD.to_csv("TN_5TUD.csv", index = True)
TN_5TVN.to_csv("TN_5TVN.csv", index = True)
TN_5UIG.to_csv("TN_5UIG.csv", index = True)
TN_5UNH.to_csv("TN_5UNH.csv", index = True)
TN_5UVI.to_csv("TN_5UVI.csv", index = True)
TN_5V54.to_csv("TN_5V54.csv", index = True)
TN_5V56.to_csv("TN_5V56.csv", index = True)
TN_5V57.to_csv("TN_5V57.csv", index = True)
TN_5VRA.to_csv("TN_5VRA.csv", index = True)
TN_5WIU.to_csv("TN_5WIU.csv", index = True)
TN_5WIV.to_csv("TN_5WIV.csv", index = True)
TN_5X7D.to_csv("TN_5X7D.csv", index = True)
TN_5XPR.to_csv("TN_5XPR.csv", index = True)
TN_5XR8.to_csv("TN_5XR8.csv", index = True)
TN_5XRA.to_csv("TN_5XRA.csv", index = True)
TN_5ZBQ.to_csv("TN_5ZBQ.csv", index = True)
TN_5ZHP.to_csv("TN_5ZHP.csv", index = True)
TN_5ZK3.to_csv("TN_5ZK3.csv", index = True)
TN_5ZK8.to_csv("TN_5ZK8.csv", index = True)
TN_5ZKB.to_csv("TN_5ZKB.csv", index = True)
TN_5ZKC.to_csv("TN_5ZKC.csv", index = True)
TN_5ZKP.to_csv("TN_5ZKP.csv", index = True)
TN_5ZKQ.to_csv("TN_5ZKQ.csv", index = True)
TN_5ZTY.to_csv("TN_5ZTY.csv", index = True)
TN_6A93.to_csv("TN_6A93.csv", index = True)
TN_6A94.to_csv("TN_6A94.csv", index = True)
TN_6AKX.to_csv("TN_6AKX.csv", index = True)
TN_6B73.to_csv("TN_6B73.csv", index = True)
TN_6BQG.to_csv("TN_6BQG.csv", index = True)
TN_6BQH.to_csv("TN_6BQH.csv", index = True)
TN_6CM4.to_csv("TN_6CM4.csv", index = True)
TN_6D26.to_csv("TN_6D26.csv", index = True)
TN_6DRX.to_csv("TN_6DRX.csv", index = True)
TN_6DRY.to_csv("TN_6DRY.csv", index = True)
TN_6DRZ.to_csv("TN_6DRZ.csv", index = True)
TN_6DS0.to_csv("TN_6DS0.csv", index = True)
TN_6E59.to_csv("TN_6E59.csv", index = True)
TN_6E67.to_csv("TN_6E67.csv", index = True)
TN_6FFH.to_csv("TN_6FFH.csv", index = True)
TN_6FFI.to_csv("TN_6FFI.csv", index = True)
TN_6FK6.to_csv("TN_6FK6.csv", index = True)
TN_6FK7.to_csv("TN_6FK7.csv", index = True)
TN_6FK8.to_csv("TN_6FK8.csv", index = True)
TN_6FK9.to_csv("TN_6FK9.csv", index = True)
TN_6FKA.to_csv("TN_6FKA.csv", index = True)
TN_6FKB.to_csv("TN_6FKB.csv", index = True)
TN_6FKD.to_csv("TN_6FKD.csv", index = True)
TN_6GDG.to_csv("TN_6GDG.csv", index = True)
TN_6GPS.to_csv("TN_6GPS.csv", index = True)
TN_6GPX.to_csv("TN_6GPX.csv", index = True)
TN_6GT3.to_csv("TN_6GT3.csv", index = True)
TN_6H7J.to_csv("TN_6H7J.csv", index = True)
TN_6H7L.to_csv("TN_6H7L.csv", index = True)
TN_6H7M.to_csv("TN_6H7M.csv", index = True)
TN_6H7N.to_csv("TN_6H7N.csv", index = True)
TN_6H7O.to_csv("TN_6H7O.csv", index = True)
TN_6HLL.to_csv("TN_6HLL.csv", index = True)
TN_6HLO.to_csv("TN_6HLO.csv", index = True)
TN_6HLP.to_csv("TN_6HLP.csv", index = True)
TN_6IBL.to_csv("TN_6IBL.csv", index = True)
TN_6IIU.to_csv("TN_6IIU.csv", index = True)
TN_6IIV.to_csv("TN_6IIV.csv", index = True)
TN_6IQL.to_csv("TN_6IQL.csv", index = True)
TN_6J20.to_csv("TN_6J20.csv", index = True)
TN_6JZH.to_csv("TN_6JZH.csv", index = True)
TN_6K1Q.to_csv("TN_6K1Q.csv", index = True)
TN_6M9T.to_csv("TN_6M9T.csv", index = True)
TN_6ME2.to_csv("TN_6ME2.csv", index = True)
TN_6ME3.to_csv("TN_6ME3.csv", index = True)
TN_6ME4.to_csv("TN_6ME4.csv", index = True)
TN_6ME5.to_csv("TN_6ME5.csv", index = True)
TN_6ME6.to_csv("TN_6ME6.csv", index = True)
TN_6ME7.to_csv("TN_6ME7.csv", index = True)
TN_6ME8.to_csv("TN_6ME8.csv", index = True)
TN_6ME9.to_csv("TN_6ME9.csv", index = True)
TN_6MH8.to_csv("TN_6MH8.csv", index = True)
TN_6MXT.to_csv("TN_6MXT.csv", index = True)
TN_6N48.to_csv("TN_6N48.csv", index = True)
TN_6OL9.to_csv("TN_6OL9.csv", index = True)
TN_6PRZ.to_csv("TN_6PRZ.csv", index = True)
TN_6PS0.to_csv("TN_6PS0.csv", index = True)
TN_6PS1.to_csv("TN_6PS1.csv", index = True)
TN_6PS2.to_csv("TN_6PS2.csv", index = True)
TN_6PS3.to_csv("TN_6PS3.csv", index = True)
TN_6PS4.to_csv("TN_6PS4.csv", index = True)
TN_6PS5.to_csv("TN_6PS5.csv", index = True)
TN_6PS6.to_csv("TN_6PS6.csv", index = True)
TN_6PS7.to_csv("TN_6PS7.csv", index = True)
TN_6PS8.to_csv("TN_6PS8.csv", index = True)
TN_6QZH.to_csv("TN_6QZH.csv", index = True)
TN_6RZ4.to_csv("TN_6RZ4.csv", index = True)
TN_6TP3.to_csv("TN_6TP3.csv", index = True)
TN_6TP4.to_csv("TN_6TP4.csv", index = True)
TN_6TP6.to_csv("TN_6TP6.csv", index = True)
TN_6TPG.to_csv("TN_6TPG.csv", index = True)
TN_6TPN.to_csv("TN_6TPN.csv", index = True)
```


```python

```
