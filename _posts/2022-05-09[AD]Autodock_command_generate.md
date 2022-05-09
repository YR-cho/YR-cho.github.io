```python
import os
import pandas as pd
```


```python
path = "./Ligands" 
file_list = os.listdir(path) 
```


```python
for i in file_list:
    print('"C:\Program Files (x86)\The Scripps Research Institute\Vina\\vina.exe" --config protocol_'+i[0:-6]+'.txt')
print("이게 마지막")
```

    "C:\Program Files (x86)\The Scripps Research Institute\Vina\vina.exe" --config protocol_g4g43g2.txt
    "C:\Program Files (x86)\The Scripps Research Institute\Vina\vina.exe" --config protocol_sdfaf.txt
    "C:\Program Files (x86)\The Scripps Research Institute\Vina\vina.exe" --config protocol_SDSD.txt
    이게 마지막
    
