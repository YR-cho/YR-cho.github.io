## Glide에서 진행한 Docking 결과를 추출하는 스크립트 제작


```python
import os
```
path = "./" # 파일 경로
file_list = os.listdir(path) ## 해당 디렉토리에 있는 파일을 리스트로 제작함

print ("file_list: {}".format(file_list))

```python
path = "./Dock_result_pv" 
file_list = os.listdir(path) 

print ("file_list: {}".format(file_list))
```

    file_list: ['glide-dock_SP_2I35_pv.maegz', 'glide-dock_SP_2RH1_pv.maegz', 'glide-dock_SP_2VT4_pv.maegz', 'glide-dock_SP_2X72_pv.maegz', 'glide-dock_SP_2Y00_pv.maegz', 'glide-dock_SP_2Y01_pv.maegz', 'glide-dock_SP_2Y02_pv.maegz', 'glide-dock_SP_2Y03_pv.maegz', 'glide-dock_SP_2Y04_pv.maegz', 'glide-dock_SP_2YCW_pv.maegz', 'glide-dock_SP_2YCX_pv.maegz', 'glide-dock_SP_2YCY_pv.maegz', 'glide-dock_SP_2YCZ_pv.maegz', 'glide-dock_SP_2YDV_pv.maegz', 'glide-dock_SP_3D4S_pv.maegz', 'glide-dock_SP_3EML_pv.maegz', 'glide-dock_SP_3NY8_pv.maegz', 'glide-dock_SP_3NY9_pv.maegz', 'glide-dock_SP_3NYA_pv.maegz', 'glide-dock_SP_3ODU_pv.maegz', 'glide-dock_SP_3OE6_pv.maegz', 'glide-dock_SP_3OE8_pv.maegz', 'glide-dock_SP_3OE9_pv.maegz', 'glide-dock_SP_3P0G_pv.maegz', 'glide-dock_SP_3PBL_pv.maegz', 'glide-dock_SP_3PWH_pv.maegz', 'glide-dock_SP_3QAK_pv.maegz', 'glide-dock_SP_3UON_pv.maegz', 'glide-dock_SP_3UZA_pv.maegz', 'glide-dock_SP_3UZC_pv.maegz', 'glide-dock_SP_3V2W_pv.maegz', 'glide-dock_SP_3V2Y_pv.maegz', 'glide-dock_SP_3VG9_pv.maegz', 'glide-dock_SP_3VGA_pv.maegz', 'glide-dock_SP_3VW7_pv.maegz', 'glide-dock_SP_3ZPQ_pv.maegz', 'glide-dock_SP_3ZPR_pv.maegz', 'glide-dock_SP_4AMJ_pv.maegz', 'glide-dock_SP_4BVN_pv.maegz', 'glide-dock_SP_4DAJ_pv.maegz', 'glide-dock_SP_4EA3_pv.maegz', 'glide-dock_SP_4EIY_pv.maegz', 'glide-dock_SP_4EJ4_pv.maegz', 'glide-dock_SP_4GBR_pv.maegz', 'glide-dock_SP_4IAQ_pv.maegz', 'glide-dock_SP_4IAR_pv.maegz', 'glide-dock_SP_4IB4_pv.maegz', 'glide-dock_SP_4JKV_pv.maegz', 'glide-dock_SP_4K5Y_pv.maegz', 'glide-dock_SP_4LDE_pv.maegz', 'glide-dock_SP_4LDL_pv.maegz', 'glide-dock_SP_4LDO_pv.maegz', 'glide-dock_SP_4MBS_pv.maegz', 'glide-dock_SP_4MQS_pv.maegz', 'glide-dock_SP_4MQT_pv.maegz', 'glide-dock_SP_4N4W_pv.maegz', 'glide-dock_SP_4N6H_pv.maegz', 'glide-dock_SP_4NTJ_pv.maegz', 'glide-dock_SP_4O9R_pv.maegz', 'glide-dock_SP_4OO9_pv.maegz', 'glide-dock_SP_4OR2_pv.maegz', 'glide-dock_SP_4PXZ_pv.maegz', 'glide-dock_SP_4PY0_pv.maegz', 'glide-dock_SP_4QIM_pv.maegz', 'glide-dock_SP_4QIN_pv.maegz', 'glide-dock_SP_4S0V_pv.maegz', 'glide-dock_SP_4U14_pv.maegz', 'glide-dock_SP_4U16_pv.maegz', 'glide-dock_SP_4UG2_pv.maegz', 'glide-dock_SP_4UHR_pv.maegz', 'glide-dock_SP_4XNW_pv.maegz', 'glide-dock_SP_4YAY_pv.maegz', 'glide-dock_SP_4Z34_pv.maegz', 'glide-dock_SP_4Z35_pv.maegz', 'glide-dock_SP_4Z36_pv.maegz', 'glide-dock_SP_4Z9G_pv.maegz', 'glide-dock_SP_4ZJ8_pv.maegz', 'glide-dock_SP_4ZJC_pv.maegz', 'glide-dock_SP_4ZUD_pv.maegz', 'glide-dock_SP_5C1M_pv.maegz', 'glide-dock_SP_5CGC_pv.maegz', 'glide-dock_SP_5CGD_pv.maegz', 'glide-dock_SP_5CXV_pv.maegz', 'glide-dock_SP_5D5B_pv.maegz', 'glide-dock_SP_5D6L_pv.maegz', 'glide-dock_SP_5DHG_pv.maegz', 'glide-dock_SP_5DHH_pv.maegz', 'glide-dock_SP_5DSG_pv.maegz', 'glide-dock_SP_5F8U_pv.maegz', 'glide-dock_SP_5G53_pv.maegz', 'glide-dock_SP_5IU4_pv.maegz', 'glide-dock_SP_5IU7_pv.maegz', 'glide-dock_SP_5IU8_pv.maegz', 'glide-dock_SP_5IUA_pv.maegz', 'glide-dock_SP_5IUB_pv.maegz', 'glide-dock_SP_5JQH_pv.maegz', 'glide-dock_SP_5JTB_pv.maegz', 'glide-dock_SP_5K2A_pv.maegz', 'glide-dock_SP_5K2B_pv.maegz', 'glide-dock_SP_5K2C_pv.maegz', 'glide-dock_SP_5K2D_pv.maegz', 'glide-dock_SP_5L7I_pv.maegz', 'glide-dock_SP_5LWE_pv.maegz', 'glide-dock_SP_5MZJ_pv.maegz', 'glide-dock_SP_5N2R_pv.maegz', 'glide-dock_SP_5N2S_pv.maegz', 'glide-dock_SP_5NDD_pv.maegz', 'glide-dock_SP_5NLX_pv.maegz', 'glide-dock_SP_5NM2_pv.maegz', 'glide-dock_SP_5NM4_pv.maegz', 'glide-dock_SP_5OLG_pv.maegz', 'glide-dock_SP_5OLH_pv.maegz', 'glide-dock_SP_5OLO_pv.maegz', 'glide-dock_SP_5OLV_pv.maegz', 'glide-dock_SP_5OLZ_pv.maegz', 'glide-dock_SP_5OM1_pv.maegz', 'glide-dock_SP_5OM4_pv.maegz', 'glide-dock_SP_5TGZ_pv.maegz', 'glide-dock_SP_5TUD_pv.maegz', 'glide-dock_SP_5TVN_pv.maegz', 'glide-dock_SP_5U09_pv.maegz', 'glide-dock_SP_5UEN_pv.maegz', 'glide-dock_SP_5UIG_pv.maegz', 'glide-dock_SP_5UNF_pv.maegz', 'glide-dock_SP_5UNH_pv.maegz', 'glide-dock_SP_5UVI_pv.maegz', 'glide-dock_SP_5V54_pv.maegz', 'glide-dock_SP_5V56_pv.maegz', 'glide-dock_SP_5V57_pv.maegz', 'glide-dock_SP_5VRA_pv.maegz', 'glide-dock_SP_5WF5_pv.maegz', 'glide-dock_SP_5WF6_pv.maegz', 'glide-dock_SP_5WIU_pv.maegz', 'glide-dock_SP_5WIV_pv.maegz', 'glide-dock_SP_5WQC_pv.maegz', 'glide-dock_SP_5WS3_pv.maegz', 'glide-dock_SP_5X7D_pv.maegz', 'glide-dock_SP_5X93_pv.maegz', 'glide-dock_SP_5XPR_pv.maegz', 'glide-dock_SP_5XR8_pv.maegz', 'glide-dock_SP_5XRA_pv.maegz', 'glide-dock_SP_5ZBH_pv.maegz', 'glide-dock_SP_5ZBQ_pv.maegz', 'glide-dock_SP_5ZHP_pv.maegz', 'glide-dock_SP_5ZK3_pv.maegz', 'glide-dock_SP_5ZK8_pv.maegz', 'glide-dock_SP_5ZKB_pv.maegz', 'glide-dock_SP_5ZKC_pv.maegz', 'glide-dock_SP_5ZKP_pv.maegz', 'glide-dock_SP_5ZKQ_pv.maegz', 'glide-dock_SP_5ZTY_pv.maegz', 'glide-dock_SP_6A93_pv.maegz', 'glide-dock_SP_6A94_pv.maegz', 'glide-dock_SP_6AKX_pv.maegz', 'glide-dock_SP_6B73_pv.maegz', 'glide-dock_SP_6BQG_pv.maegz', 'glide-dock_SP_6BQH_pv.maegz', 'glide-dock_SP_6CM4_pv.maegz', 'glide-dock_SP_6D26_pv.maegz', 'glide-dock_SP_6DRX_pv.maegz', 'glide-dock_SP_6DRY_pv.maegz', 'glide-dock_SP_6DRZ_pv.maegz', 'glide-dock_SP_6DS0_pv.maegz', 'glide-dock_SP_6E59_pv.maegz', 'glide-dock_SP_6E67_pv.maegz', 'glide-dock_SP_6FFH_pv.maegz', 'glide-dock_SP_6FFI_pv.maegz', 'glide-dock_SP_6FK6_pv.maegz', 'glide-dock_SP_6FK7_pv.maegz', 'glide-dock_SP_6FK8_pv.maegz', 'glide-dock_SP_6FK9_pv.maegz', 'glide-dock_SP_6FKA_pv.maegz', 'glide-dock_SP_6FKB_pv.maegz', 'glide-dock_SP_6FKC_pv.maegz', 'glide-dock_SP_6FKD_pv.maegz', 'glide-dock_SP_6GDG_pv.maegz', 'glide-dock_SP_6GPS_pv.maegz', 'glide-dock_SP_6GPX_pv.maegz', 'glide-dock_SP_6GT3_pv.maegz', 'glide-dock_SP_6H7J_pv.maegz', 'glide-dock_SP_6H7L_pv.maegz', 'glide-dock_SP_6H7M_pv.maegz', 'glide-dock_SP_6H7N_pv.maegz', 'glide-dock_SP_6H7O_pv.maegz', 'glide-dock_SP_6HLL_pv.maegz', 'glide-dock_SP_6HLO_pv.maegz', 'glide-dock_SP_6HLP_pv.maegz', 'glide-dock_SP_6IBL_pv.maegz', 'glide-dock_SP_6IIU_pv.maegz', 'glide-dock_SP_6IIV_pv.maegz', 'glide-dock_SP_6IQL_pv.maegz', 'glide-dock_SP_6J20_pv.maegz', 'glide-dock_SP_6J21_pv.maegz', 'glide-dock_SP_6JZH_pv.maegz', 'glide-dock_SP_6K1Q_pv.maegz', 'glide-dock_SP_6KQI_pv.maegz', 'glide-dock_SP_6M9T_pv.maegz', 'glide-dock_SP_6ME2_pv.maegz', 'glide-dock_SP_6ME3_pv.maegz', 'glide-dock_SP_6ME4_pv.maegz', 'glide-dock_SP_6ME5_pv.maegz', 'glide-dock_SP_6ME6_pv.maegz', 'glide-dock_SP_6ME7_pv.maegz', 'glide-dock_SP_6ME8_pv.maegz', 'glide-dock_SP_6ME9_pv.maegz', 'glide-dock_SP_6MH8_pv.maegz', 'glide-dock_SP_6MXT_pv.maegz', 'glide-dock_SP_6N48_pv.maegz', 'glide-dock_SP_6O3C_pv.maegz', 'glide-dock_SP_6OL9_pv.maegz', 'glide-dock_SP_6PRZ_pv.maegz', 'glide-dock_SP_6PS0_pv.maegz', 'glide-dock_SP_6PS1_pv.maegz', 'glide-dock_SP_6PS2_pv.maegz', 'glide-dock_SP_6PS3_pv.maegz', 'glide-dock_SP_6PS4_pv.maegz', 'glide-dock_SP_6PS5_pv.maegz', 'glide-dock_SP_6PS6_pv.maegz', 'glide-dock_SP_6PS7_pv.maegz', 'glide-dock_SP_6PS8_pv.maegz', 'glide-dock_SP_6QZH_pv.maegz', 'glide-dock_SP_6RZ4_pv.maegz', 'glide-dock_SP_6TO7_pv.maegz', 'glide-dock_SP_6TOD_pv.maegz', 'glide-dock_SP_6TP3_pv.maegz', 'glide-dock_SP_6TP4_pv.maegz', 'glide-dock_SP_6TP6_pv.maegz', 'glide-dock_SP_6TPG_pv.maegz', 'glide-dock_SP_6TPJ_pv.maegz', 'glide-dock_SP_6TPN_pv.maegz', 'glide-dock_SP_6TQ4_pv.maegz', 'glide-dock_SP_6TQ6_pv.maegz']
    


```python
print("#!/bin/bash")
for i in file_list:
    print("$SCHRODINGER/run interaction_fingerprints.py -i",i,"-no_properties -ocsv", i[14:18]+'.csv')
    print("$SCHRODINGER/run interaction_fingerprints.py -i",i,"-ocsv", i[14:18]+'_prop.csv')
    
# -no_properties 정말 많은 특징 정보가 추출되기 때문에 상호작용만 추출하는 옵션
# -no_properties이 없으면 RMSD해당하는 결과를 추출할 수 있다. 해당 자료를 만들고 RMSD 컬럼만 추출할 계획

```

    #!/bin/bash
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2I35_pv.maegz -no_properties -ocsv 2I35.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2I35_pv.maegz -ocsv 2I35_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2RH1_pv.maegz -no_properties -ocsv 2RH1.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2RH1_pv.maegz -ocsv 2RH1_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2VT4_pv.maegz -no_properties -ocsv 2VT4.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2VT4_pv.maegz -ocsv 2VT4_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2X72_pv.maegz -no_properties -ocsv 2X72.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2X72_pv.maegz -ocsv 2X72_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2Y00_pv.maegz -no_properties -ocsv 2Y00.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2Y00_pv.maegz -ocsv 2Y00_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2Y01_pv.maegz -no_properties -ocsv 2Y01.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2Y01_pv.maegz -ocsv 2Y01_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2Y02_pv.maegz -no_properties -ocsv 2Y02.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2Y02_pv.maegz -ocsv 2Y02_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2Y03_pv.maegz -no_properties -ocsv 2Y03.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2Y03_pv.maegz -ocsv 2Y03_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2Y04_pv.maegz -no_properties -ocsv 2Y04.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2Y04_pv.maegz -ocsv 2Y04_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2YCW_pv.maegz -no_properties -ocsv 2YCW.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2YCW_pv.maegz -ocsv 2YCW_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2YCX_pv.maegz -no_properties -ocsv 2YCX.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2YCX_pv.maegz -ocsv 2YCX_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2YCY_pv.maegz -no_properties -ocsv 2YCY.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2YCY_pv.maegz -ocsv 2YCY_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2YCZ_pv.maegz -no_properties -ocsv 2YCZ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2YCZ_pv.maegz -ocsv 2YCZ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2YDV_pv.maegz -no_properties -ocsv 2YDV.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_2YDV_pv.maegz -ocsv 2YDV_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3D4S_pv.maegz -no_properties -ocsv 3D4S.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3D4S_pv.maegz -ocsv 3D4S_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3EML_pv.maegz -no_properties -ocsv 3EML.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3EML_pv.maegz -ocsv 3EML_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3NY8_pv.maegz -no_properties -ocsv 3NY8.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3NY8_pv.maegz -ocsv 3NY8_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3NY9_pv.maegz -no_properties -ocsv 3NY9.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3NY9_pv.maegz -ocsv 3NY9_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3NYA_pv.maegz -no_properties -ocsv 3NYA.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3NYA_pv.maegz -ocsv 3NYA_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3ODU_pv.maegz -no_properties -ocsv 3ODU.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3ODU_pv.maegz -ocsv 3ODU_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3OE6_pv.maegz -no_properties -ocsv 3OE6.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3OE6_pv.maegz -ocsv 3OE6_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3OE8_pv.maegz -no_properties -ocsv 3OE8.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3OE8_pv.maegz -ocsv 3OE8_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3OE9_pv.maegz -no_properties -ocsv 3OE9.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3OE9_pv.maegz -ocsv 3OE9_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3P0G_pv.maegz -no_properties -ocsv 3P0G.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3P0G_pv.maegz -ocsv 3P0G_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3PBL_pv.maegz -no_properties -ocsv 3PBL.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3PBL_pv.maegz -ocsv 3PBL_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3PWH_pv.maegz -no_properties -ocsv 3PWH.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3PWH_pv.maegz -ocsv 3PWH_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3QAK_pv.maegz -no_properties -ocsv 3QAK.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3QAK_pv.maegz -ocsv 3QAK_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3UON_pv.maegz -no_properties -ocsv 3UON.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3UON_pv.maegz -ocsv 3UON_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3UZA_pv.maegz -no_properties -ocsv 3UZA.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3UZA_pv.maegz -ocsv 3UZA_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3UZC_pv.maegz -no_properties -ocsv 3UZC.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3UZC_pv.maegz -ocsv 3UZC_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3V2W_pv.maegz -no_properties -ocsv 3V2W.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3V2W_pv.maegz -ocsv 3V2W_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3V2Y_pv.maegz -no_properties -ocsv 3V2Y.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3V2Y_pv.maegz -ocsv 3V2Y_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3VG9_pv.maegz -no_properties -ocsv 3VG9.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3VG9_pv.maegz -ocsv 3VG9_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3VGA_pv.maegz -no_properties -ocsv 3VGA.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3VGA_pv.maegz -ocsv 3VGA_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3VW7_pv.maegz -no_properties -ocsv 3VW7.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3VW7_pv.maegz -ocsv 3VW7_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3ZPQ_pv.maegz -no_properties -ocsv 3ZPQ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3ZPQ_pv.maegz -ocsv 3ZPQ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3ZPR_pv.maegz -no_properties -ocsv 3ZPR.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_3ZPR_pv.maegz -ocsv 3ZPR_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4AMJ_pv.maegz -no_properties -ocsv 4AMJ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4AMJ_pv.maegz -ocsv 4AMJ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4BVN_pv.maegz -no_properties -ocsv 4BVN.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4BVN_pv.maegz -ocsv 4BVN_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4DAJ_pv.maegz -no_properties -ocsv 4DAJ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4DAJ_pv.maegz -ocsv 4DAJ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4EA3_pv.maegz -no_properties -ocsv 4EA3.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4EA3_pv.maegz -ocsv 4EA3_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4EIY_pv.maegz -no_properties -ocsv 4EIY.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4EIY_pv.maegz -ocsv 4EIY_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4EJ4_pv.maegz -no_properties -ocsv 4EJ4.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4EJ4_pv.maegz -ocsv 4EJ4_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4GBR_pv.maegz -no_properties -ocsv 4GBR.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4GBR_pv.maegz -ocsv 4GBR_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4IAQ_pv.maegz -no_properties -ocsv 4IAQ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4IAQ_pv.maegz -ocsv 4IAQ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4IAR_pv.maegz -no_properties -ocsv 4IAR.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4IAR_pv.maegz -ocsv 4IAR_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4IB4_pv.maegz -no_properties -ocsv 4IB4.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4IB4_pv.maegz -ocsv 4IB4_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4JKV_pv.maegz -no_properties -ocsv 4JKV.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4JKV_pv.maegz -ocsv 4JKV_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4K5Y_pv.maegz -no_properties -ocsv 4K5Y.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4K5Y_pv.maegz -ocsv 4K5Y_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4LDE_pv.maegz -no_properties -ocsv 4LDE.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4LDE_pv.maegz -ocsv 4LDE_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4LDL_pv.maegz -no_properties -ocsv 4LDL.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4LDL_pv.maegz -ocsv 4LDL_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4LDO_pv.maegz -no_properties -ocsv 4LDO.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4LDO_pv.maegz -ocsv 4LDO_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4MBS_pv.maegz -no_properties -ocsv 4MBS.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4MBS_pv.maegz -ocsv 4MBS_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4MQS_pv.maegz -no_properties -ocsv 4MQS.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4MQS_pv.maegz -ocsv 4MQS_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4MQT_pv.maegz -no_properties -ocsv 4MQT.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4MQT_pv.maegz -ocsv 4MQT_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4N4W_pv.maegz -no_properties -ocsv 4N4W.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4N4W_pv.maegz -ocsv 4N4W_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4N6H_pv.maegz -no_properties -ocsv 4N6H.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4N6H_pv.maegz -ocsv 4N6H_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4NTJ_pv.maegz -no_properties -ocsv 4NTJ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4NTJ_pv.maegz -ocsv 4NTJ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4O9R_pv.maegz -no_properties -ocsv 4O9R.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4O9R_pv.maegz -ocsv 4O9R_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4OO9_pv.maegz -no_properties -ocsv 4OO9.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4OO9_pv.maegz -ocsv 4OO9_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4OR2_pv.maegz -no_properties -ocsv 4OR2.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4OR2_pv.maegz -ocsv 4OR2_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4PXZ_pv.maegz -no_properties -ocsv 4PXZ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4PXZ_pv.maegz -ocsv 4PXZ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4PY0_pv.maegz -no_properties -ocsv 4PY0.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4PY0_pv.maegz -ocsv 4PY0_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4QIM_pv.maegz -no_properties -ocsv 4QIM.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4QIM_pv.maegz -ocsv 4QIM_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4QIN_pv.maegz -no_properties -ocsv 4QIN.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4QIN_pv.maegz -ocsv 4QIN_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4S0V_pv.maegz -no_properties -ocsv 4S0V.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4S0V_pv.maegz -ocsv 4S0V_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4U14_pv.maegz -no_properties -ocsv 4U14.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4U14_pv.maegz -ocsv 4U14_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4U16_pv.maegz -no_properties -ocsv 4U16.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4U16_pv.maegz -ocsv 4U16_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4UG2_pv.maegz -no_properties -ocsv 4UG2.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4UG2_pv.maegz -ocsv 4UG2_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4UHR_pv.maegz -no_properties -ocsv 4UHR.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4UHR_pv.maegz -ocsv 4UHR_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4XNW_pv.maegz -no_properties -ocsv 4XNW.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4XNW_pv.maegz -ocsv 4XNW_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4YAY_pv.maegz -no_properties -ocsv 4YAY.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4YAY_pv.maegz -ocsv 4YAY_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4Z34_pv.maegz -no_properties -ocsv 4Z34.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4Z34_pv.maegz -ocsv 4Z34_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4Z35_pv.maegz -no_properties -ocsv 4Z35.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4Z35_pv.maegz -ocsv 4Z35_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4Z36_pv.maegz -no_properties -ocsv 4Z36.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4Z36_pv.maegz -ocsv 4Z36_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4Z9G_pv.maegz -no_properties -ocsv 4Z9G.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4Z9G_pv.maegz -ocsv 4Z9G_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4ZJ8_pv.maegz -no_properties -ocsv 4ZJ8.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4ZJ8_pv.maegz -ocsv 4ZJ8_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4ZJC_pv.maegz -no_properties -ocsv 4ZJC.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4ZJC_pv.maegz -ocsv 4ZJC_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4ZUD_pv.maegz -no_properties -ocsv 4ZUD.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_4ZUD_pv.maegz -ocsv 4ZUD_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5C1M_pv.maegz -no_properties -ocsv 5C1M.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5C1M_pv.maegz -ocsv 5C1M_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5CGC_pv.maegz -no_properties -ocsv 5CGC.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5CGC_pv.maegz -ocsv 5CGC_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5CGD_pv.maegz -no_properties -ocsv 5CGD.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5CGD_pv.maegz -ocsv 5CGD_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5CXV_pv.maegz -no_properties -ocsv 5CXV.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5CXV_pv.maegz -ocsv 5CXV_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5D5B_pv.maegz -no_properties -ocsv 5D5B.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5D5B_pv.maegz -ocsv 5D5B_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5D6L_pv.maegz -no_properties -ocsv 5D6L.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5D6L_pv.maegz -ocsv 5D6L_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5DHG_pv.maegz -no_properties -ocsv 5DHG.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5DHG_pv.maegz -ocsv 5DHG_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5DHH_pv.maegz -no_properties -ocsv 5DHH.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5DHH_pv.maegz -ocsv 5DHH_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5DSG_pv.maegz -no_properties -ocsv 5DSG.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5DSG_pv.maegz -ocsv 5DSG_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5F8U_pv.maegz -no_properties -ocsv 5F8U.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5F8U_pv.maegz -ocsv 5F8U_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5G53_pv.maegz -no_properties -ocsv 5G53.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5G53_pv.maegz -ocsv 5G53_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5IU4_pv.maegz -no_properties -ocsv 5IU4.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5IU4_pv.maegz -ocsv 5IU4_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5IU7_pv.maegz -no_properties -ocsv 5IU7.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5IU7_pv.maegz -ocsv 5IU7_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5IU8_pv.maegz -no_properties -ocsv 5IU8.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5IU8_pv.maegz -ocsv 5IU8_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5IUA_pv.maegz -no_properties -ocsv 5IUA.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5IUA_pv.maegz -ocsv 5IUA_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5IUB_pv.maegz -no_properties -ocsv 5IUB.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5IUB_pv.maegz -ocsv 5IUB_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5JQH_pv.maegz -no_properties -ocsv 5JQH.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5JQH_pv.maegz -ocsv 5JQH_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5JTB_pv.maegz -no_properties -ocsv 5JTB.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5JTB_pv.maegz -ocsv 5JTB_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5K2A_pv.maegz -no_properties -ocsv 5K2A.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5K2A_pv.maegz -ocsv 5K2A_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5K2B_pv.maegz -no_properties -ocsv 5K2B.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5K2B_pv.maegz -ocsv 5K2B_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5K2C_pv.maegz -no_properties -ocsv 5K2C.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5K2C_pv.maegz -ocsv 5K2C_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5K2D_pv.maegz -no_properties -ocsv 5K2D.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5K2D_pv.maegz -ocsv 5K2D_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5L7I_pv.maegz -no_properties -ocsv 5L7I.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5L7I_pv.maegz -ocsv 5L7I_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5LWE_pv.maegz -no_properties -ocsv 5LWE.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5LWE_pv.maegz -ocsv 5LWE_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5MZJ_pv.maegz -no_properties -ocsv 5MZJ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5MZJ_pv.maegz -ocsv 5MZJ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5N2R_pv.maegz -no_properties -ocsv 5N2R.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5N2R_pv.maegz -ocsv 5N2R_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5N2S_pv.maegz -no_properties -ocsv 5N2S.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5N2S_pv.maegz -ocsv 5N2S_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5NDD_pv.maegz -no_properties -ocsv 5NDD.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5NDD_pv.maegz -ocsv 5NDD_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5NLX_pv.maegz -no_properties -ocsv 5NLX.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5NLX_pv.maegz -ocsv 5NLX_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5NM2_pv.maegz -no_properties -ocsv 5NM2.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5NM2_pv.maegz -ocsv 5NM2_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5NM4_pv.maegz -no_properties -ocsv 5NM4.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5NM4_pv.maegz -ocsv 5NM4_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OLG_pv.maegz -no_properties -ocsv 5OLG.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OLG_pv.maegz -ocsv 5OLG_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OLH_pv.maegz -no_properties -ocsv 5OLH.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OLH_pv.maegz -ocsv 5OLH_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OLO_pv.maegz -no_properties -ocsv 5OLO.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OLO_pv.maegz -ocsv 5OLO_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OLV_pv.maegz -no_properties -ocsv 5OLV.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OLV_pv.maegz -ocsv 5OLV_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OLZ_pv.maegz -no_properties -ocsv 5OLZ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OLZ_pv.maegz -ocsv 5OLZ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OM1_pv.maegz -no_properties -ocsv 5OM1.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OM1_pv.maegz -ocsv 5OM1_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OM4_pv.maegz -no_properties -ocsv 5OM4.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5OM4_pv.maegz -ocsv 5OM4_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5TGZ_pv.maegz -no_properties -ocsv 5TGZ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5TGZ_pv.maegz -ocsv 5TGZ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5TUD_pv.maegz -no_properties -ocsv 5TUD.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5TUD_pv.maegz -ocsv 5TUD_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5TVN_pv.maegz -no_properties -ocsv 5TVN.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5TVN_pv.maegz -ocsv 5TVN_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5U09_pv.maegz -no_properties -ocsv 5U09.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5U09_pv.maegz -ocsv 5U09_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5UEN_pv.maegz -no_properties -ocsv 5UEN.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5UEN_pv.maegz -ocsv 5UEN_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5UIG_pv.maegz -no_properties -ocsv 5UIG.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5UIG_pv.maegz -ocsv 5UIG_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5UNF_pv.maegz -no_properties -ocsv 5UNF.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5UNF_pv.maegz -ocsv 5UNF_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5UNH_pv.maegz -no_properties -ocsv 5UNH.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5UNH_pv.maegz -ocsv 5UNH_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5UVI_pv.maegz -no_properties -ocsv 5UVI.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5UVI_pv.maegz -ocsv 5UVI_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5V54_pv.maegz -no_properties -ocsv 5V54.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5V54_pv.maegz -ocsv 5V54_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5V56_pv.maegz -no_properties -ocsv 5V56.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5V56_pv.maegz -ocsv 5V56_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5V57_pv.maegz -no_properties -ocsv 5V57.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5V57_pv.maegz -ocsv 5V57_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5VRA_pv.maegz -no_properties -ocsv 5VRA.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5VRA_pv.maegz -ocsv 5VRA_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5WF5_pv.maegz -no_properties -ocsv 5WF5.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5WF5_pv.maegz -ocsv 5WF5_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5WF6_pv.maegz -no_properties -ocsv 5WF6.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5WF6_pv.maegz -ocsv 5WF6_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5WIU_pv.maegz -no_properties -ocsv 5WIU.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5WIU_pv.maegz -ocsv 5WIU_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5WIV_pv.maegz -no_properties -ocsv 5WIV.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5WIV_pv.maegz -ocsv 5WIV_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5WQC_pv.maegz -no_properties -ocsv 5WQC.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5WQC_pv.maegz -ocsv 5WQC_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5WS3_pv.maegz -no_properties -ocsv 5WS3.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5WS3_pv.maegz -ocsv 5WS3_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5X7D_pv.maegz -no_properties -ocsv 5X7D.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5X7D_pv.maegz -ocsv 5X7D_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5X93_pv.maegz -no_properties -ocsv 5X93.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5X93_pv.maegz -ocsv 5X93_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5XPR_pv.maegz -no_properties -ocsv 5XPR.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5XPR_pv.maegz -ocsv 5XPR_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5XR8_pv.maegz -no_properties -ocsv 5XR8.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5XR8_pv.maegz -ocsv 5XR8_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5XRA_pv.maegz -no_properties -ocsv 5XRA.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5XRA_pv.maegz -ocsv 5XRA_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZBH_pv.maegz -no_properties -ocsv 5ZBH.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZBH_pv.maegz -ocsv 5ZBH_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZBQ_pv.maegz -no_properties -ocsv 5ZBQ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZBQ_pv.maegz -ocsv 5ZBQ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZHP_pv.maegz -no_properties -ocsv 5ZHP.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZHP_pv.maegz -ocsv 5ZHP_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZK3_pv.maegz -no_properties -ocsv 5ZK3.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZK3_pv.maegz -ocsv 5ZK3_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZK8_pv.maegz -no_properties -ocsv 5ZK8.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZK8_pv.maegz -ocsv 5ZK8_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZKB_pv.maegz -no_properties -ocsv 5ZKB.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZKB_pv.maegz -ocsv 5ZKB_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZKC_pv.maegz -no_properties -ocsv 5ZKC.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZKC_pv.maegz -ocsv 5ZKC_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZKP_pv.maegz -no_properties -ocsv 5ZKP.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZKP_pv.maegz -ocsv 5ZKP_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZKQ_pv.maegz -no_properties -ocsv 5ZKQ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZKQ_pv.maegz -ocsv 5ZKQ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZTY_pv.maegz -no_properties -ocsv 5ZTY.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_5ZTY_pv.maegz -ocsv 5ZTY_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6A93_pv.maegz -no_properties -ocsv 6A93.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6A93_pv.maegz -ocsv 6A93_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6A94_pv.maegz -no_properties -ocsv 6A94.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6A94_pv.maegz -ocsv 6A94_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6AKX_pv.maegz -no_properties -ocsv 6AKX.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6AKX_pv.maegz -ocsv 6AKX_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6B73_pv.maegz -no_properties -ocsv 6B73.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6B73_pv.maegz -ocsv 6B73_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6BQG_pv.maegz -no_properties -ocsv 6BQG.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6BQG_pv.maegz -ocsv 6BQG_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6BQH_pv.maegz -no_properties -ocsv 6BQH.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6BQH_pv.maegz -ocsv 6BQH_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6CM4_pv.maegz -no_properties -ocsv 6CM4.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6CM4_pv.maegz -ocsv 6CM4_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6D26_pv.maegz -no_properties -ocsv 6D26.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6D26_pv.maegz -ocsv 6D26_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6DRX_pv.maegz -no_properties -ocsv 6DRX.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6DRX_pv.maegz -ocsv 6DRX_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6DRY_pv.maegz -no_properties -ocsv 6DRY.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6DRY_pv.maegz -ocsv 6DRY_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6DRZ_pv.maegz -no_properties -ocsv 6DRZ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6DRZ_pv.maegz -ocsv 6DRZ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6DS0_pv.maegz -no_properties -ocsv 6DS0.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6DS0_pv.maegz -ocsv 6DS0_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6E59_pv.maegz -no_properties -ocsv 6E59.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6E59_pv.maegz -ocsv 6E59_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6E67_pv.maegz -no_properties -ocsv 6E67.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6E67_pv.maegz -ocsv 6E67_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FFH_pv.maegz -no_properties -ocsv 6FFH.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FFH_pv.maegz -ocsv 6FFH_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FFI_pv.maegz -no_properties -ocsv 6FFI.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FFI_pv.maegz -ocsv 6FFI_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FK6_pv.maegz -no_properties -ocsv 6FK6.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FK6_pv.maegz -ocsv 6FK6_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FK7_pv.maegz -no_properties -ocsv 6FK7.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FK7_pv.maegz -ocsv 6FK7_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FK8_pv.maegz -no_properties -ocsv 6FK8.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FK8_pv.maegz -ocsv 6FK8_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FK9_pv.maegz -no_properties -ocsv 6FK9.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FK9_pv.maegz -ocsv 6FK9_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FKA_pv.maegz -no_properties -ocsv 6FKA.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FKA_pv.maegz -ocsv 6FKA_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FKB_pv.maegz -no_properties -ocsv 6FKB.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FKB_pv.maegz -ocsv 6FKB_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FKC_pv.maegz -no_properties -ocsv 6FKC.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FKC_pv.maegz -ocsv 6FKC_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FKD_pv.maegz -no_properties -ocsv 6FKD.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6FKD_pv.maegz -ocsv 6FKD_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6GDG_pv.maegz -no_properties -ocsv 6GDG.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6GDG_pv.maegz -ocsv 6GDG_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6GPS_pv.maegz -no_properties -ocsv 6GPS.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6GPS_pv.maegz -ocsv 6GPS_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6GPX_pv.maegz -no_properties -ocsv 6GPX.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6GPX_pv.maegz -ocsv 6GPX_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6GT3_pv.maegz -no_properties -ocsv 6GT3.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6GT3_pv.maegz -ocsv 6GT3_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6H7J_pv.maegz -no_properties -ocsv 6H7J.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6H7J_pv.maegz -ocsv 6H7J_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6H7L_pv.maegz -no_properties -ocsv 6H7L.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6H7L_pv.maegz -ocsv 6H7L_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6H7M_pv.maegz -no_properties -ocsv 6H7M.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6H7M_pv.maegz -ocsv 6H7M_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6H7N_pv.maegz -no_properties -ocsv 6H7N.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6H7N_pv.maegz -ocsv 6H7N_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6H7O_pv.maegz -no_properties -ocsv 6H7O.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6H7O_pv.maegz -ocsv 6H7O_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6HLL_pv.maegz -no_properties -ocsv 6HLL.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6HLL_pv.maegz -ocsv 6HLL_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6HLO_pv.maegz -no_properties -ocsv 6HLO.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6HLO_pv.maegz -ocsv 6HLO_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6HLP_pv.maegz -no_properties -ocsv 6HLP.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6HLP_pv.maegz -ocsv 6HLP_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6IBL_pv.maegz -no_properties -ocsv 6IBL.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6IBL_pv.maegz -ocsv 6IBL_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6IIU_pv.maegz -no_properties -ocsv 6IIU.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6IIU_pv.maegz -ocsv 6IIU_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6IIV_pv.maegz -no_properties -ocsv 6IIV.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6IIV_pv.maegz -ocsv 6IIV_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6IQL_pv.maegz -no_properties -ocsv 6IQL.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6IQL_pv.maegz -ocsv 6IQL_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6J20_pv.maegz -no_properties -ocsv 6J20.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6J20_pv.maegz -ocsv 6J20_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6J21_pv.maegz -no_properties -ocsv 6J21.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6J21_pv.maegz -ocsv 6J21_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6JZH_pv.maegz -no_properties -ocsv 6JZH.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6JZH_pv.maegz -ocsv 6JZH_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6K1Q_pv.maegz -no_properties -ocsv 6K1Q.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6K1Q_pv.maegz -ocsv 6K1Q_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6KQI_pv.maegz -no_properties -ocsv 6KQI.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6KQI_pv.maegz -ocsv 6KQI_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6M9T_pv.maegz -no_properties -ocsv 6M9T.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6M9T_pv.maegz -ocsv 6M9T_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME2_pv.maegz -no_properties -ocsv 6ME2.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME2_pv.maegz -ocsv 6ME2_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME3_pv.maegz -no_properties -ocsv 6ME3.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME3_pv.maegz -ocsv 6ME3_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME4_pv.maegz -no_properties -ocsv 6ME4.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME4_pv.maegz -ocsv 6ME4_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME5_pv.maegz -no_properties -ocsv 6ME5.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME5_pv.maegz -ocsv 6ME5_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME6_pv.maegz -no_properties -ocsv 6ME6.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME6_pv.maegz -ocsv 6ME6_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME7_pv.maegz -no_properties -ocsv 6ME7.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME7_pv.maegz -ocsv 6ME7_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME8_pv.maegz -no_properties -ocsv 6ME8.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME8_pv.maegz -ocsv 6ME8_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME9_pv.maegz -no_properties -ocsv 6ME9.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6ME9_pv.maegz -ocsv 6ME9_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6MH8_pv.maegz -no_properties -ocsv 6MH8.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6MH8_pv.maegz -ocsv 6MH8_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6MXT_pv.maegz -no_properties -ocsv 6MXT.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6MXT_pv.maegz -ocsv 6MXT_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6N48_pv.maegz -no_properties -ocsv 6N48.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6N48_pv.maegz -ocsv 6N48_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6O3C_pv.maegz -no_properties -ocsv 6O3C.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6O3C_pv.maegz -ocsv 6O3C_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6OL9_pv.maegz -no_properties -ocsv 6OL9.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6OL9_pv.maegz -ocsv 6OL9_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PRZ_pv.maegz -no_properties -ocsv 6PRZ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PRZ_pv.maegz -ocsv 6PRZ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS0_pv.maegz -no_properties -ocsv 6PS0.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS0_pv.maegz -ocsv 6PS0_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS1_pv.maegz -no_properties -ocsv 6PS1.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS1_pv.maegz -ocsv 6PS1_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS2_pv.maegz -no_properties -ocsv 6PS2.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS2_pv.maegz -ocsv 6PS2_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS3_pv.maegz -no_properties -ocsv 6PS3.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS3_pv.maegz -ocsv 6PS3_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS4_pv.maegz -no_properties -ocsv 6PS4.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS4_pv.maegz -ocsv 6PS4_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS5_pv.maegz -no_properties -ocsv 6PS5.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS5_pv.maegz -ocsv 6PS5_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS6_pv.maegz -no_properties -ocsv 6PS6.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS6_pv.maegz -ocsv 6PS6_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS7_pv.maegz -no_properties -ocsv 6PS7.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS7_pv.maegz -ocsv 6PS7_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS8_pv.maegz -no_properties -ocsv 6PS8.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6PS8_pv.maegz -ocsv 6PS8_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6QZH_pv.maegz -no_properties -ocsv 6QZH.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6QZH_pv.maegz -ocsv 6QZH_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6RZ4_pv.maegz -no_properties -ocsv 6RZ4.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6RZ4_pv.maegz -ocsv 6RZ4_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TO7_pv.maegz -no_properties -ocsv 6TO7.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TO7_pv.maegz -ocsv 6TO7_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TOD_pv.maegz -no_properties -ocsv 6TOD.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TOD_pv.maegz -ocsv 6TOD_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TP3_pv.maegz -no_properties -ocsv 6TP3.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TP3_pv.maegz -ocsv 6TP3_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TP4_pv.maegz -no_properties -ocsv 6TP4.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TP4_pv.maegz -ocsv 6TP4_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TP6_pv.maegz -no_properties -ocsv 6TP6.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TP6_pv.maegz -ocsv 6TP6_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TPG_pv.maegz -no_properties -ocsv 6TPG.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TPG_pv.maegz -ocsv 6TPG_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TPJ_pv.maegz -no_properties -ocsv 6TPJ.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TPJ_pv.maegz -ocsv 6TPJ_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TPN_pv.maegz -no_properties -ocsv 6TPN.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TPN_pv.maegz -ocsv 6TPN_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TQ4_pv.maegz -no_properties -ocsv 6TQ4.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TQ4_pv.maegz -ocsv 6TQ4_prop.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TQ6_pv.maegz -no_properties -ocsv 6TQ6.csv
    $SCHRODINGER/run interaction_fingerprints.py -i glide-dock_SP_6TQ6_pv.maegz -ocsv 6TQ6_prop.csv
    


```python
#Interaction Fingerprints Provides a graphical interface to compute interaction fingerprints between a receptor and ligands similar to those described in Deng et al, J. Med Chem (2004), 47, 337.    
```

## 실행 파일 만들기(Shell script)
vi test.sh ## vi 편집기를 통해 sh file 생성

파일 첫줄에 해당 내용 기입
#!/bin/bash
다음 원하는 명령어 추가함

저장후 권한 부여
chmod +x test.sh$SCHRODINGER/run interaction_fingerprints.py
해당 작업은 이전 작업이 끝나면 다음 작업이 진행됨

```python

```
