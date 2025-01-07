import os
import shutil

# 1. 현재 디렉토리 내 파일 탐색
current_dir = os.getcwd()  # 현재 디렉토리 경로 가져오기
files = [f for f in os.listdir(current_dir) if os.path.isfile(os.path.join(current_dir, f))]

# 2. 확장자를 기준으로 같은 이름의 파일을 폴더로 정리
for file in files:
    # 파일 이름과 확장자 분리
    filename, ext = os.path.splitext(file)
    
    # '.'을 제거한 확장자
    folder_name = filename

    # 파일 이름 기반으로 폴더 생성 (이미 존재하면 무시)
    folder_path = os.path.join(current_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # 파일 이동
    source_path = os.path.join(current_dir, file)
    destination_path = os.path.join(folder_path, file)
    shutil.move(source_path, destination_path)
