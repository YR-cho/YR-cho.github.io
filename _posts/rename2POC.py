import os

# 1. 현재 디렉토리 내 폴더 탐색
current_dir = os.getcwd()
folders = [f for f in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, f))]

# 2. 각 폴더 내 mol2 파일 이름 변경
for folder in folders:
    folder_path = os.path.join(current_dir, folder)
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    for file in files:
        if file.endswith('.mol2'):
            source_path = os.path.join(folder_path, file)
            new_name = "POC.mol2"
            destination_path = os.path.join(folder_path, new_name)
            
            # 파일 이름 변경
            os.rename(source_path, destination_path)

print("모든 mol2 파일의 이름이 POC로 변경되었습니다.")
