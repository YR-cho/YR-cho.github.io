```python
import os
```


```python
path = "./Ligands" 
file_list = os.listdir(path) 
```


```python
for i in file_list:
    print("f = open('./protocol_"+i[0:-6]+".txt'", ',"w")')
    print("f.write('receptor = 1vkx.pdbqt\\n')")
    print("f.write('ligand = ./Ligands/"+i,"\\n')")
    print("f.write('center_x = -20.610000610351562\\n')")
    print("f.write('center_y = 10.670000076293945\\n')")
    print("f.write('center_z = 85.9800033569336\\n')")
    print("f.write('size_x = 40\\n')")
    print("f.write('size_y = 40\\n')")
    print("f.write('size_z = 40\\n')")
    print("f.write('out = Result_"+i,"\\n')")
    print("f.write('log = log_"+i[0:-6]+".log')")
    print("f.close()")
```

    f = open('./protocol_g4g43g2.txt' ,"w")
    f.write('receptor = 1vkx.pdbqt\n')
    f.write('ligand = ./Ligands/g4g43g2.pdbqt \n')
    f.write('center_x = -20.610000610351562\n')
    f.write('center_y = 10.670000076293945\n')
    f.write('center_z = 85.9800033569336\n')
    f.write('size_x = 40\n')
    f.write('size_y = 40\n')
    f.write('size_z = 40\n')
    f.write('out = Result_g4g43g2.pdbqt \n')
    f.write('log = log_g4g43g2.log')
    f.close()
    f = open('./protocol_sdfaf.txt' ,"w")
    f.write('receptor = 1vkx.pdbqt\n')
    f.write('ligand = ./Ligands/sdfaf.pdbqt \n')
    f.write('center_x = -20.610000610351562\n')
    f.write('center_y = 10.670000076293945\n')
    f.write('center_z = 85.9800033569336\n')
    f.write('size_x = 40\n')
    f.write('size_y = 40\n')
    f.write('size_z = 40\n')
    f.write('out = Result_sdfaf.pdbqt \n')
    f.write('log = log_sdfaf.log')
    f.close()
    f = open('./protocol_SDSD.txt' ,"w")
    f.write('receptor = 1vkx.pdbqt\n')
    f.write('ligand = ./Ligands/SDSD.pdbqt \n')
    f.write('center_x = -20.610000610351562\n')
    f.write('center_y = 10.670000076293945\n')
    f.write('center_z = 85.9800033569336\n')
    f.write('size_x = 40\n')
    f.write('size_y = 40\n')
    f.write('size_z = 40\n')
    f.write('out = Result_SDSD.pdbqt \n')
    f.write('log = log_SDSD.log')
    f.close()
    


```python
f = open('./protocol_g4g43g2.txt' ,"w")
f.write('receptor = 1vkx.pdbqt\n')
f.write('ligand = ./Ligands/g4g43g2.pdbqt \n')
f.write('center_x = -20.610000610351562\n')
f.write('center_y = 10.670000076293945\n')
f.write('center_z = 85.9800033569336\n')
f.write('size_x = 40\n')
f.write('size_y = 40\n')
f.write('size_z = 40\n')
f.write('out = Result_g4g43g2.pdbqt \n')
f.write('log = log_g4g43g2.log')
f.close()
f = open('./protocol_sdfaf.txt' ,"w")
f.write('receptor = 1vkx.pdbqt\n')
f.write('ligand = ./Ligands/sdfaf.pdbqt \n')
f.write('center_x = -20.610000610351562\n')
f.write('center_y = 10.670000076293945\n')
f.write('center_z = 85.9800033569336\n')
f.write('size_x = 40\n')
f.write('size_y = 40\n')
f.write('size_z = 40\n')
f.write('out = Result_sdfaf.pdbqt \n')
f.write('log = log_sdfaf.log')
f.close()
f = open('./protocol_SDSD.txt' ,"w")
f.write('receptor = 1vkx.pdbqt\n')
f.write('ligand = ./Ligands/SDSD.pdbqt \n')
f.write('center_x = -20.610000610351562\n')
f.write('center_y = 10.670000076293945\n')
f.write('center_z = 85.9800033569336\n')
f.write('size_x = 40\n')
f.write('size_y = 40\n')
f.write('size_z = 40\n')
f.write('out = Result_SDSD.pdbqt \n')
f.write('log = log_SDSD.log')
f.close()
```


```python

```


```python

```


```python

```


```python

```
