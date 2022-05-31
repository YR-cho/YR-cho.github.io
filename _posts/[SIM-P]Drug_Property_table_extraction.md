```python
import os
import pandas as pd
```


```python
df=pd.read_csv("./GPCR_5TGZ_ligand_export.csv")
```

약물 추천 특성 제안 논문 :In Silico Pharmacol. 2015; 3: 6.
####  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4464579/ ####

df["ADMET_Risk"] ### ≤6.5
df["BBB_Filter"] ### 
df["TOX_Risk"] ### ≤1
df["Absn_Risk"] ### <3.5

df["MWt"] ###
df["PSA"] ### <140
df["HBD"] ### <5 
df["HBA"] ### ≤8
df["LogP"] ### ≤4.5
df["S+logD"] ### ≤3.5
df["S+logP"] ### ≤4.5
df["S+Sw"] ### ≥0.010
df["LogS"] ### −6.0 – 0.5
df["RBP"] ### <1.0
### 연구 목적에 따라 추출 조건을 지정한다.


```python
df = pd.read_csv("./GPCR_5TGZ_ligand_export.csv")
df = df[df["ADMET_Risk"] <= 7.0]
#### 1차 추출
#df = df[df["Absn_Risk"] <= 3.5]
df = df[df["TOX_Risk"]  <= 1.0]
#### 2차 추출
df = df[df["PSA"]  <= 140]
#### 3차 추출
df = df[df["LogS"]  >= -6.0]
df = df[df["S+logD"]  <= 3.5]
df = df[df["S+logP"]  <= 4.5]
#df = df[df["S+Sw"]  >= 0.010]
#df = df[df["RBP"]  <= 1.0]

```


```python
df.to_csv("./DEL.csv")
```


```python

```


```python

```

M


```python

```
