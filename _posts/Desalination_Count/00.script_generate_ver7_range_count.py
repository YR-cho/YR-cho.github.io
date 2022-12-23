import os
import sys

path = "./Emim_Tf2N_2.0M_353K" 
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
    
    
    print("CATION_MOLECULE =",'"'+"EMI"+'"')
    print("CATION_ATOM_COUNT =",19)
    print("CATION_weight =",111.17)   


    print("ANION_MOLECULE =",'"'+"T2N"+'"')
    print("ANION_ATOM_COUNT = ",15)
    print("ANION_weight =",281.16)    
    
    
    
    print("WATER_MOLECULE =",'"'+"T5P"+'"')
    print("WATER_ATOM_COUNT =",3)
    print("WATER_weight =",18.02)

    print("SODIUM_ATOM =",'"'+"NA"+'"')
    print("CHLORIDE_ATOM =",'"'+"CL"+'"')
    
    print("SURFACE_RANGE = ",5)
    print("DIGGER_RANGE = ",6)
    
    print("INNER_range =",''+"DIGGER_RANGE - SURFACE_RANGE"+'') 
    

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
list_set_array = np.array([], dtype= int)


for i in range(0, len(Data_Selecte_subst_index)):
    select_dataframe = None  ## 선택한 데이터 프레임 초기화
    select_dataframe = Data_Selecte_subst.iloc[i]


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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()
        
        
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
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()



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
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()



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
## step 3. Select 5A surface From Invert moleuce --range1
######################################################

Data_Selecte_subst = IL_Cluster_surface_invert
Data_Selecte_subst_index = IL_Cluster_surface_invert.index



find_range = DIGGER_RANGE    ### input
list_set = []
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()


# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result1 = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]


######################################################
## Select 5A Surface
## step 3. Select 5A surface From Invert moleuce --range2
######################################################

find_range = DIGGER_RANGE+1    ### input
list_set = []
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()



# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result2 = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]


######################################################
## Select 5A Surface
## step 3. Select 5A surface From Invert moleuce --range3
######################################################

find_range = DIGGER_RANGE+2    ### input
list_set = []
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()



# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result3 = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]


######################################################
## Select 5A Surface
## step 3. Select 5A surface From Invert moleuce --range4
######################################################


find_range = DIGGER_RANGE+3    ### input
list_set = []
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()



# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result4 = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]


######################################################
## Select 5A Surface
## step 3. Select 5A surface From Invert moleuce --range5
######################################################


find_range = DIGGER_RANGE+4    ### input
list_set = []
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()



# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result5 = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]



######################################################
## Select 5A Surface
## step 3. Select 5A surface From Invert moleuce --range6
######################################################


find_range = DIGGER_RANGE +5   ### input
list_set = []
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()



# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result6 = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]



######################################################
## Select 5A Surface
## step 3. Select 5A surface From Invert moleuce --range7
######################################################


find_range = DIGGER_RANGE+6    ### input
list_set = []
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()



# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result7 = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]



######################################################
## Select 5A Surface
## step 3. Select 5A surface From Invert moleuce --range8
######################################################


find_range = DIGGER_RANGE+7   ### input
list_set = []
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()



# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result8 = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]




######################################################
## Select 5A Surface
## step 3. Select 5A surface From Invert moleuce --range9
######################################################



find_range = DIGGER_RANGE+8    ### input
list_set = []
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()



# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result9 = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]


######################################################
## Select 5A Surface
## step 3. Select 5A surface From Invert moleuce --range10
######################################################



find_range = DIGGER_RANGE +9   ### input
list_set = []
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()



# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result10 = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]



######################################################
## Select 5A Surface
## step 3. Select 5A surface From Invert moleuce --range11
######################################################



find_range = DIGGER_RANGE+10   ### input
list_set = []
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()



# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result11 = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]



######################################################
## Select 5A Surface
## step 3. Select 5A surface From Invert moleuce --range12
######################################################


find_range = DIGGER_RANGE+11   ### input
list_set = []
list_set_array = np.array([], dtype= int)

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
    Select_Atom_List_NP = np.array(Select_Atom_List,dtype=int)
    
    list_set_array = np.append(list_set_array,Select_Atom_List_NP)
list_set_array= np.unique(list_set_array)
list_set = list_set_array.tolist()



# 포함하고자 하는 문자열 리스트 생성
Select_Residue_List = Total_system_SYSTEM_Reside_DF.iloc[list_set][["Residue_number"]].drop_duplicates().squeeze().to_list()

# 해당 list_set 있는 잔기를 선택
result12 = Total_system_SYSTEM_Reside_DF[Total_system_SYSTEM_Reside_DF['Residue_number'].isin(Select_Residue_List)]






######################################################
## Select 5A Surface
## step 3-2. Select Residue
######################################################

IL_Cluster_digger1 = result1[(result1['subst_name'] == CATION_MOLECULE)|
                             (result1['subst_name'] == ANION_MOLECULE)|
                             (result1['subst_name'] == WATER_MOLECULE)|
                             (result1['subst_name'] == SODIUM_ATOM)|
                             (result1['subst_name'] == CHLORIDE_ATOM)]
                             
  
IL_Cluster_digger2 = result2[(result2['subst_name'] == CATION_MOLECULE)|
                             (result2['subst_name'] == ANION_MOLECULE)|
                             (result2['subst_name'] == WATER_MOLECULE)|
                             (result2['subst_name'] == SODIUM_ATOM)|
                             (result2['subst_name'] == CHLORIDE_ATOM)]

IL_Cluster_digger3 = result3[(result3['subst_name'] == CATION_MOLECULE)|
                             (result3['subst_name'] == ANION_MOLECULE)|
                             (result3['subst_name'] == WATER_MOLECULE)|
                             (result3['subst_name'] == SODIUM_ATOM)|
                             (result3['subst_name'] == CHLORIDE_ATOM)]    

IL_Cluster_digger4 = result4[(result4['subst_name'] == CATION_MOLECULE)|
                             (result4['subst_name'] == ANION_MOLECULE)|
                             (result4['subst_name'] == WATER_MOLECULE)|
                             (result4['subst_name'] == SODIUM_ATOM)|
                             (result4['subst_name'] == CHLORIDE_ATOM)]                             

IL_Cluster_digger5 = result5[(result5['subst_name'] == CATION_MOLECULE)|
                             (result5['subst_name'] == ANION_MOLECULE)|
                             (result5['subst_name'] == WATER_MOLECULE)|
                             (result5['subst_name'] == SODIUM_ATOM)|
                             (result5['subst_name'] == CHLORIDE_ATOM)]
                             
IL_Cluster_digger6 = result6[(result6['subst_name'] == CATION_MOLECULE)|
                             (result6['subst_name'] == ANION_MOLECULE)|
                             (result6['subst_name'] == WATER_MOLECULE)|
                             (result6['subst_name'] == SODIUM_ATOM)|
                             (result6['subst_name'] == CHLORIDE_ATOM)]

IL_Cluster_digger7 = result7[(result7['subst_name'] == CATION_MOLECULE)|
                             (result7['subst_name'] == ANION_MOLECULE)|
                             (result7['subst_name'] == WATER_MOLECULE)|
                             (result7['subst_name'] == SODIUM_ATOM)|
                             (result7['subst_name'] == CHLORIDE_ATOM)]

IL_Cluster_digger8 = result8[(result8['subst_name'] == CATION_MOLECULE)|
                             (result8['subst_name'] == ANION_MOLECULE)|
                             (result8['subst_name'] == WATER_MOLECULE)|
                             (result8['subst_name'] == SODIUM_ATOM)|
                             (result8['subst_name'] == CHLORIDE_ATOM)]

IL_Cluster_digger9 = result9[(result9['subst_name'] == CATION_MOLECULE)|
                             (result9['subst_name'] == ANION_MOLECULE)|
                             (result9['subst_name'] == WATER_MOLECULE)|
                             (result9['subst_name'] == SODIUM_ATOM)|
                             (result9['subst_name'] == CHLORIDE_ATOM)]

IL_Cluster_digger10 = result10[(result10['subst_name'] == CATION_MOLECULE)|
                               (result10['subst_name'] == ANION_MOLECULE)|
                               (result10['subst_name'] == WATER_MOLECULE)|
                               (result10['subst_name'] == SODIUM_ATOM)|
                               (result10['subst_name'] == CHLORIDE_ATOM)]

IL_Cluster_digger11 = result11[(result11['subst_name'] == CATION_MOLECULE)|
                               (result11['subst_name'] == ANION_MOLECULE)|
                               (result11['subst_name'] == WATER_MOLECULE)|
                               (result11['subst_name'] == SODIUM_ATOM)|
                               (result11['subst_name'] == CHLORIDE_ATOM)]

IL_Cluster_digger12 = result12[(result12['subst_name'] == CATION_MOLECULE)|
                               (result12['subst_name'] == ANION_MOLECULE)|
                               (result12['subst_name'] == WATER_MOLECULE)|
                               (result12['subst_name'] == SODIUM_ATOM)|
                               (result12['subst_name'] == CHLORIDE_ATOM)]



######################################################
######################################################





######################################################
## Select 5A Surface
## step 4. Define inside Water using invert
######################################################


IL_Cluster_digger_NAME = IL_Cluster_digger1["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_digger_INSIDE = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_digger_NAME)]
INSIDE_water1 = IL_Cluster_digger_INSIDE[(IL_Cluster_digger_INSIDE['subst_name'] == WATER_MOLECULE)]


IL_Cluster_digger_NAME = IL_Cluster_digger2["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_digger_INSIDE = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_digger_NAME)]
INSIDE_water2 = IL_Cluster_digger_INSIDE[(IL_Cluster_digger_INSIDE['subst_name'] == WATER_MOLECULE)]


IL_Cluster_digger_NAME = IL_Cluster_digger3["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_digger_INSIDE = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_digger_NAME)]
INSIDE_water3 = IL_Cluster_digger_INSIDE[(IL_Cluster_digger_INSIDE['subst_name'] == WATER_MOLECULE)]


IL_Cluster_digger_NAME = IL_Cluster_digger4["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_digger_INSIDE = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_digger_NAME)]
INSIDE_water4 = IL_Cluster_digger_INSIDE[(IL_Cluster_digger_INSIDE['subst_name'] == WATER_MOLECULE)]


IL_Cluster_digger_NAME = IL_Cluster_digger5["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_digger_INSIDE = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_digger_NAME)]
INSIDE_water5 = IL_Cluster_digger_INSIDE[(IL_Cluster_digger_INSIDE['subst_name'] == WATER_MOLECULE)]


IL_Cluster_digger_NAME = IL_Cluster_digger6["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_digger_INSIDE = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_digger_NAME)]
INSIDE_water6 = IL_Cluster_digger_INSIDE[(IL_Cluster_digger_INSIDE['subst_name'] == WATER_MOLECULE)]


IL_Cluster_digger_NAME = IL_Cluster_digger7["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_digger_INSIDE = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_digger_NAME)]
INSIDE_water7 = IL_Cluster_digger_INSIDE[(IL_Cluster_digger_INSIDE['subst_name'] == WATER_MOLECULE)]


IL_Cluster_digger_NAME = IL_Cluster_digger8["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_digger_INSIDE = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_digger_NAME)]
INSIDE_water8 = IL_Cluster_digger_INSIDE[(IL_Cluster_digger_INSIDE['subst_name'] == WATER_MOLECULE)]


IL_Cluster_digger_NAME = IL_Cluster_digger9["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_digger_INSIDE = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_digger_NAME)]
INSIDE_water9 = IL_Cluster_digger_INSIDE[(IL_Cluster_digger_INSIDE['subst_name'] == WATER_MOLECULE)]


IL_Cluster_digger_NAME = IL_Cluster_digger10["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_digger_INSIDE = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_digger_NAME)]
INSIDE_water10 = IL_Cluster_digger_INSIDE[(IL_Cluster_digger_INSIDE['subst_name'] == WATER_MOLECULE)]


IL_Cluster_digger_NAME = IL_Cluster_digger11["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_digger_INSIDE = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_digger_NAME)]
INSIDE_water11 = IL_Cluster_digger_INSIDE[(IL_Cluster_digger_INSIDE['subst_name'] == WATER_MOLECULE)]


IL_Cluster_digger_NAME = IL_Cluster_digger12["Residue_number"].drop_duplicates().squeeze().to_list()
IL_Cluster_digger_INSIDE = Total_system_SYSTEM_Reside_DF[~Total_system_SYSTEM_Reside_DF['Residue_number'].isin(IL_Cluster_digger_NAME)]
INSIDE_water12 = IL_Cluster_digger_INSIDE[(IL_Cluster_digger_INSIDE['subst_name'] == WATER_MOLECULE)]


######################################################
######################################################




######################################################
## ANALYSIS 1
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
WMC1 = Counter(INSIDE_water1['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC2 = Counter(INSIDE_water2['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC3 = Counter(INSIDE_water3['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC4 = Counter(INSIDE_water4['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC5 = Counter(INSIDE_water5['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC6 = Counter(INSIDE_water6['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC7 = Counter(INSIDE_water7['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC8 = Counter(INSIDE_water8['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC9 = Counter(INSIDE_water9['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC10 = Counter(INSIDE_water10['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC11 = Counter(INSIDE_water11['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC12 = Counter(INSIDE_water12['subst_name'])['T5P'] / WATER_ATOM_COUNT

Absortion1 = (WMC1*WATER_weight)/((CMC*CATION_weight)+(AMC*ANION_weight)+(WMC1*WATER_weight))*100
Absortion2 = (WMC2*WATER_weight)/((CMC*CATION_weight)+(AMC*ANION_weight)+(WMC2*WATER_weight))*100
Absortion3 = (WMC3*WATER_weight)/((CMC*CATION_weight)+(AMC*ANION_weight)+(WMC3*WATER_weight))*100
Absortion4 = (WMC4*WATER_weight)/((CMC*CATION_weight)+(AMC*ANION_weight)+(WMC4*WATER_weight))*100
Absortion5 = (WMC5*WATER_weight)/((CMC*CATION_weight)+(AMC*ANION_weight)+(WMC5*WATER_weight))*100
Absortion6 = (WMC6*WATER_weight)/((CMC*CATION_weight)+(AMC*ANION_weight)+(WMC6*WATER_weight))*100
Absortion7 = (WMC7*WATER_weight)/((CMC*CATION_weight)+(AMC*ANION_weight)+(WMC7*WATER_weight))*100
Absortion8 = (WMC8*WATER_weight)/((CMC*CATION_weight)+(AMC*ANION_weight)+(WMC8*WATER_weight))*100
Absortion9 = (WMC9*WATER_weight)/((CMC*CATION_weight)+(AMC*ANION_weight)+(WMC9*WATER_weight))*100
Absortion10 = (WMC10*WATER_weight)/((CMC*CATION_weight)+(AMC*ANION_weight)+(WMC10*WATER_weight))*100
Absortion11 = (WMC11*WATER_weight)/((CMC*CATION_weight)+(AMC*ANION_weight)+(WMC11*WATER_weight))*100
Absortion12 = (WMC12*WATER_weight)/((CMC*CATION_weight)+(AMC*ANION_weight)+(WMC12*WATER_weight))*100

print(Absortion1,
      Absortion2,
      Absortion3,
      Absortion4,
      Absortion5,
      Absortion6,
      Absortion7,
      Absortion8,
      Absortion9,
      Absortion10,
      Absortion11,
      Absortion12, sep=',')


sys.stdout.close() 
#sys.stdout = temp

######################################################
## ANALYSIS 1
## 
######################################################


import sys
from collections import Counter

sys.stdout = open(INPUT_FILE+"_COUNT_"+str(INNER_range)+'.csv', "w")


# (WMC) WATER_MOLECULE_COUNT
WMC1 = Counter(INSIDE_water1['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC2 = Counter(INSIDE_water2['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC3 = Counter(INSIDE_water3['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC4 = Counter(INSIDE_water4['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC5 = Counter(INSIDE_water5['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC6 = Counter(INSIDE_water6['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC7 = Counter(INSIDE_water7['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC8 = Counter(INSIDE_water8['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC9 = Counter(INSIDE_water9['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC10 = Counter(INSIDE_water10['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC11 = Counter(INSIDE_water11['subst_name'])['T5P'] / WATER_ATOM_COUNT
WMC12 = Counter(INSIDE_water12['subst_name'])['T5P'] / WATER_ATOM_COUNT

print(WMC1 ,
      WMC2,
      WMC3,
      WMC4,
      WMC5,
      WMC6,
      WMC7,
      WMC8,
      WMC9,
      WMC10,
      WMC11,
      WMC12, sep=',')


sys.stdout.close() 
#sys.stdout = temp



    """)
