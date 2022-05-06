## 전 작업에서 제작한 데이터 프레임을 하나로 합치는 작업 


```python
import os
import pandas as pd
from io import StringIOㅁ
```


```python
path = "./TN_Balance_n20_181" 
file_list = os.listdir(path) # 파일 이름 리스트로 설정
```


```python
for i in file_list:
    globals()[i[0:7]] = pd.read_csv("./TN_Balance_n20_181/"+i) # df=pd.read_csv("./MATRIX_198/Matrix_2I35.csv")
```


```python
TN_2I35.shape
```




    (20, 2945)



### None 데이터에서 데이터 프레임을 Concat 시킴


```python
### 이상 없이 작동함
df = None  ## 데이터 없음
df_PDB = pd.concat([df, TN_2I35], ignore_index=True)
```

## 많은 파일에 적용 -- 파일을 자동으로 읽고 Matrix 형태로 데이터를 제작


```python
### 변수를 자동으로 선언하는 코드
path = "./TN_Balance_n20_181" 
file_list = os.listdir(path) # 파일 이름 리스트로 설정
for i in file_list:
    globals()[i[0:7]] = pd.read_csv("./TN_Balance_n20_181/"+i)
    
print("변수적용 완료")
print("변수 형태 TN_XXXX")
```

    변수적용 완료
    변수 형태 TN_XXXX
    


```python
### 생성된 변수를 자동으로 concat시키는 코드
df = None  ## 비어 있는ㅁ
for i in file_list:
    df = pd.concat([df, globals()[i[0:7]]], ignore_index=True)

print("이상없이 작동함")
```


```python
### NaN값 0으로 채우기
df_fillna = df.fillna(0)
```


```python
### RMSD 정보를 정확하게 T/N으로 Define함
df_fillna.loc[df_fillna['r_i_glide_rmsd_to_input'] <= 2.0, 'Label'] = 'T'  ## 다른 함수 처럼 변수로 설정할 필요 없이 바로 적용됨
df_fillna.loc[df_fillna['r_i_glide_rmsd_to_input'] > 2.0, 'Label'] = 'N' ## 다른 함수 처럼 변수로 설정할 필요 없이 바로 적용됨
```


```python
###  RSMD 컬럼을 지운다
df_fillna_change_resd = df_fillna.drop(["r_i_glide_rmsd_to_input"], axis=1) ### drop method는 반드시 axis를 작성해주어야한다.
```


```python
### pd.get_dummies 함수를 사용하여 one-hot encoding을 실시한다.
Label_OHE = pd.get_dummies(df_fillna_change_resd["Label"])
```


```python
### Label 컬럼도 삭제한다.
df_fillna_change_resd_label = df_fillna_change_resd.drop(["Label"], axis=1) 
```


```python
df_fillna_change_resd_label.shape
```




    (3620, 16498)




```python
## one-hot-encoding으로 작업했던 컬럼을 붙힌다.
GPCR_Interaction_Matrix_20 = pd.concat([df_fillna_change_resd_label,Label_OHE['T'],Label_OHE['N']],axis=1)
```


```python
### 저장하기
GPCR_Interaction_Matrix_20.to_csv("GPCR_Interaction_Matrix_20.csv", mode='w', index=None)
```


```python

```
