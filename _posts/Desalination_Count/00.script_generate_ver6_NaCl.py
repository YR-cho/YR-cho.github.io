import os
import sys

path = "./FILE4" 
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


######################################################  
###################################################### 
 
Data_Selecte_subst = IL_Cluster
Data_Selecte_subst_index = IL_Cluster.index

######################################################
## IL Cluster Surface
## step 1. IL Cluster 1A  
######################################################  

find_range = CLUSTER_SURFACE_RANGE    ### input
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
## IL Cluster Surface
## step 1. IL Cluster 2A  
######################################################  

find_range = CLUSTER_SURFACE_RANGE+1    ### input
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
## IL Cluster Surface
## step 1. IL Cluster 3A  
######################################################  

find_range = CLUSTER_SURFACE_RANGE+2    ### input
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
## IL Cluster Surface
## step 1. IL Cluster 4A  
######################################################  

find_range = CLUSTER_SURFACE_RANGE+3    ### input
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
## IL Cluster Surface
## step 1. IL Cluster 5A  
######################################################  


find_range = CLUSTER_SURFACE_RANGE+4    ### input
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
## IL Cluster Surface
## step 1. IL Cluster 6A  
######################################################  


find_range = CLUSTER_SURFACE_RANGE+5    ### input
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
## IL Cluster Surface
## step 1. IL Cluster 7A  
######################################################  

find_range = CLUSTER_SURFACE_RANGE+6    ### input
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
## IL Cluster Surface
## step 1. IL Cluster 8A  
######################################################  

find_range = CLUSTER_SURFACE_RANGE+7    ### input
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
## IL Cluster Surface
## step 1. IL Cluster 9A  
######################################################  


find_range = CLUSTER_SURFACE_RANGE+8    ### input
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
## IL Cluster Surface
## step 1. IL Cluster 10A  
######################################################  


find_range = CLUSTER_SURFACE_RANGE+9    ### input
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
## IL Cluster Surface
## step 1. IL Cluster 11A  
######################################################  


find_range = CLUSTER_SURFACE_RANGE+10    ### input
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
## IL Cluster Surface
## step 1. IL Cluster 12A  
######################################################  


find_range = CLUSTER_SURFACE_RANGE+11    ### input
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
## ANALYSIS
## 
######################################################

NA1 = len(result1[(result1['subst_name'] == SODIUM_ATOM)])
NA2 = len(result2[(result2['subst_name'] == SODIUM_ATOM)])
NA3 = len(result3[(result3['subst_name'] == SODIUM_ATOM)])
NA4 = len(result4[(result4['subst_name'] == SODIUM_ATOM)])
NA5 = len(result5[(result5['subst_name'] == SODIUM_ATOM)])
NA6 = len(result6[(result6['subst_name'] == SODIUM_ATOM)])
NA7 = len(result7[(result7['subst_name'] == SODIUM_ATOM)])
NA8 = len(result8[(result8['subst_name'] == SODIUM_ATOM)])
NA9 = len(result9[(result9['subst_name'] == SODIUM_ATOM)])
NA10 = len(result10[(result10['subst_name'] == SODIUM_ATOM)])
NA11 = len(result11[(result11['subst_name'] == SODIUM_ATOM)])
NA12 = len(result12[(result12['subst_name'] == SODIUM_ATOM)])

CL1 = len(result1[(result1['subst_name'] == CHLORIDE_ATOM)])
CL2 = len(result2[(result2['subst_name'] == CHLORIDE_ATOM)])
CL3 = len(result3[(result3['subst_name'] == CHLORIDE_ATOM)])
CL4 = len(result4[(result4['subst_name'] == CHLORIDE_ATOM)])
CL5 = len(result5[(result5['subst_name'] == CHLORIDE_ATOM)])
CL6 = len(result6[(result6['subst_name'] == CHLORIDE_ATOM)])
CL7 = len(result7[(result7['subst_name'] == CHLORIDE_ATOM)])
CL8 = len(result8[(result8['subst_name'] == CHLORIDE_ATOM)])
CL9 = len(result9[(result9['subst_name'] == CHLORIDE_ATOM)])
CL10 = len(result10[(result10['subst_name'] == CHLORIDE_ATOM)])
CL11 = len(result11[(result11['subst_name'] == CHLORIDE_ATOM)])
CL12 = len(result12[(result12['subst_name'] == CHLORIDE_ATOM)])


import sys
from collections import Counter

sys.stdout = open(INPUT_FILE+"_NACL_"+str(INNER_range)+'.csv', "w")


print(NA1,NA2,NA3,NA4,NA5,NA6,NA7,NA8,NA9,NA10,NA11,NA12,
      CL1,CL2,CL3,CL4,CL5,CL6,CL7,CL8,CL9,CL10,CL11,CL12,sep=',')


sys.stdout.close() 
#sys.stdout = temp

    """)
