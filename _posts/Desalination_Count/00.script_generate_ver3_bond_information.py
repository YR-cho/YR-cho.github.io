import os
import sys

path = "./FILE" 
file_list = os.listdir(path) 


for i in(file_list):
    sys.stdout = open(i+"_inner1_run.py", "w")

    print("""# -*- coding: utf-8 -*-
    
import pandas as pd
import numpy as np
import rdkit
from rdkit import Chem
import biopandas
from biopandas.pdb import PandasPdb
from biopandas.mol2 import PandasMol2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
from collections import Counter



## INPUT PART #######################################
    """) 
    print("INPUT_FILE = "+'"'+i+'"')
    print("INPUT_FILE_PATH = "+'"./'+i+'"')
    
    
    print("CATION_MOLECULE =",'"'+"BMI"+'"')
    print("CATION_ATOM_COUNT =",25)
    print("CATION_weight =",281.16)   


    print("ANION_MOLECULE =",'"'+"T2N"+'"')
    print("ANION_ATOM_COUNT = ",15)
    print("ANION_weight =",139.22)    
    
    
    
    print("WATER_MOLECULE =",'"'+"T5P"+'"')
    print("WATER_ATOM_COUNT =",3)
    print("WATER_weight =",18.02)

    print("SODIUM_ATOM =",'"'+"NA"+'"')
    print("CHLORIDE_ATOM =",'"'+"CL"+'"')
    
    print("SURFACE_RANGE = ",5)
    print("DIGGER_RANGE = ",6)          
      
    
    #### 여기 밑에서 부터는 내용이 들어감
    print(""" 
#####################################################
## Bond information

cnt = 0
find_word = "@<TRIPOS>BOND"
with open(INPUT_FILE, 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    line = None    # 변수 line을 None으로 초기화
    while line != '':
        line = file.readline()
        cnt += 1
        if "@<TRIPOS>BOND" in line:
            FN = cnt
            
        if "@<TRIPOS>SUBSTRUCTURE" in line:
            EN = cnt
#===============================================================================           
f = open(INPUT_FILE_PATH, 'r')
F = f.readlines()[FN:EN-1]
Bond_list = []
for i in range(EN-FN-1):
    DATA = F[int(i)].strip().split()
    Bond_list.append(DATA)
#===============================================================================  
column_name=['Bond_Index', 'Bond_Atom1', 'Bond_Atom2', 'Bond_Case']
Bond_Data_Frame = pd.DataFrame(Bond_list, columns = column_name)
#===============================================================================
Bond_Data_Frame = Bond_Data_Frame.astype({'Bond_Atom1': int, 'Bond_Atom2': int})

#####################################################

##input
pmol = PandasMol2().read_mol2(INPUT_FILE_PATH)  ### input
Total_system = pmol.df


######################################################
## Making Bond information 
######################################################

condition = (pmol.df.subst_name == CATION_MOLECULE) 
Data_Selecte_subst_CATION = pmol.df[condition]
Data_Selecte_subst_CATION_index = pmol.df[condition].index

condition = (pmol.df.subst_name == ANION_MOLECULE) 
Data_Selecte_subst_ANION = pmol.df[condition]
Data_Selecte_subst_ANION_index = pmol.df[condition].index

condition = (pmol.df.subst_name == WATER_MOLECULE) 
Data_Selecte_subst_WATER = pmol.df[condition]
Data_Selecte_subst_WATER_index = pmol.df[condition].index

condition = (pmol.df.subst_name == SODIUM_ATOM) 
Data_Selecte_subst_NA = pmol.df[condition]
Data_Selecte_subst_NA_index = pmol.df[condition].index


condition = (pmol.df.subst_name == CHLORIDE_ATOM) 
Data_Selecte_subst_CL = pmol.df[condition]
Data_Selecte_subst_CL_index = pmol.df[condition].index

######################################################
## Define Bond information 
######################################################

CATION_Residue_LIST = []
for i in range(1, int(len(Data_Selecte_subst_CATION_index)/CATION_ATOM_COUNT)+1):
    ATOM_COUNT = 0  ## while 반복문 초기화
    while ATOM_COUNT < CATION_ATOM_COUNT:    ## 수치 적정 변수로 생각하기  ## 적용 완료
        CATION_Residue_LIST.append("CATION_Res_"+str(i))
        ATOM_COUNT = ATOM_COUNT+1
        
        
ANION_Residue_LIST = []
for i in range(1, int(len(Data_Selecte_subst_ANION_index)/ANION_ATOM_COUNT)+1):
    ATOM_COUNT = 0  ## while 반복문 초기화
    while ATOM_COUNT < ANION_ATOM_COUNT:    ## 수치 적정 변수로 생각하기  ## 적용 완료
        ANION_Residue_LIST.append("ANION_Res_"+str(i))
        ATOM_COUNT = ATOM_COUNT+1       
        
        
WATER_Residue_LIST = []
for i in range(1, int(len(Data_Selecte_subst_WATER_index)/WATER_ATOM_COUNT)+1):
    ATOM_COUNT = 0  ## while 반복문 초기화
    while ATOM_COUNT < WATER_ATOM_COUNT:    ## 수치 적정 변수로 생각하기  ## 적용 완료
        WATER_Residue_LIST.append("WATER_Res_"+str(i))
        ATOM_COUNT = ATOM_COUNT+1        
        
        
NA_Residue_LIST = []
for i in range(1, int(len(Data_Selecte_subst_NA_index)/1)+1):
    ATOM_COUNT = 0  ## while 반복문 초기화
    while ATOM_COUNT < 1:    ## 수치 적정 변수로 생각하기
        NA_Residue_LIST.append("NA_Res_"+str(i))
        ATOM_COUNT = ATOM_COUNT+1        
        
        
CL_Residue_LIST = []
for i in range(1, int(len(Data_Selecte_subst_CL_index)/1)+1):
    ATOM_COUNT = 0  ## while 반복문 초기화
    while ATOM_COUNT < 1:    ## 수치 적정 변수로 생각하기
        CL_Residue_LIST.append("CL_Res_"+str(i))
        ATOM_COUNT = ATOM_COUNT+1        


######################################################
## concat Bond information wiht Origianl DATA
## Total_system_SYSTEM_Reside_DF
######################################################

SYSTEM_Reside_LIST = CATION_Residue_LIST + ANION_Residue_LIST + WATER_Residue_LIST + NA_Residue_LIST + CL_Residue_LIST
SYSTEM_Reside_DF = pd.DataFrame(SYSTEM_Reside_LIST)
SYSTEM_Reside_DF.columns=["Residue_number"]
Total_system_SYSTEM_Reside_DF = pd.concat([Total_system,SYSTEM_Reside_DF],axis=1)

######################################################


######################################################
## Define Cluster
## 
######################################################



######################################################
## Define Cluster
## step 1. 선택한 molecule의 인근 (3A) ATOM 선택하기
######################################################

condition = (pmol.df.subst_name == ANION_MOLECULE)
Data_Selecte_subst = pmol.df[condition]
Data_Selecte_subst_index = pmol.df[condition].index



find_range = 3    ### input
list_set = []

for i in range(0, len(Data_Selecte_subst_index)):
    select_dataframe = None  ## 선택한 데이터 프레임 초기화
    select_dataframe = Data_Selecte_subst.iloc[i]
    #select_dataframe = Data_Selecte_subst.loc[i]


    sq1_range = (select_dataframe[['x','y','z']]+find_range)
    sq3_range = (select_dataframe[['x','y','z']]-find_range)

    selected_dataframe = Total_system_SYSTEM_Reside_DF[(Total_system_SYSTEM_Reside_DF['x'] <= sq1_range["x"]) &
                                                       (Total_system_SYSTEM_Reside_DF['x'] >= sq3_range["x"]) &
                                                       (Total_system_SYSTEM_Reside_DF['y'] <= sq1_range["y"]) &
                                                       (Total_system_SYSTEM_Reside_DF['y'] >= sq3_range["y"]) &
                                                       (Total_system_SYSTEM_Reside_DF['z'] <= sq1_range["z"]) &
                                                       (Total_system_SYSTEM_Reside_DF['z'] >= sq3_range["z"])]
                                      

    cal_x = (float(select_dataframe["x"]) - selected_dataframe["x"]).pow(2)
    cal_y = (float(select_dataframe["y"]) - selected_dataframe["y"]).pow(2)
    cal_z = (float(select_dataframe["z"]) - selected_dataframe["z"]).pow(2)
    Distance = (cal_x+cal_y+cal_z)**0.5
    
    #Distance

    Distance_index = Distance[(Distance <= find_range)].index
    Select_Atom_List = Distance_index.values.tolist()
    
    ##  선택한 원자 선택
    
    # list_set
    # list_set = [] 위쪽에 빈공간 있음
    for i in range(0,len(Select_Atom_List)+1):
        list_set.extend(Select_Atom_List)
        list_set = set(list_set)  
        list_set = list(list_set)
        
        
######################################################
## Define Cluster
## step 2. 선택한 molecule에서 Cation Residue만 선택하기
######################################################     


# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]


######################################################
## Define Cluster
## step 3. 선택한 molecule에서 Cation Residue만 선택하기
######################################################  

Data_Selecte_subst = result[result['subst_name'] == CATION_MOLECULE]
Data_Selecte_subst_index = result[result['subst_name'] == CATION_MOLECULE].index


find_range = 3    ### input
list_set = []

for i in range(0, len(Data_Selecte_subst_index)):
    select_dataframe = None  ## 선택한 데이터 프레임 초기화
    select_dataframe = Data_Selecte_subst.iloc[i]


    sq1_range = (select_dataframe[['x','y','z']]+find_range)
    sq3_range = (select_dataframe[['x','y','z']]-find_range)

    selected_dataframe = Total_system[(Total_system['x'] <= sq1_range["x"]) &
                                      (Total_system['x'] >= sq3_range["x"]) &
                                      (Total_system['y'] <= sq1_range["y"]) &
                                      (Total_system['y'] >= sq3_range["y"]) &
                                      (Total_system['z'] <= sq1_range["z"]) &
                                      (Total_system['z'] >= sq3_range["z"])]
                                      

    cal_x = (float(select_dataframe["x"]) - selected_dataframe["x"]).pow(2)
    cal_y = (float(select_dataframe["y"]) - selected_dataframe["y"]).pow(2)
    cal_z = (float(select_dataframe["z"]) - selected_dataframe["z"]).pow(2)
    Distance = (cal_x+cal_y+cal_z)**0.5
    
    #Distance

    Distance_index = Distance[(Distance <= find_range)].index
    Select_Atom_List=Distance_index.values.tolist()
    
    ##  선택한 원자 선택
    
    # list_set
    # list_set = [] 위쪽에 빈공간 있음
    for i in range(0,len(Select_Atom_List)+1):
        list_set.extend(Select_Atom_List)
        list_set = set(list_set)  
        list_set = list(list_set)


# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]



######################################################
## Define Cluster
## step 4. IL Cluster Define  
######################################################  

IL_Cluster = result[(result['subst_name'] == CATION_MOLECULE)|(result['subst_name'] == ANION_MOLECULE)]
IL_Cluster

######################################################  
######################################################  



######################################################
## Select 5A Surface
## 
######################################################





######################################################
## Select 5A Surface
## step 1. Select 5A surface
######################################################

Data_Selecte_subst = IL_Cluster
Data_Selecte_subst_index = IL_Cluster.index


find_range = SURFACE_RANGE    ### input
list_set = []

for i in range(0, len(Data_Selecte_subst_index)):
    select_dataframe = None  ## 선택한 데이터 프레임 초기화
    select_dataframe = Data_Selecte_subst.iloc[i]


    sq1_range = (select_dataframe[['x','y','z']]+find_range)
    sq3_range = (select_dataframe[['x','y','z']]-find_range)

    selected_dataframe = Total_system[(Total_system['x'] <= sq1_range["x"]) &
                                      (Total_system['x'] >= sq3_range["x"]) &
                                      (Total_system['y'] <= sq1_range["y"]) &
                                      (Total_system['y'] >= sq3_range["y"]) &
                                      (Total_system['z'] <= sq1_range["z"]) &
                                      (Total_system['z'] >= sq3_range["z"])]
                                      

    cal_x = (float(select_dataframe["x"]) - selected_dataframe["x"]).pow(2)
    cal_y = (float(select_dataframe["y"]) - selected_dataframe["y"]).pow(2)
    cal_z = (float(select_dataframe["z"]) - selected_dataframe["z"]).pow(2)
    Distance = (cal_x+cal_y+cal_z)**0.5
    
    #Distance

    Distance_index = Distance[(Distance <= find_range)].index
    Select_Atom_List=Distance_index.values.tolist()
    
    ##  선택한 원자 선택
    
    # list_set
    # list_set = [] 위쪽에 빈공간 있음
    for i in range(0,len(Select_Atom_List)+1):
        list_set.extend(Select_Atom_List)
        list_set = set(list_set)  
        list_set = list(list_set)

# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]

IL_Cluster_surface = result[(result['subst_name'] == CATION_MOLECULE)|
                            (result['subst_name'] == ANION_MOLECULE)|
                            (result['subst_name'] == WATER_MOLECULE)|
                            (result['subst_name'] == SODIUM_ATOM)|
                            (result['subst_name'] == CHLORIDE_ATOM)]




######################################################
## Select 5A Surface
## step 2. Invert
######################################################

IL_Cluster_surface_NAME = IL_Cluster_surface["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_surface_invert = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_surface_NAME)]


######################################################
## Select 5A Surface
## step 3. Select 5A surface From Invert moleuce
######################################################

Data_Selecte_subst = IL_Cluster_surface_invert
Data_Selecte_subst_index = IL_Cluster_surface_invert.index



find_range = DIGGER_RANGE    ### input
list_set = []

for i in range(0, len(Data_Selecte_subst_index)):
    select_dataframe = None  ## 선택한 데이터 프레임 초기화
    select_dataframe = Data_Selecte_subst.iloc[i]


    sq1_range = (select_dataframe[['x','y','z']]+find_range)
    sq3_range = (select_dataframe[['x','y','z']]-find_range)

    selected_dataframe = Total_system[(Total_system['x'] <= sq1_range["x"]) &
                                      (Total_system['x'] >= sq3_range["x"]) &
                                      (Total_system['y'] <= sq1_range["y"]) &
                                      (Total_system['y'] >= sq3_range["y"]) &
                                      (Total_system['z'] <= sq1_range["z"]) &
                                      (Total_system['z'] >= sq3_range["z"])]
                                      

    cal_x = (float(select_dataframe["x"]) - selected_dataframe["x"]).pow(2)
    cal_y = (float(select_dataframe["y"]) - selected_dataframe["y"]).pow(2)
    cal_z = (float(select_dataframe["z"]) - selected_dataframe["z"]).pow(2)
    Distance = (cal_x+cal_y+cal_z)**0.5
    
    #Distance

    Distance_index = Distance[(Distance <= find_range)].index
    Select_Atom_List=Distance_index.values.tolist()
    
    ##  선택한 원자 선택
    
    # list_set
    # list_set = [] 위쪽에 빈공간 있음
    for i in range(0,len(Select_Atom_List)+1):
        list_set.extend(Select_Atom_List)
        list_set = set(list_set)  
        list_set = list(list_set)


# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]

IL_Cluster_digger = result[(result['subst_name'] == CATION_MOLECULE)|
                           (result['subst_name'] == ANION_MOLECULE)|
                           (result['subst_name'] == WATER_MOLECULE)|
                           (result['subst_name'] == SODIUM_ATOM)|
                           (result['subst_name'] == CHLORIDE_ATOM)]
                           
                           
                           
######################################################
## Select 5A Surface
## step 4. Define inside Water using invert
######################################################

IL_Cluster_digger_NAME = IL_Cluster_digger["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_digger_INSIDE = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_digger_NAME)]
INSIDE_water = IL_Cluster_digger_INSIDE[(IL_Cluster_digger_INSIDE['subst_name'] == WATER_MOLECULE)]

######################################################
######################################################




######################################################
## ANALYSIS
## 
######################################################

import sys
from collections import Counter

sys.stdout = open(INPUT_FILE+"_inner_"+str(INNER_range)+'.csv', "w")

# (CMC) CATION_MOLECULE_COUNT
CMC = Counter(IL_Cluster['subst_name'])[CATION_MOLECULE] / CATION_ATOM_COUNT

# (AMC) ANION_MOLECULE_COUNT
AMC = Counter(IL_Cluster['subst_name'])[ANION_MOLECULE] / ANION_ATOM_COUNT

# (WMC) WATER_MOLECULE_COUNT
WMC = Counter(INSIDE_water['subst_name'])['T5P'] / WATER_ATOM_COUNT

Absortion = (WMC*WATER_weight)/((CMC*CATION_weight)+(AMC*ANION_weight)+(WMC*WATER_weight))*100
print(CMC,AMC,WMC,Absortion)

sys.stdout.close() 
sys.stdout = temp

    """)
