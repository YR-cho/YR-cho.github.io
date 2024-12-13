import os
import shutil

# 기준 디렉터리 설정 (현재 디렉터리 기준)
base_directory = "."

# 복사할 대상 파일 목록
target_files = ["POC_GMX.gro", "POC_GMX.itp"]

# 파일 이름이 중복될 경우 숫자를 추가하는 함수
def get_unique_filename(directory, filename):
    name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{name}_{counter}{ext}"
        counter += 1

    return new_filename

# 하위 폴더의 파일을 상위 폴더로 복사하는 함수
def copy_files_to_parent():
    for root, dirs, files in os.walk(base_directory):
        for target_file in target_files:
            if target_file in files:
                source_path = os.path.join(root, target_file)
                
                # 상위 폴더 경로 설정
                parent_directory = os.path.dirname(root)
                unique_filename = get_unique_filename(parent_directory, target_file)
                destination_path = os.path.join(parent_directory, unique_filename)
                
                # 파일 복사
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {source_path} -> {destination_path}")

# 함수 실행
copy_files_to_parent()
print("All target files have been copied to their parent directories.")
