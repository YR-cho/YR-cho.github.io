import os
import sys

sys.stdout = open('script_code.txt',"a")
path = "./input_file"

#===============================================================

file_list = os.listdir(path)
for file_name in file_list:
    print("$SCHRODINGER/glide",file_name)
