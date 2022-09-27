### Python Version 2.XX
### For Linux

import os

for root, dirs, files in os.walk('./'):
    
    for file in files:
		g = open('./A1_%s.in' % file , 'w')  ### 생성된 모든 파일에 A1이라는 헤드문자 들어감
		g.write('GRIDFILE "/home/fandg90/Albendazole/%s"\n' % file)  ### 반복문으로 생성되는 Grid file 마다 들어감.
		g.write('LIGANDFILE "/home/fandg90/Albendazole/Albendazole_1.mae"\n')  ### Ligand는 고정
		g.write('POSTDOCK_NPOSE   1\n') ### pose 생성은 1개
		g.write('PRECISION  SP') ### Docking 알고리즘
		g.close()
