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
INPUT_FILE = 'WWW.mol2'
INPUT_FILE_PATH = './WWW.mol2'
SELECT_MOLECULE  = "T2N"

ANION_MOLECULE  = "T2N"
CATION_MOLECULE = "BMI"


CLUSTER_RANGE = 5
DIGGER_RANGE = 5


#####################################################



### STEP 0 Bond 추출 #######################################

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
###
print("Stage0 COMPLETE")

#####################################################


pmol = PandasMol2().read_mol2(INPUT_FILE_PATH)  ### input
Total_system = pmol.df
condition = (pmol.df.subst_name == ANION_MOLECULE) 
Data_Selecte_subst = pmol.df[condition]
Data_Selecte_subst_index = pmol.df[condition].index
#Data_Selecte_subst
#Data_Selecte_subst_index
## 값 setting

find_range = 3    ### input
list_set = []

for i in Data_Selecte_subst_index:
    select_dataframe = None
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
    
    # list_set
    # list_set = [] 위쪽에 빈공간 있음
    for i in range(0,len(Select_Atom_List)+1):
        list_set.extend(Select_Atom_List)
        list_set = set(list_set)  
        list_set = list(list_set)
list_set_bond = [i+1 for i in list_set]


###############################################################################################

#list_set_bond = [i+1 for i in list_set_bond_TEST]
Bond_Atom_result1 = []
Bond_Atom_result2 = []
#list_set_bond1 = [1]  ### while 시작을 위한 잛은 코드
#list_set_bond2 = [1,2] ### while 시작을 위한 잛은 코드


while True:
    
    for i in list_set_bond:
        Bond_Data_Frame_SUM = Bond_Data_Frame.loc[(Bond_Data_Frame['Bond_Atom1'] == int(i))|
                                                  (Bond_Data_Frame['Bond_Atom2'] == int(i))]
        
        Bond_Data_Frame_SUM_ATOM1 = Bond_Data_Frame_SUM["Bond_Atom1"].tolist()
        Bond_Data_Frame_SUM_ATOM2 = Bond_Data_Frame_SUM["Bond_Atom2"].tolist()
        Bond_Data_Frame_SUM_ATOM1_ATOM2 = Bond_Data_Frame_SUM_ATOM1 + Bond_Data_Frame_SUM_ATOM2
        
        for value in Bond_Data_Frame_SUM_ATOM1_ATOM2:
            if value not in Bond_Atom_result1:
                Bond_Atom_result1.append(int(value))
                list_set_bond = Bond_Atom_result1
                list_set_bond1 = Bond_Atom_result1  
    print(len(list_set_bond1))
    for j in list_set_bond:
        Bond_Data_Frame_SUM = Bond_Data_Frame.loc[(Bond_Data_Frame['Bond_Atom1'] == int(j))|
                                                  (Bond_Data_Frame['Bond_Atom2'] == int(j))]

        Bond_Data_Frame_SUM_ATOM1 = Bond_Data_Frame_SUM["Bond_Atom1"].tolist()
        Bond_Data_Frame_SUM_ATOM2 = Bond_Data_Frame_SUM["Bond_Atom2"].tolist()
        Bond_Data_Frame_SUM_ATOM1_ATOM2 = Bond_Data_Frame_SUM_ATOM1 + Bond_Data_Frame_SUM_ATOM2
        for value in Bond_Data_Frame_SUM_ATOM1_ATOM2:
            if value not in Bond_Atom_result2:
                Bond_Atom_result2.append(int(value))
                list_set_bond = Bond_Atom_result2 
                list_set_bond2 = Bond_Atom_result2
    #print(len(list_set_bond1))
    print(len(list_set_bond2))


    if len(list_set_bond1) == len(list_set_bond2):
        break


    
#if len(Bond_Atom_result) > len(list_set_bond):
    #list_set_bond = Bond_Atom_result
        
list_set_bond_rerange = [int(i)-1 for i in Bond_Atom_result2]
print("Stage1 COMPLETE")

##############################################################################################
### STEP 2 선택된 Molecule 인근에 있는 잔기 다시 선택하기#####################################
###############################################################################################


Pre_selected_DF = Total_system.iloc[list_set_bond_rerange]
condition = (Pre_selected_DF.subst_name == CATION_MOLECULE)
Data_Selecte_subst = Pre_selected_DF.loc[condition]
Data_Selecte_subst_index = Pre_selected_DF.loc[condition].index 



find_range = 3    ### input
list_set = []
list_set_bond = []


for i in Data_Selecte_subst_index:
    select_dataframe = None
    select_dataframe = Data_Selecte_subst.loc[i]


    sq1_range = (select_dataframe[['x','y','z']]+find_range)
    sq3_range = (select_dataframe[['x','y','z']]-find_range)

    selected_dataframe = Total_system[(Total_system['x'] <= int(sq1_range["x"])) &
                                      (Total_system['x'] >= int(sq3_range["x"])) &
                                      (Total_system['y'] <= int(sq1_range["y"])) &
                                      (Total_system['y'] >= int(sq3_range["y"])) &
                                      (Total_system['z'] <= int(sq1_range["z"])) &
                                      (Total_system['z'] >= int(sq3_range["z"]))]
                                      

    cal_x = (float(select_dataframe["x"]) - selected_dataframe["x"]).pow(2)
    cal_y = (float(select_dataframe["y"]) - selected_dataframe["y"]).pow(2)
    cal_z = (float(select_dataframe["z"]) - selected_dataframe["z"]).pow(2)
    Distance = (cal_x+cal_y+cal_z)**0.5
    
    #Distance
    
    Distance_index = Distance[(Distance <= find_range)].index
    
    Select_Atom_List=Distance_index.values.tolist()
    
    # list_set
    # list_set = [] 위쪽에 빈공간 있음
    for i in range(0,len(Select_Atom_List)+1):
        list_set.extend(Select_Atom_List)
        list_set = set(list_set) 
        list_set = list(list_set)
        
list_set_bond_TEST = list_set        
list_set_bond = [i+1 for i in list_set] 




############################################################################################


#list_set_bond = [i+1 for i in list_set_bond_TEST]
Bond_Atom_result1 = []
Bond_Atom_result2 = []
#list_set_bond1 = [1]  ### while 시작을 위한 잛은 코드
#list_set_bond2 = [1,2] ### while 시작을 위한 잛은 코드


while True:
    
    for i in list_set_bond:
        Bond_Data_Frame_SUM = Bond_Data_Frame.loc[(Bond_Data_Frame['Bond_Atom1'] == int(i))|
                                                  (Bond_Data_Frame['Bond_Atom2'] == int(i))]
        
        Bond_Data_Frame_SUM_ATOM1 = Bond_Data_Frame_SUM["Bond_Atom1"].tolist()
        Bond_Data_Frame_SUM_ATOM2 = Bond_Data_Frame_SUM["Bond_Atom2"].tolist()
        Bond_Data_Frame_SUM_ATOM1_ATOM2 = Bond_Data_Frame_SUM_ATOM1 + Bond_Data_Frame_SUM_ATOM2
        
        for value in Bond_Data_Frame_SUM_ATOM1_ATOM2:
            if value not in Bond_Atom_result1:
                Bond_Atom_result1.append(int(value))
                list_set_bond = Bond_Atom_result1
                list_set_bond1 = Bond_Atom_result1  
    print(len(list_set_bond1))
    for j in list_set_bond:
        Bond_Data_Frame_SUM = Bond_Data_Frame.loc[(Bond_Data_Frame['Bond_Atom1'] == int(j))|
                                                  (Bond_Data_Frame['Bond_Atom2'] == int(j))]

        Bond_Data_Frame_SUM_ATOM1 = Bond_Data_Frame_SUM["Bond_Atom1"].tolist()
        Bond_Data_Frame_SUM_ATOM2 = Bond_Data_Frame_SUM["Bond_Atom2"].tolist()
        Bond_Data_Frame_SUM_ATOM1_ATOM2 = Bond_Data_Frame_SUM_ATOM1 + Bond_Data_Frame_SUM_ATOM2
        for value in Bond_Data_Frame_SUM_ATOM1_ATOM2:
            if value not in Bond_Atom_result2:
                Bond_Atom_result2.append(int(value))
                list_set_bond = Bond_Atom_result2 
                list_set_bond2 = Bond_Atom_result2
    #print(len(list_set_bond1))
    print(len(list_set_bond2))


    if len(list_set_bond1) == len(list_set_bond2):
        break


    
#if len(Bond_Atom_result) > len(list_set_bond):
    #list_set_bond = Bond_Atom_result
        
list_set_bond_rerange = [int(i)-1 for i in Bond_Atom_result2]
############################################################################################
print("Stage2 COMPLETE")
############################################################################################
### STEP 3 IL_CLUSTER Define
############################################################################################
Interaction_2nd = Total_system.iloc[list_set_bond_rerange]
condition = ((pmol.df.subst_name == CATION_MOLECULE)|(pmol.df.subst_name == ANION_MOLECULE))
IL_Cluster = Interaction_2nd.loc[condition]
IL_Cluster_list = list(IL_Cluster.index)
Pre_selected_DF = Total_system.iloc[IL_Cluster_list]
Data_Selecte_subst = Pre_selected_DF
Data_Selecte_subst_index = Pre_selected_DF.index 

print("Cluster Analysis")
DATA_cluster = Total_system.iloc[IL_Cluster_list]
DATA_cluster['subst_name'].value_counts()







find_range = CLUSTER_RANGE 
list_set = []
list_set_bond = []


for i in Data_Selecte_subst_index:
    select_dataframe = None
    select_dataframe = Data_Selecte_subst.loc[i]
    sq1_range = (select_dataframe[['x','y','z']]+find_range) ### 다른 컬럼은 해당 계산을 받아들이지 못함. 계산할 컬럼만 추출할 필요가 있으며, 해당 설정은 대괄호[[]] 두개를 사용해 컬럼을 설정한다.
    sq3_range = (select_dataframe[['x','y','z']]-find_range)

    selected_dataframe = Total_system[(Total_system['x'] <= int(sq1_range["x"])) &
                                      (Total_system['x'] >= int(sq3_range["x"])) &
                                      (Total_system['y'] <= int(sq1_range["y"])) &
                                      (Total_system['y'] >= int(sq3_range["y"])) &
                                      (Total_system['z'] <= int(sq1_range["z"])) &
                                      (Total_system['z'] >= int(sq3_range["z"]))]
                                      

    cal_x = (float(select_dataframe["x"]) - selected_dataframe["x"]).pow(2)
    cal_y = (float(select_dataframe["y"]) - selected_dataframe["y"]).pow(2)
    cal_z = (float(select_dataframe["z"]) - selected_dataframe["z"]).pow(2)
    Distance = (cal_x+cal_y+cal_z)**0.5
    
    #Distance
    
    Distance_index = Distance[(Distance <= find_range)].index
    Select_Atom_List=Distance_index.values.tolist()
    
    
    for i in range(0,len(Select_Atom_List)+1):
        list_set.extend(Select_Atom_List)
        list_set = set(list_set)  ### 정렬 및 중복제거를 실시하지만 set형태 {}를 사용한다.
        list_set = list(list_set)
        
list_NA_CL = list_set        
#list_set_bond = [i+1 for i in list_set] ### Bond같은 경우 Atom list를 지속적으로 선별해야함.
DATA_Surface_NACL = Total_system.iloc[list_NA_CL]
DATA_Surface_NACL['subst_name'].value_counts()




### 반전 선택 index 로직

Index_revse_list = []
Total_data_index_list = Total_system.index.values.tolist()
for i in Total_data_index_list:
    if i not in list_NA_CL:
        Index_revse_list.append(i)


Pre_selected_DF = Total_system.iloc[Index_revse_list]
Data_Selecte_subst = Pre_selected_DF
Data_Selecte_subst_index = Pre_selected_DF.index 




find_range = DIGGER_RANGE   
list_set = []
list_set_bond = []


for i in Data_Selecte_subst_index:
    select_dataframe = None
    select_dataframe = Data_Selecte_subst.loc[i]


    sq1_range = (select_dataframe[['x','y','z']]+find_range)
    sq3_range = (select_dataframe[['x','y','z']]-find_range)

    selected_dataframe = Total_system[(Total_system['x'] <= int(sq1_range["x"])) &
                                      (Total_system['x'] >= int(sq3_range["x"])) &
                                      (Total_system['y'] <= int(sq1_range["y"])) &
                                      (Total_system['y'] >= int(sq3_range["y"])) &
                                      (Total_system['z'] <= int(sq1_range["z"])) &
                                      (Total_system['z'] >= int(sq3_range["z"]))]
                                      

    cal_x = (float(select_dataframe["x"]) - selected_dataframe["x"]).pow(2)
    cal_y = (float(select_dataframe["y"]) - selected_dataframe["y"]).pow(2)
    cal_z = (float(select_dataframe["z"]) - selected_dataframe["z"]).pow(2)
    Distance = (cal_x+cal_y+cal_z)**0.5
    
    #Distance
    
    Distance_index = Distance[(Distance <= find_range)].index
    
    Select_Atom_List=Distance_index.values.tolist()
    
    # list_set
    # list_set = [] 위쪽에 빈공간 있음
    for i in range(0,len(Select_Atom_List)+1):
        list_set.extend(Select_Atom_List)
        list_set = set(list_set) 
        list_set = list(list_set)
        
list_set_bond_TEST = list_set 
Digger_list = list_set
list_set_bond = [i+1 for i in list_set] 




Index_revse_list = []
Total_data_index_list = Total_system.index.values.tolist()
for i in Total_data_index_list:
    if i not in Digger_list:
        Index_revse_list.append(i)




Pre_selected_DF = Total_system.iloc[Index_revse_list]
condition = (Pre_selected_DF.subst_name == "T5P")
Data_Selecte_subst = Pre_selected_DF.loc[condition]
Data_Selecte_subst_index = Pre_selected_DF.loc[condition].index 
list_set_bond = [i+1 for i in Data_Selecte_subst_index] 




#list_set_bond = [i+1 for i in list_set_bond_TEST]
Bond_Atom_result1 = []
Bond_Atom_result2 = []
#list_set_bond1 = [1]  ### while 시작을 위한 잛은 코드
#list_set_bond2 = [1,2] ### while 시작을 위한 잛은 코드


while True:
    
    for i in list_set_bond:
        Bond_Data_Frame_SUM = Bond_Data_Frame.loc[(Bond_Data_Frame['Bond_Atom1'] == int(i))|
                                                  (Bond_Data_Frame['Bond_Atom2'] == int(i))]
        
        Bond_Data_Frame_SUM_ATOM1 = Bond_Data_Frame_SUM["Bond_Atom1"].tolist()
        Bond_Data_Frame_SUM_ATOM2 = Bond_Data_Frame_SUM["Bond_Atom2"].tolist()
        Bond_Data_Frame_SUM_ATOM1_ATOM2 = Bond_Data_Frame_SUM_ATOM1 + Bond_Data_Frame_SUM_ATOM2
        
        for value in Bond_Data_Frame_SUM_ATOM1_ATOM2:
            if value not in Bond_Atom_result1:
                Bond_Atom_result1.append(int(value))
                list_set_bond = Bond_Atom_result1
                list_set_bond1 = Bond_Atom_result1  
    print(len(list_set_bond1))
    for j in list_set_bond:
        Bond_Data_Frame_SUM = Bond_Data_Frame.loc[(Bond_Data_Frame['Bond_Atom1'] == int(j))|
                                                  (Bond_Data_Frame['Bond_Atom2'] == int(j))]

        Bond_Data_Frame_SUM_ATOM1 = Bond_Data_Frame_SUM["Bond_Atom1"].tolist()
        Bond_Data_Frame_SUM_ATOM2 = Bond_Data_Frame_SUM["Bond_Atom2"].tolist()
        Bond_Data_Frame_SUM_ATOM1_ATOM2 = Bond_Data_Frame_SUM_ATOM1 + Bond_Data_Frame_SUM_ATOM2
        for value in Bond_Data_Frame_SUM_ATOM1_ATOM2:
            if value not in Bond_Atom_result2:
                Bond_Atom_result2.append(int(value))
                list_set_bond = Bond_Atom_result2 
                list_set_bond2 = Bond_Atom_result2
    #print(len(list_set_bond1))
    print(len(list_set_bond2))


    if len(list_set_bond1) == len(list_set_bond2):
        break


    
#if len(Bond_Atom_result) > len(list_set_bond):
    #list_set_bond = Bond_Atom_result
        
list_set_bond_rerange = [int(i)-1 for i in Bond_Atom_result2]

inner_water_list = list_set_bond_rerange




DATA_Inner_Water = Total_system.iloc[inner_water_list]
DATA_Inner_Water['subst_name'].value_counts()

#############################################################################################

import sys
from collections import Counter

INNER_range = DIGGER_RANGE - CLUSTER_RANGE

temp = sys.stdout 
sys.stdout = open(INPUT_FILE+"_inner_"+str(INNER_range)+'.csv', "w")

print(Counter(DATA_cluster['subst_name'])[CATION_MOLECULE],
     Counter(DATA_cluster['subst_name'])[ANION_MOLECULE],
     Counter(DATA_Inner_Water['subst_name'])['T5P'],
     Counter(DATA_Surface_NACL['subst_name'])['NA'],
     Counter(DATA_Surface_NACL['subst_name'])['CL'],sep=',')

sys.stdout.close() 
sys.stdout = temp