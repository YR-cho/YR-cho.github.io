import os

# 기준 경로 설정 (현재 디렉토리 기준으로 설정)
base_path = "./"  # 작업을 수행할 상위 경로로 바꿔주세요

# 상위 경로의 모든 폴더에 대해 반복
for folder_name in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder_name)
    
    # 폴더인지 확인
    if os.path.isdir(folder_path):
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".pdb"):
                old_file_path = os.path.join(folder_path, file_name)
                new_file_path = os.path.join(folder_path, f"{folder_name}.pdb")
                
                # 파일 이름 변경
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")
