import os

# 기준 디렉터리 설정 (현재 디렉터리 기준)
base_directory = "."

# 변경할 대상 파일명
target_filename = "POC_GMX.itp"

# 디렉터리 순회하며 파일 찾기 및 수정
for root, dirs, files in os.walk(base_directory):
    if target_filename in files:
        file_path = os.path.join(root, target_filename)
        print(f"Modifying: {file_path}")

        # 파일 읽기 및 "MOL" -> "POC" 변경
        with open(file_path, 'r') as file:
            content = file.read()
        
        updated_content = content.replace("MOL", "POC")

        # 변경된 내용 다시 저장
        with open(file_path, 'w') as file:
            file.write(updated_content)

print("All modifications completed.")

